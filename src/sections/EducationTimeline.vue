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
  <section id="education" class="py-8 max-w-5xl mx-auto text-textPrimary">
    <div>
      <h2>
        <p class="mr-2 text-primaryColor">Educational</p>
        background
      </h2>
      <div class="h-1 w-20 underline bg-primaryColor" />
    </div>

    <!-- Timeline -->
    <ul class="relative list-none pl-0 mt-8">
      <!-- Vertical line -->
      <div class="absolute z-10 top-10 left-12 w-px h-full bg-gray-200" />

      <!-- Loop throught items and create an element for everyone of them -->
      <li
        v-for="(item, index) in orderedItems"
        :key="index"
        class="relative mb-8 flex items-start space-x-4 rounded-lg p-4 bg-bgSecondary"
      >
        <!-- Logo Wrapper -->
        <div
          class="relative my-auto z-20 flex items-center justify-center w-16 h-16 rounded-full border-4 border-gray-300 bg-gray-100"
          :class="{ 'bg-primary-100': !(item.place && item.place.logoUrl) }"
        >
          <!-- If item has an image -->
          <img
            v-if="item && item.logoUrl"
            :src="item.logoUrl"
            class="rounded-full w-full h-full object-cover"
          />
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
            <div>
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
