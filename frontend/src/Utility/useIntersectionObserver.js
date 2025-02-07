import { onUnmounted } from "vue";

export function useIntersectionObserver(activeSection) {
  let observer = null;

  const initializeObserver = (sections) => {
    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
            activeSection.value = entry.target.id;
          }
        });
      },
      {
        threshold: [0, 0.5, 1],
        rootMargin: "0px",
      }
    );

    sections.value.forEach((section) => {
      const element = document.getElementById(section.id);
      if (element) observer.observe(element);
    });
  };

  onUnmounted(() => {
    if (observer) observer.disconnect();
  });

  return { initializeObserver };
}
