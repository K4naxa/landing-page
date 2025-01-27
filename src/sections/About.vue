<script setup></script>
<template>
  <!-- Hero Section Start -->
  <section
    id="about"
    class="container mx-auto flex md:flex-row flex-col items-center pt-8 lg:pt-0 mb-8 scroll-m-16 lg:scroll-m-0"
  >
    <div class="lg:w-1/3 md:order-1 lg:order-2">
      <div
        class="flex mx-auto h-80 w-80 shadow-lg shadow-primaryColor justify-center content-center rounded-full overflow-hidden"
      >
        <img
          class="object-center object-cover h-full w-full"
          alt="hero"
          src="../assets/Hero.jpg"
        />
      </div>
    </div>
    <div
      class="lg:flex-grow md:w-1/2 flex flex-col md:items-start md:text-left mb-16 md:pt-10 pt-8 items-center text-center"
    >
      <h1
        class="title-font sm:text-6xl leading-6 text-3xl mb-4 font-bold text-white"
      >
        Hi, I'm <span class="text-primaryColor">Jami</span>
      </h1>
      <h3 class="title-font sm:text-3xl text-xl mb-4 font-bold text-white">
        Fullstack Web Developer
      </h3>
      <p class="mb-2 leading-relaxed text-slate-200">
        Motivated and passionate Full-Stack Developer with a strong enthusiasm
        for coding and problem-solving. I excel in tacklig challenges, learning
        new skills, and pushing my abilities with exciting projects
      </p>

      <p class="mb-8 leading-relaxed text-slate-200">
        Looking for opportunities to work with a team of developers to improve
        my skills and learn from others.
      </p>

      <div class="flex gap-4 flex-wrap">
        <a
          href="/src/assets/cv.pdf"
          target="_blank"
          class="rounded-md border border-primaryColor text-textPrimary px-4 py-2 hover:bg-primaryColor hover:text-bgPrimary transition-colors duration-150"
        >
          CV
        </a>
        <a
          href="https://github.com/K4naxa"
          target="_blank"
          class="rounded-md flex gap-2 border border-primaryColor text-textPrimary px-4 py-2 hover:bg-primaryColor hover:text-bgPrimary transition-colors duration-150"
        >
          <img
            src="/src/assets/github-mark-white.png"
            alt="github logo"
            class="h-6 w-6"
          />
          Github
        </a>
      </div>
    </div>
  </section>
</template>
