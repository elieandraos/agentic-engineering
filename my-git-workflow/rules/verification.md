# Verification

Two different full-suite runs exist in this workflow — one before Gate 1, one at the completed-issue
boundary — and they are not a duplicate of each other, even though both run the same command:

> Gate 1 full-suite verification validates the completed working tree before history is written.
> The final issue-boundary full suite validates the assembled commit history as actually committed.

The first proves the implementation is correct as a single working tree, before any commit exists
to review or split. The second proves the *commits* — however many the issue was split into,
whatever order they landed in — reconstruct that same correct state when read back from git. They
answer different questions, so both stay in the loop; don't drop one because the other already ran
green.

## Default loop: targeted per commit, full suite once at the issue boundary

While building a single commit — whether it's the whole issue (#288, #287) or one step of a
multi-commit issue (#120, #289) — verify it with the tests actually relevant to that commit's
change (`php artisan test --compact <path>`) plus `vendor/bin/pint --dirty --format agent`. Do not
reflexively run the full suite after every commit; that's slow and, for a step that's deliberately
inert (see `rules/commit-boundaries.md`'s persistence-layer examples), it proves nothing the
targeted run didn't already cover.

Run the **full regression suite once**, at the completed-issue boundary — after the last commit for
that issue, before reporting the issue done. This is the moment that actually matters: it's the
proof that the whole issue, landed as however many commits it took, didn't regress anything else in
the app. Every issue in the evidence (#288, #287, #120, #289) ended this way — one full-suite run,
reported with its exact pass/skip/fail counts.

## Stronger technique: isolation verification, when a split needs real proof

> Do not use isolation verification merely because an issue was split into multiple commits. Use it
> when the intermediate committed states are themselves a property that needs to be proven, such as
> a history rewrite or commit ordering whose correctness depends on sequence.

Some situations need more than "I verified the pieces as I wrote them" — they need proof that each
*committed* state, read back from git in order, actually stands on its own. Reach for this when:

- Reconstructing an already-implemented diff into semantic commits after the fact (#120's rebase).
- Building a multi-commit issue where the commit *order* is itself load-bearing for correctness —
  e.g. a feature flag that would retroactively activate other tests before their supporting code
  has landed (#120, #289; see `rules/commit-boundaries.md` and the ordering note below).

The technique, exactly as used for both #120 and #289:

1. Commit the first semantic group.
2. `git stash push -u -m "<description>"` — hides every change not yet committed (staged,
   unstaged, and untracked), leaving the working tree at exactly the state of the commits made so
   far.
3. Run `vendor/bin/pint --test --format agent` and the **full** `php artisan test --compact`
   against that isolated state.
4. `git stash pop` — restores the remaining work.
5. Repeat for each subsequent commit: stage the next semantic group, commit, stash the rest,
   verify in isolation, pop.
6. After the last commit, run one final full-suite pass with nothing stashed — the completed-issue
   boundary check from above.

This is expensive (a full suite run per commit), which is exactly why it's a tool to reach for
deliberately, not a default. #288 and #287 never needed it — each was one commit, verified once,
same as the issue boundary. #120 and #289 needed it because "does this intermediate commit actually
stand alone" was the property being asserted, not assumed.

## Ordering commits to keep intermediate states green

Watch specifically for feature-flag activation retroactively changing what's under test.
`skipUnlessFortifyHas()`-style runtime-gated tests (or any test conditioned on config/feature
state) are silent until the moment the gating condition flips — and when it does, every test that
was quietly skipped starts running immediately, against whatever code currently exists.

This is exactly what happened while ordering #120's commits: enabling Fortify's 2FA feature flag
would have un-skipped three pre-existing tests in `SecurityTest.php` — a file the issue never
touched — whose assertions depended on `SecurityController` changes that were still a separate,
not-yet-landed commit. Landing "enable the feature flag" before "wire the controller" would have
made the flag-enabling commit red on its own, breaking the isolation guarantee.

The fix was to reorder: land the controller wiring (inert while the flag is off — `Features::` 
helpers all read `false`, so nothing observable changes) *before* the commit that flips the flag on.
The flag-enabling commit then lands last, and activates everything at once — including retroactively
proving the earlier, inert-looking commits correct.

Before committing a step that changes config/feature state, check whether any currently-skipped
test in the repo (not just the ones this issue is adding) would start running as a result, and
confirm its dependencies are already committed. If they aren't, reorder — don't land a commit that
will read as green in isolation today but was only green because a gate hid the real assertions.
