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
};

const closeModal = () => {
  showModal.value = false;
  document.body.classList.remove("no-scroll");
};
</script>

<template>
  <section id="portfolio" class="py-8 mx-auto text-textPrimary">
    <div>
      <h2 class="flex items-center">
        My
        <p class="ml-3 text-primaryColor">Portfolio</p>
      </h2>
      <div class="h-1 w-12 underline bg-primaryColor" />
    </div>

    <!-- Portfolio Items -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mt-8">
      <div
        v-for="(item, index) in orderedItems"
        @click="openModal(item)"
        class="p-4 bg-bgSecondary rounded-lg object-fill cursor-pointer hover:shadow-xl hover:scale-105 duration-150 transition-transform shadow-primaryColor"
        :key="index"
      >
        <img
          class="object-contain object-center h-36 mx-auto rounded-lg w-full mb-4"
          :src="item.image"
          alt="project image"
        />

        <div>
          <h3 class="text-primaryColor text-2xl mb-2 text-center">
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
  </section>

  <!-- Project Modal -->
  <div
    v-if="showModal"
    class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 text-textPrimary z-50"
    @click.self="closeModal"
  >
    <div
      class="bg-bgPrimary rounded-lg max-w-2xl w-full h-full p-6 relative lg:max-h-[90vh] overflow-auto scrollbar-thin"
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

      <h3 class="text-primaryColor text-2xl mb-4">
        {{ selectedProject.title }}
      </h3>
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
        <h4 class="text-primaryColor text-lg mb-2">Key features</h4>
        <ul class="list-disc list-inside">
          <li v-for="(feature, i) in selectedProject.key_features" :key="i">
            {{ feature }}
          </li>
        </ul>
      </div>

      <div class="mb-6">
        <h4 class="text-primaryColor text-lg mb-2">Technical Highlights</h4>
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
      <div class="flex justify-between">
        <a
          :href="selectedProject.documentation"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md border p-2 text-primaryColor bg-bgSecondary"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none':
              !selectedProject.documentation,
          }"
        >
          Documentation
        </a>
        <a
          :href="selectedProject.github"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md border p-2 text-primaryColor"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none':
              !selectedProject.github,
          }"
        >
          Github
        </a>
        <a
          :href="selectedProject.demo"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md bg-primaryColor text-white p-2"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none':
              !selectedProject.demo,
          }"
        >
          Live Demo
        </a>
      </div>
    </div>
  </div>
</template>
