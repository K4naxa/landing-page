<script setup>
import { computed } from "vue";
import portfolioItems from "/src/Data/portfolio.json";

// Reverse the items array
const orderedItems = computed(() => [...educationData.items].reverse());
</script>
<template>
  <section id="portfolio" class="py-8 max-w-5xl mx-auto text-textPrimary">
    <div>
      <h2>
        My
        <p class="ml-3 text-primaryColor">Portfolio</p>
      </h2>
      <div class="h-1 w-12 underline bg-primaryColor" />
    </div>

    <!-- Portfolio Items -->
    <div v-for="(project, index) in portfolioItems">
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
    </div>
  </section>
</template>
