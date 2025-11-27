<script setup>
import { ref, reactive, defineEmits } from "vue";

const showPassword = ref(false);
const showError = ref(false);
const showRegisterMessage = ref(false);
const registerURL = "http://localhost:8000/api/auth/register";

const submitBody = reactive({
  email: "",
  username: "",
  name: "",
  surname: "",
  patronymic: "",
  password: "",
});

const emptyBody = {
  email: "",
  username: "",
  name: "",
  surname: "",
  patronymic: "",
  password: "",
};

const onSubmit = async () => {
  showRegisterMessage.value = false;
  showError.value = false;
  try {
    const response = await fetch(registerURL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(submitBody),
    });

    if (!response.ok) {
      const errData = await response.json();
      console.log("Ошибка сервера:", errData);
      showError.value = true;
      showRegisterMessage.value = true;
      return;
    }
    
    const data = await response.json();

    Object.assign(submitBody, emptyBody);
  } catch (err) {
    showError.value = true;
  }
  showRegisterMessage.value = true;
};
</script>

<template>
  <div class="main-div">
    <router-link class="header-logo" to="/">лотерея</router-link>
    <div class="form-div">
      <p class="header-p-form">Регистрация</p>

      <form id="registerForm" @submit.prevent="onSubmit">
        <div class="inputs-div">
          <input
            v-model="submitBody.email"
            type="email"
            required
            placeholder="Почта"
          />
          <input
            v-model="submitBody.username"
            type="text"
            required
            placeholder="Имя пользователя"
          />
          <input
            v-model="submitBody.name"
            type="text"
            required
            placeholder="Имя"
          />
          <input
            v-model="submitBody.surname"
            type="text"
            required
            placeholder="Фамилия"
          />
          <input
            v-model="submitBody.patronymic"
            type="text"
            required
            placeholder="Отчество"
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
              v-if="showRegisterMessage"
              :class="showError ? 'error-p' : 'success-p'"
              v-text="
                showError
                  ? 'Ошибка регистрации! Попробуйте ещё раз.'
                  : 'Регистрация успешна! Выполните вход.'
              "
            ></p>
          </div>
        </div>
      </form>
      <div>
        <button form="registerForm">Зарегистрироваться</button>
        <p>
          <span>Уже есть аккаунт? </span>
          <router-link
            style="cursor: pointer; text-decoration: none"
            to="/login"
            >Войти.</router-link
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
}

.succes-p {
  color: rgb(0, 255, 26);
}

.error-p,
.succes-p {
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
}
</style>
