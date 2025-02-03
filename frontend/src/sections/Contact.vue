<script setup>
import { ref } from "vue";
import axios from "axios";
import { VueReCaptcha, useReCaptcha } from "vue-recaptcha-v3";
const { executeRecaptcha, recaptchaLoaded } = useReCaptcha();
const recaptcha = async () => {
  await recaptchaLoaded();
  return await executeRecaptcha("contact"); // Create a reCAPTCHA token
};

const formMessages = ref({
  success: "",
  error: "",
});

const formLoading = ref(false);
const formData = ref({
  name: "",
  email: "",
  subject: "", // Correct property name
  message: "",
});

const submitForm = async () => {
  formMessages.value.success = "";
  formMessages.value.error = "";
  formLoading.value = true;

  if (
    !formData.value.name ||
    !formData.value.email ||
    !formData.value.message
  ) {
    formMessages.value.error = "Please fill out all required fields.";
    formLoading.value = false;
    return;
  }

  // reCAPTCHA create token
  const token = await recaptcha();

  if (!token) {
    formMessages.value.error = "Invalid reCAPTCHA. Please try again.";
    formLoading.value = false;
    return; // Exit if the token is invalid
  }

  // Send the message
  try {
    // Send the token to the CAPTCHA validation API first
    const captchaResponse = await fetch("http://127.0.0.1:5000/api/captcha", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ recaptcha_token: token }),
      credentials: "include", // Add this
    });

    // If the CAPTCHA validation is successful (status 200), submit the form
    if (captchaResponse.ok) {
      console.log("reCAPTCHA validation response is ok");

      const response = await axios.post("http://127.0.0.1:5000/api/contact", {
        name: formData.value.name,
        email: formData.value.email,
        subject: formData.value.subject,
        message: formData.value.message,
      });

      console.log("Success:", response.data.message);
      // Clear form fields
      formData.value.name = "";
      formData.value.email = "";
      formData.value.subject = "";
      formData.value.message = "";

      formMessages.value.success = "Message sent successfully!";
      formMessages.value.error = "";
      formLoading.value = false;
    } else {
      // If the CAPTCHA validation fails, show an error message
      console.error("Error:", captchaResponse.statusText);
      formMessages.value.error =
        "Failed to validate reCAPTCHA. Please try again.";
      formLoading.value = false;
    }
  } catch (error) {
    console.error("Error:", error.response?.data || error.message);
    formMessages.value.error = "Failed to send message. Please try again.";
  }
};
</script>
<template>
  <section
    id="contact"
    class="py-8 mx-auto text-textPrimary scroll-m-16 lg:scroll-m-0"
  >
    <div class="mb-8">
      <h2 class="flex items-center text-primaryColor">
        contact
        <p class="ml-3 text-textPrimary">me</p>
      </h2>
      <div class="h-1 w-12 underline bg-primaryColor" />
    </div>
    <div
      class="grid sm:grid-cols-2 items-start gap-16 mx-auto max-w-5xl bg-bgSecondary rounded-lg shadow-lg p-8"
    >
      <div class="flex flex-col gap-4">
        <h1 class="text-3xl font-extrabold">Let's Talk</h1>
        <p class="text-textGray mt-4">
          Interested on hiring me for a project or want to work together on
          something? Feel free to reach out to me!
        </p>

        <h1 class="text-3xl font-extrabold mt-8">Socials</h1>

        <div class="flex flex-wrap gap-6">
          <div class="py-2 px-4 w-fit rounded-md bg-bgPrimary">Linkedin</div>
          <div class="py-2 px-4 w-fit rounded-md bg-bgPrimary">Email</div>
          <div class="py-2 px-4 w-fit rounded-md bg-bgPrimary">Github</div>
          <div class="py-2 px-4 w-fit rounded-md bg-bgPrimary">Phone</div>
        </div>
      </div>

      <form @submit.prevent="submitForm()" class="ml-auto space-y-4">
        <input
          required
          v-model="formData.name"
          type="text"
          placeholder="Name"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm"
        />
        <input
          required
          v-model="formData.email"
          type="email"
          placeholder="Email"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm"
        />
        <input
          v-model="formData.subject"
          type="text"
          placeholder="Subject"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm"
        />
        <textarea
          required
          v-model="formData.message"
          placeholder="Message"
          rows="6"
          class="w-full rounded-md py-3 px-4 bg-bgPrimary text-sm"
        ></textarea>
        <button
          type="submit"
          class="text-white bg-primaryColor hover:text-bgPrimary active:scale-95 duration-150 tracking-wide rounded-md text-sm px-4 py-3 w-full !mt-6"
        >
          Send
        </button>
      </form>
    </div>
  </section>
</template>
