<script setup>
import { ref } from "vue";
import axios from "axios";
import { VueReCaptcha, useReCaptcha } from "vue-recaptcha-v3";

const { executeRecaptcha, recaptchaLoaded } = useReCaptcha();
const recaptcha = async () => {
  await recaptchaLoaded();
  return await executeRecaptcha("contact"); // Create a reCAPTCHA token with the action name "contact"
};

import { toast } from "vue3-toastify";

const fireToast = (message, type) => {
  toast(message, {
    type: type,
    autoClose: 3000,
  });
};

const formLoading = ref(false);
const formData = ref({
  name: "",
  email: "",
  subject: "", // Correct property name
  message: "",
});

const submitForm = async () => {
  formLoading.value = true;

  // Validate form fields
  if (!formData.value.name || !formData.value.email || !formData.value.message) {
    fireToast("Please fill out all required fields.", "error");
    formLoading.value = false;
    return;
  }

  // reCAPTCHA create token
  const token = await recaptcha();

  if (!token) {
    fireToast("Invalid reCAPTCHA. Please try again.", "error");
    formLoading.value = false;
    return; // Exit if the token is invalid
  } else {
    console.log("reCAPTCHA token created successfully");
  }

  try {
    // Send the message to the backend with the reCAPTCHA token
    const response = await axios.post("/api/contact", {
      name: formData.value.name,
      email: formData.value.email,
      subject: formData.value.subject,
      message: formData.value.message,
      recaptcha_token: token,
    });

    console.log("Success:", response.data.message);

    // Clear form fields
    formData.value = {
      name: "",
      email: "",
      subject: "",
      message: "",
    };

    fireToast("Message sent successfully!", "success");
    formLoading.value = false;
  } catch (error) {
    console.error("Error:", error.response?.data || error.message);
    formLoading.value = false;
    fireToast("Failed to send message. Please try again.", "error");
  }
};
</script>
<template>
  <div class="text-textPrimary lg:rounded-lg">
    <div class="grid sm:grid-cols-2 items-start gap-12 lg:gap-16 mx-auto w-full bg-bgSecondary rounded-lg">
      <div class="flex flex-col gap-4">
        <div class="relative mb-4">
          <h2 class="flex items-center text-primaryColor">
            contact
            <p class="ml-3 text-textPrimary">me</p>
          </h2>
          <div class="h-1 w-12 underline bg-primaryColor" />
        </div>
        <div>
          <p class="text-textGray mt-2">
            Interested on hiring me for a project or want to work together on something? <br />
            Feel free to reach out to me!
          </p>
        </div>

        <h1 class="text-2xl font-extrabold mt-8">Socials</h1>

        <div class="flex flex-wrap gap-6">
          <a
            href="https://www.linkedin.com/in/jami-hyvärinen-1aa237295"
            target="_blank"
            class="rounded-md text-textPrimary px-4 py-2 active:scale-95 button-effects"
            >Linkedin</a
          >
        </div>
      </div>

      <form @submit.prevent="submitForm()" class="ml-auto space-y-4 max-w-lg mx-auto rounded-lg">
        <input
          required
          v-model="formData.name"
          type="text"
          placeholder="Name"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm focus:outline-none border border-bgPrimary focus:border-primaryColor glass-effect"
        />
        <input
          required
          v-model="formData.email"
          type="email"
          placeholder="Email"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm focus:outline-none border border-bgPrimary focus:border-primaryColor glass-effect"
        />
        <input
          v-model="formData.subject"
          type="text"
          placeholder="Subject"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm focus:outline-none border border-bgPrimary focus:border-primaryColor glass-effect"
        />
        <textarea
          required
          v-model="formData.message"
          placeholder="Message"
          rows="6"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm focus:outline-none border border-bgPrimary focus:border-primaryColor glass-effect"
        ></textarea>
        <button
          type="submit"
          :disabled="formLoading"
          class="text-white hover:text-bgPrimary border duration-150 border-primaryColor tracking-wide rounded-md text-sm px-4 py-3 w-full mt-6"
          :class="formLoading ? 'bg-bgPrimary/50 cursor-not-allowed' : 'bg-primaryColor active:scale-95 '"
        >
          <p v-if="!formLoading">Send</p>
          <div v-else role="status">
            <svg
              aria-hidden="true"
              class="w-8 h-8 text-transparent animate-spin fill-primaryColor mx-auto"
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
        </button>
      </form>
    </div>
  </div>
</template>
