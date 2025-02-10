<script setup>
import {
  computed,
  ref,
  defineProps,
  defineEmits,
  onMounted,
  onUnmounted,
} from "vue";

const props = defineProps({
  showModal: Boolean,
  selectedProject: Object,
  clickPosition: Object,
});

const showModal = computed(() => props.showModal);
const selectedProject = computed(() => props.selectedProject);
const isAnimating = ref(true);

const emits = defineEmits(["closeModal"]);
const closeModal = () => {
  isAnimating.value = true;
  setTimeout(() => {
    emits("closeModal");
  }, 300);
};

onMounted(() => {
  window.addEventListener("popstate", handlePopState);
  setTimeout(() => {
    isAnimating.value = false;
  }, 50);
});

onUnmounted(() => {
  window.removeEventListener("popstate", handlePopState);
});

const handlePopState = (event) => {
  if (showModal) {
    closeModal();
  }
};
</script>
<template>
  <div
    id="projectModal"
    class="fixed inset-0 bg-black bg-opacity-50 flex items-center backdrop-blur-sm justify-center text-textPrimary z-50"
    @click.self="closeModal"
  >
    <div
      class="modal-content bg-black/90 rounded-lg lg:max-w-4xl flex flex-col w-full h-full lg:h-fit px-4 py-8 relative lg:max-h-[90vh] overflow-auto scrollbar-thin lg:border border-gray-400 border-opacity-50"
      :style="{
        '--click-x': clickPosition.x + 'px',
        '--click-y': clickPosition.y + 'px',
      }"
      :class="{ 'modal-entering': isAnimating }"
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
        v-if="selectedProject.image"
        class="object-cover object-center mx-auto rounded-lg h-64 mb-6"
        :src="selectedProject.image"
        alt="project image"
      />
      <span v-else>
        <div
          class="object-contain flex items-center justify-center object-center h-32 mx-auto glass-effect rounded-lg mb-6 max-w-96"
        >
          Coming soon...
        </div>
      </span>

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
          class="bg-primaryColor px-3 py-1 rounded-full text-xs glass-effect select-none"
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
          class="rounded-md flex gap-2 px-4 py-2 hover:bg-primaryColor button-effects"
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
          class="rounded-md flex gap-2 px-4 py-2 hover:bg-primaryColor button-effects"
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
          v-if="selectedProject.demo"
          :href="selectedProject.demo"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md flex gap-2 px-4 py-2 hover:bg-primaryColor bg-primaryColor select-none hover:bg-opacity-80"
          :class="{
            'opacity-30 cursor-not-allowed pointer-events-none':
              !selectedProject.demo,
          }"
        >
          Demo
        </a>
        <a
          v-if="selectedProject.live"
          :href="selectedProject.live"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md flex gap-2 px-4 py-2 hover:bg-primaryColor bg-primaryColor select-none hover:bg-opacity-80"
          :class="{
            'opacity-30 cursor-not-allowed pointer-events-none':
              !selectedProject.live,
          }"
        >
          Live site
        </a>
      </div>
    </div>
  </div>
</template>
<style scoped>
.modal-content {
  transform-origin: var(--click-x) var(--click-y);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, opacity;
}

.modal-entering {
  transform: scale(0.3);
  opacity: 0;
}

.modal-content:not(.modal-entering) {
  transform: scale(1);
  opacity: 1;
}
</style>
