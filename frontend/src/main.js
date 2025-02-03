import { createApp } from "vue";
import "./index.css";
import App from "./App.vue";
import { VueReCaptcha } from "vue-recaptcha-v3";

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

app.mount("#app");
