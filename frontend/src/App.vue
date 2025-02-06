<script setup>
import EducationTimeline from "./sections/EducationTimeline.vue";
import About from "./sections/About.vue";
import Layout from "./layouts/Layout.vue";
import Portfolio from "./sections/portfolio.vue";
import Contact from "./sections/Contact.vue";
</script>

<template>
  <!-- Animated background -->
  <div class="animated-background"></div>
  <div class="main-container">
    <!-- Glass container -->

    <Layout>
      <section id="about" class="section">
        <div class="section-content glass-effect">
          <About />
        </div>
      </section>

      <section id="education" class="section">
        <div class="section-content glass-effect">
          <EducationTimeline />
        </div>
      </section>

      <section id="portfolio" class="section">
        <div class="section-content glass-effect">
          <Portfolio />
        </div>
      </section>

      <section id="contact" class="section">
        <div class="section-content glass-effect">
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
  overflow: hidden;
  backdrop-filter: blur(16px);
  background: rgba(0, 0, 0, 0.1);
}

/* Optional: Add these styles for better text readability */
.section-content {
  color: rgba(255, 255, 255, 0.9);
}
</style>
