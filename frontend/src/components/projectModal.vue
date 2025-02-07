<script setup>
import { computed, ref, defineProps, defineEmits } from "vue";

const props = defineProps({
  showModal: Boolean,
  selectedProject: Object,
});

const showModal = computed(() => props.showModal);
const selectedProject = computed(() => props.selectedProject);

const emits = defineEmits(["closeModal"]);
const closeModal = () => {
  emits("closeModal");
};
</script>
<template>
  <div
    class="fixed inset-0 bg-black bg-opacity-50 flex items-center backdrop-blur-sm justify-center text-textPrimary z-50"
    @click.self="closeModal"
  >
    <div
      class="bg-black/ rounded-lg lg:max-w-4xl flex flex-col w-full h-full lg:h-fit px-4 py-8 relative lg:max-h-[90vh] overflow-auto scrollbar-thin bg-black/90 border border-gray-400 border-opacity-50"
    >
      <button
        @click="closeModal"
        class="absolute top-2 right-2 text-textPrimary hover:text-primaryColor"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-6 w-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>

      <img
        class="object-cover object-center mx-auto rounded-lg h-64 mb-6"
        :src="selectedProject.image"
        alt="project image"
      />

      <div class="mb-6">
        <h2>
          {{ selectedProject.title }}
        </h2>
        <div class="h-1 w-20 underline bg-primaryColor" />
      </div>
      <p class="text-textSecondary mb-6">{{ selectedProject.description }}</p>

      <div class="flex flex-wrap gap-2 mb-6">
        <div
          v-for="(tech, i) in selectedProject.stack"
          :key="i"
          class="bg-primaryColor px-3 py-1 rounded-full text-xs"
        >
          {{ tech }}
        </div>
      </div>

      <div class="mb-6">
        <div>
          <h2 class="flex items-center text-lg">
            Key
            <p class="ml-2 text-primaryColor">Features</p>
          </h2>
        </div>
        <ul class="list-disc list-inside">
          <li v-for="(feature, i) in selectedProject.key_features" :key="i">
            {{ feature }}
          </li>
        </ul>
      </div>

      <div class="mb-6">
        <h2 class="flex items-center text-lg">
          Technical
          <p class="ml-2 text-primaryColor">Highlights</p>
        </h2>
        <ul class="list-disc list-inside">
          <li
            v-for="(highlight, i) in selectedProject.technical_highlights"
            :key="i"
          >
            {{ highlight }}
          </li>
        </ul>
      </div>

      <!-- Links -->
      <div class="flex flex-wrap gap-4">
        <a
          :href="selectedProject.documentation"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md flex gap-2 border border-primaryColor text-textPrimary px-4 py-2 hover:bg-primaryColor hover:text-bgPrimary transition-colors duration-150"
          :class="{
            'opacity-30 cursor-not-allowed pointer-events-none':
              !selectedProject.documentation,
          }"
        >
          Documentation
        </a>
        <a
          :href="selectedProject.github"
          target="_blank"
          class="rounded-md flex gap-2 border border-primaryColor text-textPrimary px-4 py-2 hover:bg-primaryColor hover:text-bgPrimary transition-colors duration-150"
          :class="{
            'opacity-30 cursor-not-allowed pointer-events-none':
              !selectedProject.github,
          }"
        >
          <img
            src="/src/assets/github-mark-white.png"
            alt="github logo"
            class="h-6 w-6"
          />
          Github
        </a>
        <a
          :href="selectedProject.demo"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md flex gap-2 border bg-primaryColor border-primaryColor text-white px-4 py-2 hover:text-bgPrimary transition-colors duration-150"
          :class="{
            'opacity-30 cursor-not-allowed pointer-events-none':
              !selectedProject.demo,
          }"
        >
          Demo
        </a>
      </div>
    </div>
  </div>
</template>
