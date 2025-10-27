import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";

import MainPage from "./views/MainPage.vue";
import RegisterPage from "./views/RegisterPage.vue";
import LoginPage from "./views/LoginPage.vue";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

createApp(App).use(router).mount("#app");
