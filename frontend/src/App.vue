<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import EducationTimeline from "./sections/EducationTimeline.vue";
import About from "./sections/About.vue";
import Portfolio from "./sections/portfolio.vue";
import Contact from "./sections/Contact.vue";
import Layout from "./layouts/Layout.vue";

const isMobile = ref(false);
const checkMobile = () => {
  isMobile.value = window.innerWidth <= 1027;
};

onMounted(() => {
  checkMobile();
  window.addEventListener("resize", checkMobile);

  onUnmounted(() => {
    window.removeEventListener("resize", checkMobile);
  });
});
</script>

<template>
  <!-- Animated background -->
  <div class="animated-background"></div>

  <div class="main-container">
    <!-- Pass in a helper class for mobile to disable outer vertical scroll -->
    <Layout :isMobile="isMobile" class="">
      <section id="about" class="section">
        <div class="lg:mx-8 mx-auto">
          <About />
        </div>
      </section>

      <section id="education" class="section">
        <div class="section-content w-screen lg:w-full lg:mx-8">
          <EducationTimeline />
        </div>
      </section>

      <section id="portfolio" class="section">
        <div class="section-content w-screen lg:w-full lg:mx-8">
          <Portfolio />
        </div>
      </section>

      <section id="contact" class="section">
        <Contact />
      </section>
    </Layout>
  </div>
</template>

<style scoped>
/* Outer container for the whole app */
.main-container {
  min-height: 100dvh;
  position: relative;
  overflow-x: hidden;
  /* When not on mobile, you might want vertical scroll */
  overflow-y: auto;
  backdrop-filter: blur(16px);
  background: rgba(0, 0, 0, 0.1);
}

.section {
  position: relative;
  display: flex;
  flex-shrink: 0;
  overflow-x: hidden;
}

/* Desktop styles */
@media screen and (min-width: 1024px) {
  .section {
    min-height: 100vh;
    width: auto; /* Let the container decide */
    align-items: center;
    @apply mx-8;
  }
}

/* Mobile styles */
@media screen and (max-width: 1023px) {
  .section {
    width: 100vw; /* Each slide fills the viewport width */
    /* Start content at the top so nothing is hidden */
    align-items: flex-start;
    @apply p-8;
  }
}

/* Background animation */
@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

.animated-background {
  position: fixed;
  top: 0;
  left: 0;
  will-change: background-position;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    30deg,
    rgb(230, 0, 69),
    /* rgb(34, 38, 42), */ rgb(0, 8, 10),
    rgb(0, 8, 10),
    rgb(170, 0, 51)
  );
  background-size: 400% 300%;
  animation: gradient 15s ease infinite;
  z-index: 0;

  /* Mobile */
  @media screen and (max-width: 1024px) {
    background-size: 300% 200%;
    animation: gradient 5s infinite;
  }
}
</style>
