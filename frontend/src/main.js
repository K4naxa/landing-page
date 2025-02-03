import { createApp } from "vue";
import "./index.css";
import App from "./App.vue";
import { VueReCaptcha } from "vue-recaptcha-v3";
import Vue3Toastify from "vue3-toastify";
import "vue3-toastify/dist/index.css";

const app = createApp(App);

app.use(VueReCaptcha, {
  siteKey: "6LctMcsqAAAAAFuJZvz47zyhes5uSQkdnZviMJaO",
  loaderOptions: {
    autoHideBadge: true,
    explicitRenderParameters: {
      badge: "bottomright",
    },
  },
});

app.use(Vue3Toastify, {
  autoClose: 3000,
  position: "top-right",
  pauseOnHover: true,

  // You can pass your own options to the plugin

  theme: "dark",
});

app.mount("#app");
