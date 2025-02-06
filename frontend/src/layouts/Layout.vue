<script setup>
import { ref, onMounted, onUnmounted } from "vue";

const sections = ref([]);
const activeSection = ref(null);
const isHeaderVisible = ref(true);
let observer = null;

// Smooth scroll to section when clicking navigation
const scrollToSection = (sectionId) => {
  const section = document.getElementById(sectionId);
  if (!section) return;

  section.scrollIntoView({ behavior: "smooth" });
  activeSection.value = sectionId;
};

onMounted(() => {
  // Initialize sections
  sections.value = Array.from(document.querySelectorAll("section")).map(
    (section) => ({
      id: section.id,
      height: section.offsetHeight,
      name: section.id.charAt(0).toUpperCase() + section.id.slice(1),
    })
  );

  // Set initial active section
  activeSection.value = sections.value[0]?.id;

  // Initialize Intersection Observer
  observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("section-visible");
          if (entry.intersectionRatio >= 0.5) {
            activeSection.value = entry.target.id;
          }
        } else {
          entry.target.classList.remove("section-visible");
        }
      });
    },
    {
      threshold: [0, 0.5, 1],
      rootMargin: "0px",
    }
  );

  // Observe all sections
  sections.value.forEach((section) => {
    const element = document.getElementById(section.id);
    if (element) {
      observer.observe(element);
    }
  });
});

onUnmounted(() => {
  if (observer) {
    observer.disconnect();
  }
});
</script>
<template>
  <div class="flex h-screen w-screen overflow-hidden relative">
    <!-- Mobile Header (visible on small screens) -->
    <header
      class="lg:hidden fixed top-0 left-0 right-0 z-50 transition-transform duration-300"
      :class="[
        isHeaderVisible ? 'translate-y-0' : '-translate-y-full',
        'bg-backgroundColor/95 backdrop-blur-sm',
      ]"
    >
      <div class="flex items-center justify-between px-4 py-3">
        <div class="flex items-center space-x-3">
          <img
            class="h-10 w-10 rounded-full object-cover"
            src="../assets/Hero.jpg"
            alt="Profile"
          />
          <div>
            <h2 class="text-white text-sm font-bold">Jami Hyvärinen</h2>
            <p class="text-white/70 text-xs">Fullstack Web Developer</p>
          </div>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <nav class="transition-all duration-300 h-24 fixed">
        <div class="px-4 py-2 space-y-1 flex">
          <button
            v-for="section in sections"
            :key="section.id"
            @click="
              scrollToSection(section.id);
              isMobileMenuOpen = false;
            "
            :class="[
              'w-full text-left text-white px-4 py-2 rounded transition-all',
              activeSection === section.id
                ? 'bg-primaryColor'
                : 'hover:bg-primaryColor/20',
            ]"
          >
            {{ section.name }}
          </button>
        </div>
      </nav>
    </header>

    <!-- Desktop sidebar (hidden on small screens) -->
    <div class="hidden lg:flex fixed left-8 w-64 h-screen z-50">
      <!-- left side bar content -->
      <div class="flex flex-col my-auto h-fit justify-center glass-effect">
        <!-- photo + name -->
        <div class="flex flex-col items-center mb-8">
          <div
            class="flex h-52 w-52 mb-4 justify-center content-center rounded-full overflow-hidden relative z-10"
          >
            <img
              class="object-center object-cover h-full w-full blurry-image-border"
              alt="hero"
              src="../assets/Hero.jpg"
            />
          </div>
          <h2 class="text-white text-xl font-bold">Jami Hyvärinen</h2>
          <p class="text-white text-sm">Fullstack Web Developer</p>
        </div>

        <!-- Nav buttons -->
        <nav class="flex flex-col space-y-4">
          <button
            v-for="section in sections"
            :key="section.id"
            @click="scrollToSection(section.id)"
            :class="[
              'text-white px-4 py-2 rounded transition-all border border-transparent',
              activeSection === section.id
                ? 'bg-primaryColor'
                : 'hover:bg-primaryColor hover:bg-opacity-20 hover:border-primaryColor',
            ]"
          >
            {{ section.name }}
          </button>
        </nav>
      </div>
    </div>

    <!-- Main Content -->
    <div
      class="mt-24 lg:mt-0 lg:ml-80 w-full min-h-screen overflow-y-auto overflow-x-hidden scrollbar-thin"
    >
      <div class="px-4 mx-auto">
        <slot />
      </div>
    </div>
  </div>
</template>
<style scoped></style>
