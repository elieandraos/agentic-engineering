# Inertia Forms

`inertia-vue-development` and `wayfinder-development` already establish the `<Form>` component, bound
to a Wayfinder route helper, as the default way to build a named-input form:

```vue
<Form v-bind="routeHelper.form()" v-slot="{ errors, processing }">
    <!-- named inputs -->
</Form>
```

Keep using `useForm()` only when `form.transform()`, or another genuinely client-side transformation,
is required and cannot reasonably be handled by the backend. This file adds the one delta Boost
doesn't cover: making a custom Vue control participate in `<Form>` serialization.

## Make custom controls serializable

A custom component that is driven only by `v-model` and does not render a native named control should expose an optional `name` prop and render a hidden input when `name` is provided. The hidden input mirrors the component's current value so it participates in `<Form>` serialization.

```vue
<script setup lang="ts">
const props = defineProps<{
    modelValue: string;
    name?: string;
}>();
</script>

<template>
    <!-- visible control omitted -->
    <input v-if="props.name" type="hidden" :name="props.name" :value="props.modelValue" />
</template>
```

For components with internal derived values, keep the existing reactive state and derive the hidden value from that state rather than maintaining a second independent form value.

For invisible defaults that need no custom control, use a normal hidden input in the page itself.

Native controls and components that already forward `$attrs` to their native input/select do not need a custom serialization layer.
