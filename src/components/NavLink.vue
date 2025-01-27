<template>
  <a
    :href="to"
    class="text-textPrimary px-3 py-3 uppercase hover:text-primaryColor duration-150 transition-colors"
  >
    <slot></slot>
  </a>
</template>

<script>
export default {
  name: "NavLink",
  props: {
    to: {
      type: String,
      required: true,
    },
  },
};
</script>
