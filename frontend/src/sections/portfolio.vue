<script setup>
import { computed, ref } from "vue";
import portfolioItems from "/src/Data/portfolio.json";

const orderedItems = computed(() => [...portfolioItems.items]);
const showModal = ref(false);
const selectedProject = ref({});

const openModal = (item) => {
  selectedProject.value = item;
  showModal.value = true;
  document.body.classList.add("no-scroll");
  // Push a new state to the browser history, so that user can swipe back from the modal
  history.pushState({ modalOpen: false }, "", "");
  history.pushState({ modalOpen: true }, "", "");
  window.addEventListener("popstate", handlePopState);
};

const closeModal = () => {
  showModal.value = false;
  document.body.classList.remove("no-scroll");
  history.back();
};

const handlePopState = (event) => {
  // Close the modal if the back button is pressed
  if (showModal) {
    closeModal();
    window.removeEventListener("popstate", handlePopState);
  }
};
</script>

<template>
  <div class="mx-auto text-textPrimary scroll-m-16 lg:scroll-m-0">
    <!-- Header -->
    <div class="mb-8">
      <h2 class="flex items-center">
        My
        <p class="ml-3 text-primaryColor">Portfolio</p>
      </h2>
      <div class="h-1 w-12 underline bg-primaryColor" />
    </div>

    <!-- Portfolio Items -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div
        v-for="(item, index) in orderedItems"
        @click="openModal(item)"
        class="p-4 bg-bgSecondary rounded-lg cursor-pointer duration-150 transition-all glass-effect hover:-translate-y-2 hover:shadow-lg hover:shadow-primaryColor"
        :key="index"
      >
        <img
          v-if="item.image"
          class="object-contain object-center h-36 mx-auto rounded-lg w-full mb-4"
          :src="item.image"
          alt="project image"
        />
        <div
          v-else
          class="object-contain flex items-center justify-center object-center h-36 mx-auto rounded-lg w-full mb-4 font-semibold text-lg text-primaryColor text-opacity-50"
        >
          Coming soon...
        </div>

        <div>
          <h3 class="text-lg mb-2 uppercase text-center">
            {{ item.title }}
          </h3>
          <div class="flex items-center flex-wrap w-full gap-2">
            <div
              v-for="(tech, i) in item.stack"
              :key="i"
              class="bg-primaryColor px-3 py-1 rounded-full text-xs"
            >
              {{ tech }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Project Modal -->
  <div
    v-if="showModal"
    class="fixed inset-0 bg-black bg-opacity-50 flex items-center backdrop-blur-sm justify-center text-textPrimary z-50"
    @click.self="closeModal"
  >
    <div
      class="bg-bgPrimary rounded-lg lg:max-w-4xl flex flex-col w-full h-full lg:h-fit p-6 relative lg:max-h-[90vh] overflow-auto scrollbar-thin"
    >
      <button
        @click="closeModal"
        class="absolute top-4 right-4 text-textPrimary hover:text-primaryColor"
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
