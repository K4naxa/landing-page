<script setup></script>
<template>
  <nav
    class="flex flex-wrap items-center justify-between p-5 bg-secondary-500 static top-0 w-full z-50"
  >
    <a class="flex title-font font-medium items-center text-white mb-4 md:mb-0">
      <span class="ml-3 text-xl">My Resume</span>
    </a>

    <div
      :class="[
        'w-full md:w-auto md:flex text-right text-bold mt-5 md:mt-0 border-t-2 border-primary-500 md:border-none',
      ]"
    >
      <a
        href="#about"
        class="block md:inline-block text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
      >
        About
      </a>
      <a
        href="#education"
        class="block md:inline-block text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
      >
        Education
      </a>
      <a
        href="#portfolio"
        class="block md:inline-block text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
      >
        Portfolio
      </a>
      <a
        href="#achievements"
        class="block md:inline-block text-slate-200 hover:text-primary-500 px-3 py-3 uppercase"
      >
        Achievements
      </a>
    </div>
    <a
      href="#contact"
      class="toggle hidden md:flex w-full md:w-auto px-4 py-2 text-right bg-primary-500 hover:bg-secondary-600 hover:text-primary-500 text-white md:rounded"
    >
      Hire me
    </a>
  </nav>
</template>
