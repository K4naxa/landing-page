<script setup>
import { ref, onMounted, onUnmounted, defineProps, computed } from "vue";
import MobileHeader from "../components/MobileHeader.vue";
import DesktopHeader from "../components/DesktopHeader.vue";
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

  section.scrollIntoView({ behavior: "smooth", block: "start" });
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
  <div
    class="h-screen flex flex-col lg:flex-row w-full lg:justify-around overflow-x-hidden relative"
  >
    <!-- Mobile Header (visible on small screens) -->
    <MobileHeader
      v-if="isMobile"
      :sections="sections"
      :activeSection="activeSection"
      @scrollToSection="scrollToSection"
    />

    <!-- Desktop sidebar (hidden on small screens) -->
    <DesktopHeader
      v-if="!isMobile"
      :sections="sections"
      :activeSection="activeSection"
      @scrollToSection="scrollToSection"
    />

    <!-- Main Content -->
    <div
      ref="swipeTarget"
      :class="
        isMobile
          ? 'swipe-container'
          : 'overflow-x-hidden overflow-y-auto scrollbar-thin w-full'
      "
    >
      <slot />
    </div>
  </div>
</template>
<style scoped>
.swipe-container {
  display: flex;
  flex-direction: row;
  overflow-x: hidden;
  overflow-y: hidden;
  width: 100vw;
  height: 100%;
}
</style>
