<script setup>
import { computed, ref } from "vue";
import portfolioItems from "/src/Data/portfolio.json";
import projectModal from "../components/projectModal.vue";

const orderedItems = computed(() => [...portfolioItems.items]);
const showModal = ref(false);
const selectedProject = ref({});
const clickPosition = ref({ x: 0, y: 0 });

const openModal = (item, event) => {
  // Get the clicked element's bounding rectangle
  const rect = event.currentTarget.getBoundingClientRect();

  // Calculate the center point of the clicked portfolio item
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;

  // Store the center coordinates
  clickPosition.value = {
    x: centerX,
    y: centerY,
  };

  selectedProject.value = item;
  showModal.value = true;
  document.body.classList.add("no-scroll");
  // Push a new state to the browser history, so that user can swipe back from the modal
  history.pushState({ modalOpen: false }, "", "");
  history.pushState({ modalOpen: true }, "", "");
};

const closeModal = () => {
  showModal.value = false;
  document.body.classList.remove("no-scroll");
  history.back();
};
</script>

<template>
  <div class="mx-auto text-textPrimary scroll-m-16 lg:scroll-m-0">
    <!-- Header -->
    <div class="relative mb-16">
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
        @click="(event) => openModal(item, event)"
        class="p-4 bg-bgSecondary rounded-lg cursor-pointer duration-150 transition-all glass-effect lg:hover:-translate-y-2 lg:hover:shadow-lg lg:hover:bg-primaryColor/15 lg:hover:shadow-primaryColor/30"
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
          class="object-contain flex items-center justify-center object-center h-36 mx-auto rounded-lg w-full mb-4"
        >
          Coming soon
        </div>

        <div>
          <h3 class="text-lg mb-2 uppercase text-center">
            {{ item.title }}
          </h3>
          <div class="flex items-center flex-wrap w-full gap-2">
            <div
              v-for="(tech, i) in item.stack"
              :key="i"
              class="px-3 py-1 rounded-full text-xs glass-effect bg-primaryColor/10"
            >
              {{ tech }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Project Modal -->

  <projectModal
    v-if="showModal"
    :selectedProject="selectedProject"
    :clickPosition="clickPosition"
    @closeModal="closeModal"
  />
</template>
