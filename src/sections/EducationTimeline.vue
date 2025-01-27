<script setup>
import { computed } from "vue";
import educationData from "/src/Data/education.json";

// Reverse the items array
const orderedItems = computed(() => [...educationData.items].reverse());

/**
 * Format date range
 * @param {Object} item
 * @return {Array<{faIcon: string, label: string}>}
 */
const _formatItemDate = (item) => {
  const period = item.period;
  const from = new Date(period[0]).toLocaleDateString("en-US", {
    month: "2-digit",
    year: "numeric",
  });
  const to = new Date(period[1]).toLocaleDateString("en-US", {
    month: "2-digit",
    year: "numeric",
  });

  return [
    {
      label: `${from} ➔ ${to}`,
    },
  ];
};
</script>
<template>
  <section id="education" class="py-8 mx-auto text-textPrimary">
    <div>
      <h2>
        <p class="mr-2 text-primaryColor">Educational</p>
        background
      </h2>
      <div class="h-1 w-20 underline bg-primaryColor" />
    </div>

    <!-- Timeline -->
    <ul class="list-none pl-0 mt-8">
      <!-- Loop throught items and create an element for everyone of them -->
      <li
        v-for="(item, index) in orderedItems"
        :key="index"
        class="relative mb-8 flex flex-col md:flex-row items-start space-x-4 rounded-lg p-4 bg-bgSecondary justify-center"
      >
        <!-- Logo Wrapper -->
        <div
          class="flex mb-8 lg:my-auto items-center justify-center h-20 w-full md:w-20"
        >
          <div
            class="relative my-auto z-10 flex items-center justify-center w-20 h-20 rounded-full"
            :class="{ 'bg-primary-100': !(item.place && item.logo) }"
          >
            <!-- If item has an image -->
            <img
              v-if="item && item.logo"
              :src="item.logo"
              class="rounded-full w-full h-full object-scale-down"
            />
          </div>
        </div>

        <!-- Item Content -->
        <div class="flex-1">
          <!-- Header -->
          <div class="flex items-start justify-between">
            <div>
              <h4
                class="text-lg font-semibold text-textPrimary"
                v-html="item.title"
              ></h4>
              <h6 class="text-sm text-gray-500">
                {{ item.place ? item.place : "" }}
              </h6>
            </div>
            <div class="absolute top-0 right-0 mt-2 mr-2">
              <span
                v-for="date in _formatItemDate(item)"
                :key="date.label"
                class="text-xs bg-primaryColor text-textPrimary px-2 py-1 rounded"
                v-html="date.label"
              ></span>
            </div>
          </div>

          <!-- Body -->
          <div class="mt-2 text-sm text-gray-300">
            <p v-html="item.description"></p>
            <div class="mt-2">
              <span
                v-for="tag in item.tags"
                :key="tag"
                class="text-xs bg-primary-100 text-primary-700 px-2 py-1 rounded"
              >
                {{ tag }}
              </span>
            </div>
          </div>
        </div>
      </li>
    </ul>
  </section>
</template>
