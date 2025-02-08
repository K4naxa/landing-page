<script setup>
import { defineProps, defineEmits } from "vue";

const props = defineProps({
  isMobile: Boolean,
  sections: Array,
  activeSection: String,
});

// scroll to sectio functionality
const emit = defineEmits(["scrollToSection"]);
const scrollToSection = (sectionId) => {
  emit("scrollToSection", sectionId);
};
</script>
<template>
  <div class="hidden lg:flex w-96 h-screen z-50 justify-center">
    <!-- left side bar content -->
    <div
      class="flex flex-col my-auto h-fit justify-center glass-effect rounded-lg p-8"
    >
      <!-- photo + name -->
      <!-- <div class="flex flex-col items-center mb-8">
        <div
          class="flex h-3/4 w-3/4 mb-4 justify-center content-center rounded-full overflow-hidden relative z-10"
        >
          <img
            class="object-center object-cover aspect-square"
            alt="hero"
            src="../assets/Hero.jpg"
          />
        </div>
        <h2 class="text-white text-xl font-bold">Jami Hyvärinen</h2>
        <p class="text-white text-sm">Fullstack Web Developer</p>
      </div> -->

      <!-- Nav buttons -->
      <nav class="flex flex-col space-y-4">
        <button
          v-for="section in sections"
          :key="section.id"
          @click="scrollToSection(section.id)"
          :class="[
            'text-white px-4 py-2 rounded transition-all border border-transparent',
            activeSection === section.id
              ? 'bg-primaryColor'
              : 'hover:bg-primaryColor hover:bg-opacity-20 hover:border-primaryColor',
          ]"
        >
          {{ section.name }}
        </button>
      </nav>
    </div>
  </div>
</template>
