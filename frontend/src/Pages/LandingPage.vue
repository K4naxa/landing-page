<script setup>
import EducationTimeline from "../sections/EducationTimeline.vue";
import About from "../sections/About.vue";
import Layout from "../layouts/Layout.vue";
import Portfolio from "../sections/portfolio.vue";
</script>
<template>
  <div class="bg-gradient-to-tr from-bgPrimary to-bgLinear overflow-x-hidden">
    <Layout>
      <About />

      <EducationTimeline />

      <Portfolio />
    </Layout>
  </div>
</template>
>
