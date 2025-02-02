<template>
  <form @submit.prevent="submitForm">
    <input v-model="name" type="text" placeholder="Your Name" required />
    <input v-model="email" type="email" placeholder="Your Email" required />
    <input v-model="phone" type="tel" placeholder="Your Phone" />
    <textarea v-model="message" placeholder="Your Message" required></textarea>
    <button type="submit">Submit</button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const name = ref("");
const email = ref("");
const phone = ref("");
const message = ref("");

const submitForm = async () => {
  try {
    const response = await axios.post("http://127.0.0.1:5000/contact", {
      name: name.value,
      email: email.value,
      phone: phone.value,
      message: message.value,
    });

    console.log("Success:", response.data);
    // Clear form fields
    name.value = "";
    email.value = "";
    phone.value = "";
    message.value = "";
    alert("Message sent successfully!");
  } catch (error) {
    console.error("Error:", error.response?.data || error.message);
    alert("Failed to send message. Please try again.");
  }
};
</script>
