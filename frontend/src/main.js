import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
import { createRouter, createWebHistory } from "vue-router";

import MainPage from "./views/MainPage.vue";
import RegisterPage from "./views/RegisterPage.vue";
import LoginPage from "./views/LoginPage.vue";
import UserProfilePage from "./views/UserProfilePage.vue";
import LotteryPage from "./views/LotteryPage.vue";

const routes = [
  {
    path: "/",
    name: "MainPage",
    component: MainPage,
  },
  {
    path: "/register",
    name: "RegisterPage",
    component: RegisterPage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/user-profile",
    name: "UserProfilePage",
    component: UserProfilePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/lottery/:id",
    name: "LotteryPage",
    component: LotteryPage,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const access_token = localStorage.getItem("access_token");
  const refresh_token = localStorage.getItem("refresh_token");

  try {
    if (access_token != null && refresh_token != null) {
      let response = await fetch("http://localhost:8000/api/auth/me", {
        method: "GET",
        headers: {
          Authorization: `Bearer ${access_token}`,
        },
      });

      if (!response.ok) {
        response = await fetch("http://localhost:8000/api/auth/refresh", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({refresh_token}),
        });

        if (response.ok) {
          const data = await response.json();
          localStorage.setItem("access_token", data.access_token);
          localStorage.setItem("refresh_token", data.refresh_token);
          return next();
        } else {
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
        }
      } else {
        return next();
      }
    }
  } catch (err) {
    console.log(err);
  }

  if (to.meta.requiresAuth) {
    alert("Вам нужно войти в аккаунт для просмотра этого!")
    return next("/login");
  }

  return next();
});

createApp(App).use(router).mount("#app");
