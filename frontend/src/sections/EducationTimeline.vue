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

  // Ensure a proper date format (YYYY-MM) to work on firefox
  const formatToISO = (dateString) => {
    const [year, month] = dateString.split("/");
    return new Date(`${year}-${month.padStart(2, "0")}-01`);
  };

  const from = formatToISO(period[0]).toLocaleDateString("en-US", {
    month: "2-digit",
    year: "numeric",
  });

  const to = formatToISO(period[1]).toLocaleDateString("en-US", {
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
  <div class="text-textPrimary">
    <div class="relative mb-16">
      <h2>
        <p class="mr-2 text-primaryColor">Educational</p>
        <p class="ml-24 lg:ml-0">background</p>
      </h2>
      <div
        class="h-1 w-20 top-10 absolute lg:relative lg:top-0 underline bg-primaryColor"
      />
    </div>

    <!-- Timeline -->
    <ul class="list-none pl-0 mt-8 flex flex-col gap-12 lg:gap-16">
      <!-- Loop throught items and create an element for everyone of them -->
      <li
        v-for="(item, index) in orderedItems"
        :key="index"
        class="relative flex flex-col md:flex-row items-start space-x-4 rounded-lg bg-bgSecondary justify-center"
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
          <div class="flex flex-col items-start justify-between">
            <div class="lg:absolute top-0 right-0 flex space-x-2">
              <span
                v-for="date in _formatItemDate(item)"
                :key="date.label"
                class="text-xs text-textPrimary px-2 py-1 rounded glass-effect"
                v-html="date.label"
              ></span>
            </div>
            <div>
              <h4
                class="text-lg font-semibold text-textPrimary"
                v-html="item.title"
              ></h4>
              <h6 class="text-sm text-gray-500">
                {{ item.place ? item.place : "" }}
              </h6>
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

        <!-- <hr
          v-if="index !== orderedItems.length - 1"
          class="h-1 w-3/4 absolute -bottom-6 left-1/2 transform -translate-x-1/2 bg-white opacity-15 backdrop-blur-sm"
        /> -->
      </li>
    </ul>
  </div>
</template>
