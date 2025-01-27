<script setup>
import NavLink from "../components/NavLink.vue";
</script>
<template>
  <nav
    class="hidden md:flex flex-wrap items-center justify-between p-5 bg-secondary-500 static top-0 w-full z-50"
  >
    <a class="flex title-font font-medium items-center text-white mb-4 md:mb-0">
      <span class="ml-3 text-xl">My Resume</span>
    </a>

    <div :class="[' w-autoflex text-right text-bold mt-5']">
      <NavLink to="#about">About</NavLink>
      <NavLink to="#education">Education</NavLink>
      <NavLink to="#portfolio">Portfolio</NavLink>
      <NavLink to="#achievements">Achievements</NavLink>
    </div>

    <a
      href="#contact"
      class="w-full md:w-auto px-4 py-2 text-right bg-primaryColor hover:scale-105 hover:bg-red-800 active:scale-95 duration-75 transition-all hover:text-primary-500 text-white md:rounded"
    >
      Contact
    </a>
  </nav>

  <!-- Mobile nav menu -->
  <nav
    class="md:hidden flex items-center justify-around bg-secondary-500 h-16 fixed bottom-0 w-full z-50 rounded-t-md bg-bgSecondary border-t-2 border-primaryColor text-sm"
  >
    <a
      href="#about"
      class="text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
    >
      About
    </a>
    <a
      href="#education"
      class="text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
    >
      Education
    </a>
    <a
      href="#portfolio"
      class="text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
    >
      Portfolio
    </a>
    <a
      href="#achievements"
      class="text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
    >
      Achievements
    </a>
    <a
      href="#contact"
      class="w-24 md:w-auto px-4 py-2 text-right bg-primary-500 hover:bg-secondary-600 hover:text-primary-500 text-white md:rounded"
    >
      Hire me
    </a>
  </nav>
  <div class="mx-4">
    <slot />
  </div>
  <div class="mb-16" />
</template>
