<script setup>
import EducationTimeline from "./sections/EducationTimeline.vue";
import About from "./sections/About.vue";
import Layout from "./layouts/Layout.vue";
import Portfolio from "./sections/portfolio.vue";
import Contact from "./sections/Contact.vue";

import { ref, onMounted, onUnmounted } from "vue";

const isMobile = ref(false);

onMounted(() => {
  const checkMobile = () => {
    console.log(window.innerWidth);
    isMobile.value = window.innerWidth <= 1027;
  };

  checkMobile();
  window.addEventListener("resize", checkMobile);

  // Cleanup event listener on component unmount
  onUnmounted(() => {
    window.removeEventListener("resize", checkMobile);
  });
});
</script>

<template>
  <!-- Animated background -->
  <div class="animated-background"></div>
  <div class="main-container">
    <!-- Glass container -->

    <Layout :isMobile="isMobile">
      <section id="about" class="section">
        <div
          class="section-content w-screen lg:w-full lg:mx-8"
          :class="isMobile ? '' : 'glass-effect'"
        >
          <About />
        </div>
      </section>

      <section id="education" class="section">
        <div
          class="section-content w-screen lg:w-full lg:mx-8"
          :class="isMobile ? '' : 'glass-effect'"
        >
          <EducationTimeline />
        </div>
      </section>

      <section id="portfolio" class="section">
        <div
          class="section-content w-screen lg:w-full lg:mx-8"
          :class="isMobile ? '' : 'glass-effect'"
        >
          <Portfolio />
        </div>
      </section>

      <section id="contact" class="section">
        <div
          class="section-content w-screen lg:w-full lg:mx-8"
          :class="isMobile ? '' : 'glass-effect'"
        >
          <Contact />
        </div>
      </section>
    </Layout>
  </div>
</template>

<style scoped>
.main-container {
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
  overflow-y: auto;
  backdrop-filter: blur(16px);
  background: rgba(0, 0, 0, 0.1);
}
</style>
