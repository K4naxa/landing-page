<script setup>
import { ref, onMounted, onUnmounted, defineProps, computed } from "vue";
import { useSwipe } from "@vueuse/core";

const props = defineProps({
  isMobile: Boolean,
});

const sections = ref([]);
const activeSection = ref(null);
const isHeaderVisible = ref(true);
const isMobile = computed(() => props.isMobile);
let observer = null;

const swipeTarget = ref(null);
const { direction, lengthX } = useSwipe(swipeTarget, {
  threshold: 50, // minimum distance for a swipe
  onSwipeEnd(e) {
    if (!isMobile.value) return;

    const currentIndex = sections.value.findIndex(
      (section) => section.id === activeSection.value
    );

    if (direction.value === "right" && currentIndex > 0) {
      // Swipe right - previous section
      scrollToSection(sections.value[currentIndex - 1].id);
    } else if (
      direction.value === "left" &&
      currentIndex < sections.value.length - 1
    ) {
      // Swipe left - next section
      scrollToSection(sections.value[currentIndex + 1].id);
    }
  },
});

// Smooth scroll to section when clicking navigation
const scrollToSection = (sectionId) => {
  const section = document.getElementById(sectionId);
  if (!section) return;

  section.scrollIntoView({ behavior: "smooth" });
  activeSection.value = sectionId;
};

// Mobile functionalities

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
          // entry.target.classList.add("section-visible");
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
  <div class="flex h-screen w-screen overflow-x-hidden relative">
    <!-- Mobile Header (visible on small screens) -->
    <header
      class="lg:hidden fixed top-0 left-0 right-0 z-50 transition-transform duration-300"
      :class="[
        isHeaderVisible ? 'translate-y-0' : '-translate-y-full',
        'bg-backgroundColor/95 backdrop-blur-sm',
      ]"
    >
      <!-- Mobile Navigation -->
      <nav class="transition-all duration-300 h-24 fixed w-full">
        <div class="px-4 py-2 grid grid-cols-4 gap-4 w-full">
          <button
            v-for="section in sections"
            :key="section.id"
            @click="scrollToSection(section.id)"
            :class="[
              'w-full text-textPrimary px-4 py-2 rounded transition-all text-center',
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
      <div class="flex flex-col my-auto h-fit justify-center glass-effect p-4">
        <!-- photo + name -->
        <div class="flex flex-col items-center mb-8">
          <div
            class="flex h-3/4 w-3/4 mb-4 justify-center content-center rounded-full overflow-hidden relative z-10"
          >
            <img
              class="object-center object-cover aspect-square"
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
      ref="swipeTarget"
      class="mt-24 lg:mt-0 lg:ml-80 w-full overflow-x-hidden scrollbar-thin"
    >
      <div class="flex lg:flex-col">
        <slot />
      </div>
    </div>
  </div>
</template>
<style scoped></style>
