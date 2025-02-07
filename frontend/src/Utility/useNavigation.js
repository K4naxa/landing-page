import { ref } from "vue";

export function useNavigation() {
  const sections = ref([]);
  const activeSection = ref(null);

  const initializeSections = () => {
    sections.value = Array.from(document.querySelectorAll("section")).map(
      (section) => ({
        id: section.id,
        height: section.offsetHeight,
        name: section.id.charAt(0).toUpperCase() + section.id.slice(1),
      })
    );
    activeSection.value = sections.value[0]?.id;
  };

  const scrollToSection = (sectionId) => {
    const section = document.getElementById(sectionId);
    if (!section) return;

    section.scrollIntoView({ behavior: "smooth" });
    activeSection.value = sectionId;
  };

  return {
    sections,
    activeSection,
    initializeSections,
    scrollToSection,
  };
}
