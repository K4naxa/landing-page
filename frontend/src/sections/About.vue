<script setup>
import { useReCaptcha } from "vue-recaptcha-v3";
import { ref } from "vue";
import axios from "axios";

import { toast } from "vue3-toastify";

const fireToast = (message, type) => {
  toast(message, {
    type: type,
    autoClose: 3000,
  });
};

const { executeRecaptcha, recaptchaLoaded } = useReCaptcha();

const cvLoading = ref(false);
const downloadCV = async () => {
  cvLoading.value = true;
  await recaptchaLoaded(); // Ensure reCAPTCHA is ready
  const token = await executeRecaptcha("cv_download");

  if (!token) {
    alert("reCAPTCHA failed. Please try again.");
    cvLoading.value = false;
    return;
  } else {
    console.log("reCAPTCHA token created successfully");
  }

  try {
    const response = await axios.post(
      "/api/cv",
      { recaptcha_token: token },
      { responseType: "blob" } // Get binary data
    );

    console.log("Success: CV downloaded");

    // Create a URL object from the blob data
    const fileURL = window.URL.createObjectURL(
      new Blob([response.data], { type: "application/pdf" })
    );

    // Open the PDF in a new tab
    window.open(fileURL, "_blank");
    cvLoading.value = false;
  } catch (error) {
    fireToast("Failed to download CV. Please try again.", "error");
    cvLoading.value = false;
  }
};
</script>
<template>
  <!-- Hero Section Start -->
  <div
    class="container flex w-full justify-center lg:flex-row flex-col items-center"
  >
    <div class="lg:w-1/3 lg:order-2 relative">
      <!-- Existing image container -->
      <div
        class="flex mx-auto aspect-square w-3/4 max-w-96 lg:w-80 justify-center rounded-full overflow-hidden relative z-10 mb-8 lg:mb-0"
      >
        <img
          class="object-cover h-full w-full inset-shadow-sm inset-shadow-primaryColor/50"
          style="object-position: center -100px"
          alt="hero"
          src="../assets/Hero.jpg"
        />
      </div>
    </div>
    <div
      class="lg:flex-grow lg:w-1/2 flex flex-col lg:text-left text-center content-center"
    >
      <h1
        class="title-font sm:text-6xl leading-6 text-3xl mb-4 font-bold text-white"
      >
        Hi, I'm <span class="text-primaryColor">Jami</span>
      </h1>
      <h3 class="title-font sm:text-3xl text-xl mb-4 font-bold text-white">
        Fullstack Web Developer
      </h3>
      <p class="mb-8 leading-relaxed text-slate-200">
        Passionate Full-Stack Developer driven by a love for creating engaging
        user experiences and solving complex problems. I excel in tackling
        technical challenges with enthusiasm and creativity.
      </p>

      <p class="mb-8 leading-relaxed text-slate-200">
        My strong coding skills are matched by my eagerness to learn and grow.
        I'm motivated by innovative projects that stretch my abilities and allow
        me to contribute meaningfully to impactful solutions.
      </p>
      <p class="mb-8 leading-relaxed text-slate-200">
        Looking for opportunities to collaborate with talented teams where I can
        both share my expertise and learn from others, ultimately improving my
        skills while creating exceptional digital experiences.
      </p>

      <div class="flex gap-4 flex-wrap w-full justify-center lg:justify-start">
        <button
          :disabled="cvLoading"
          @click="downloadCV"
          class="rounded-md select-none cursor-pointer text-textPrimary px-4 py-2 shadow-lg shadow-transparent button-effects"
          :class="cvLoading ? 'bg-bgPrimary cursor-not-allowed' : ''"
        >
          <p v-if="!cvLoading">CV</p>
          <div v-else role="status">
            <svg
              aria-hidden="true"
              class="w-6 h-6 text-transparent animate-spin fill-primaryColor mx-auto"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
          <p class="sr-only">link for cv download</p>
        </button>
        <a
          href="https://github.com/K4naxa"
          target="_blank"
          class="rounded-md flex gap-2 text-textPrimary px-4 py-2 button-effects"
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
  </div>
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
