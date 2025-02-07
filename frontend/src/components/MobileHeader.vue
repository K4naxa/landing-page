<script setup>
import { ref, onMounted, onUnmounted, defineProps, defineEmits } from "vue";

const props = defineProps({
  isMobile: Boolean,
  sections: Array,
  activeSection: String,
});

const emit = defineEmits(["scrollToSection"]);

const scrollToSection = (sectionId) => {
  emit("scrollToSection", sectionId);
};
</script>
<template>
  <header
    class="lg:hidden transition-transform flex items-center duration-300 glass-effect h-[--header-height]"
  >
    <!-- Mobile Navigation -->

    <nav class="px-4 py-2 grid grid-cols-4 gap-4 w-full">
      <button
        v-for="section in sections"
        :key="section.id"
        @click="scrollToSection(section.id)"
        :class="[
          'w-full text-textPrimary py-2 rounded transition-all text-center',
          activeSection === section.id
            ? 'bg-primaryColor'
            : 'hover:bg-primaryColor/20',
        ]"
      >
        {{ section.name }}
      </button>
    </nav>
  </header>
</template>
