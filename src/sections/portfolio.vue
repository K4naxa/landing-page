<script setup>
import { computed } from "vue";
import portfolioItems from "/src/Data/portfolio.json";

const orderedItems = computed(() => [...portfolioItems.items]);

console.log(portfolioItems);
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
    <div
      v-for="(item, index) in orderedItems"
      class="p-4 bg-bgSecondary rounded-lg mt-8 max-w-96"
      :key="index"
    >
      <img
        class="object-cover object-center mx-auto rounded-lg w-full mt-4"
        :src="item.image"
        alt="project image"
      />

      <div>
        <div class="flex items-center justify-between w-full mb-4">
          <div
            v-for="i in item.stack"
            class="bg-primaryColor px-3 py-1 rounded-full text-xs"
          >
            {{ i }}
          </div>
        </div>
        <h3 class="text-primaryColor text-2xl mb-4">{{ item.title }}</h3>
        <p class="text-textSecondary">{{ item.description }}</p>
      </div>

      <div class="w-full flex justify-between mt-4">
        <a
          :href="item.documentation"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md border p-2 text-primaryColor"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none':
              !item.documentation,
          }"
        >
          Documentation
        </a>
        <a
          :href="item.github"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md border p-2 text-primaryColor"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none': !item.github,
          }"
        >
          Github
        </a>
        <a
          :href="item.demo"
          target="_blank"
          rel="noopener noreferrer"
          class="rounded-md bg-primaryColor text-white p-2"
          :class="{
            'opacity-50 cursor-not-allowed pointer-events-none': !item.demo,
          }"
        >
          Live Demo
        </a>
      </div>
    </div>
  </section>
</template>
