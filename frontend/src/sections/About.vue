<script setup></script>
<template>
  <!-- Hero Section Start -->
  <section
    id="about"
    class="container mx-auto flex md:flex-row flex-col items-center pt-8 lg:pt-0 mb-8 scroll-m-16 lg:scroll-m-0"
  >
    <div class="lg:w-1/3 md:order-1 lg:order-2 relative">
      <!-- Gradient background elements -->
      <div class="absolute inset-0 z-0 animate-hue-rotate">
        <div
          class="absolute top-1/2 left-1/2 w-[110%] h-[110%] -translate-x-1/2 -translate-y-1/2 bg-[conic-gradient(var(--tw-gradient-stops))] from-primaryColor via-transparent to-primaryColor opacity-30 blur-[100px] animate-hue-pulse"
        ></div>
        <div
          class="absolute top-1/2 left-1/2 w-[120%] h-[120%] -translate-x-1/2 -translate-y-1/2 bg-[conic-gradient(var(--tw-gradient-stops))] from-transparent via-primaryColor to-transparent opacity-20 blur-[80px] animate-hue-pulse-2"
        ></div>
      </div>

      <!-- Existing image container -->
      <div
        class="flex mx-auto h-80 w-80 justify-center content-center rounded-full overflow-hidden relative z-10"
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
          class="rounded-md text-textPrimary px-4 py-2 hover:bg-primaryColor bg-primaryColor active:scale-95 hover:text-bgPrimary transition-all duration-150"
        >
          CV
        </a>
        <a
          href="https://github.com/K4naxa"
          target="_blank"
          class="rounded-md flex gap-2 bg-primaryColor active:scale-95 border border-primaryColor text-textPrimary px-4 py-2 hover:text-bgPrimary transition-all duration-150"
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
<style scoped>
@keyframes hue-rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes hue-scale {
  0%,
  100% {
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.1);
  }
}

.animate-hue-rotate {
  animation: hue-rotate 8s linear infinite;
}

.animate-hue-scale {
  animation: hue-scale 6s ease-in-out infinite;
}
@keyframes hue-pulse {
  0%,
  100% {
    transform: translate(-50%, -50%) scale(0.5);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.2);
  }
}

@keyframes hue-pulse-2 {
  0%,
  100% {
    transform: translate(-50%, -50%) scale(0.7);
  }
  50% {
    transform: translate(-50%, -50%) scale(1.15);
  }
}

.animate-hue-pulse {
  animation: hue-rotate 8s linear infinite, hue-pulse 6s ease-in-out infinite;
}

.animate-hue-pulse-2 {
  animation: hue-rotate 8s linear infinite, hue-pulse-2 5s ease-in-out infinite;
}
</style>
