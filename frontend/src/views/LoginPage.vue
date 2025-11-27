<script setup>
import { ref, reactive, defineEmits } from "vue";
import { useRouter } from "vue-router";

const showPassword = ref(false);
const showError = ref(false);
const loginURL = "http://localhost:8000/api/auth/token";
const router = useRouter();

const submitBody = reactive({
  username: "",
  password: "",
});

const onSubmit = async () => {
  showError.value = false;
  try {
    const response = await fetch(loginURL, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: `username=${submitBody.username}&password=${submitBody.password}`,
    });

    if (!response.ok) {
      const errData = await response.json();
      console.log("Ошибка сервера:", errData);
      showError.value = true;
      showRegisterMessage.value = true;
      return;
    }

    const data = await response.json();

    localStorage.setItem("access_token", data.access_token);
    localStorage.setItem("refresh_token", data.refresh_token);

    goToMainPage();
  } catch (err) {
    showError.value = true;
  }
};

const goToMainPage = () => {
  router.push("/");
};
</script>

<template>
  <div class="main-div">
    <router-link class="header-logo" to="/">лотерея</router-link>
    <div class="form-div">
      <p class="header-p-form">Вход в аккаунт</p>

      <form id="registerForm" @submit.prevent="onSubmit">
        <div class="inputs-div">
          <input
            v-model="submitBody.username"
            type="text"
            required
            placeholder="Имя пользователя"
          />
          <div class="password-div">
            <input
              v-model="submitBody.password"
              :type="showPassword ? 'text' : 'password'"
              minlength="8"
              required
              placeholder="Пароль"
            />
            <div class="checkbox-div">
              <span>Показать пароль</span>
              <input type="checkbox" v-model="showPassword" />
            </div>
            <p
              v-if="showError"
              class="error-p"
              v-text="'Ошибка входа! Попробуйте ещё раз.'"
            ></p>
          </div>
        </div>
      </form>
      <div class="button-div">
        <button form="registerForm">Войти</button>
        <p class="register-p">
          <span>Ещё нет аккаунта? </span>
          <router-link
            style="cursor: pointer; text-decoration: none"
            to="/register"
            >Зарегистрироваться.</router-link
          >
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-div {
  display: flex;
  height: 100vh;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-image: url("/register-page/background-image-register-page.png");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
}

.header-logo {
  cursor: pointer;
  text-decoration: none;
  color: black;
}

.header-p-form,
.header-logo {
  font-size: 2em;
  font-weight: bold;
}

.form-div {
  display: flex;
  flex: 1;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 2em;
}

.inputs-div {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
}

input {
  width: 400px;
  padding-left: 10px;
  border: 2px solid grey;
}

input:focus,
input:active {
  outline: none;
  border: 2px solid #b25dfd;
}

input[type="checkbox"] {
  width: 17px;
  cursor: pointer;
}

.password-div {
  display: flex;
  flex-direction: column;
}

.checkbox-div {
  display: flex;
  align-items: center;
  gap: 0.4em;
  padding-left: 5px;
}

.error-p {
  color: red;
  padding-left: 5px;
  font-weight: bold;
}

button {
  width: 200px;
  color: white;
  background-color: #b25dfd;
  border: none;
  font-weight: bold;
  cursor: pointer;
  margin-bottom: 20px;
}

.button-div {
  display: flex;
  flex-direction: column;
  align-items: center;
}

input,
button {
  height: 40px;
  border-radius: 10px;
  font-size: 1em;
}

@media (max-width: 450px) {
  input {
    width: 300px;
  }

  .register-p {
    text-align: center;
  }
}
</style>
