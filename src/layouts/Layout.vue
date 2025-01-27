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
    class="md:hidden flex items-center justify-around h-16 fixed top-0 w-full z-50 rounded-t-md bg-bgSecondary border-b-2 shadow-md border-primaryColor text-sm"
  >
    <NavLink to="#about">About</NavLink>
    <NavLink to="#education">Education</NavLink>
    <NavLink to="#portfolio">Portfolio</NavLink>
    <a
      href="#contact"
      class="w-24 md:w-auto px-4 py-2 text-center bg-primaryColor rounded-md text-white md:rounded"
    >
      Hire me
    </a>
  </nav>
  <div class="px-4 max-w-[1380px] mx-auto mt-16 lg:mt-0">
    <slot />
  </div>
</template>
