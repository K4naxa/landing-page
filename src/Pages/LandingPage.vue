<script setup>
import EducationTimeline from "../sections/EducationTimeline.vue";
import About from "../sections/About.vue";
import Layout from "../layouts/layout.vue";
import Portfolio from "../sections/portfolio.vue";
</script>
<template>
  <div>
    <Layout />

    <About />

    <div class="h-1 w-3/4 bg-bgSecondary rounded-full mx-auto" />

    <EducationTimeline />

    <div class="h-1 w-3/4 bg-bgSecondary rounded-full mx-auto" />

    <Portfolio />
  </div>
</template>
>
