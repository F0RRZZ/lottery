<script setup>
import { ref } from "vue";

const space = ref("&nbsp;");

const text_info = ref({
  email: "user@example.com",
  username: "iCHCaX-HVhTn961tqvq-JifMsVxGjPXgx8Q41cIWQe8sIy",
  name: "Глеб",
  surname: "Конников",
  patronymic: "Владимирович",
  id: 0,
  is_active: true,
  created_at: "2025-11-03T14:14:25.388Z",
  updated_at: "2025-11-03T14:14:25.388Z",
});

const text_info_name = ref({
  email: "Электропочта",
  username: "Логин",
  name: "Имя",
  surname: "Фамилия",
  patronymic: "Отчество",
  id: "Номер пользователя",
});
</script>

<template>
  <div class="info-div">
    <img class="user-img" src="/user-profile-page/user-image.png" alt="" />
    <div class="text-info-div">
      <p class="initials-p">
        <span>{{ text_info.surname }} {{ space.value }}</span
        ><span>{{ text_info.name }} {{ space.value }}</span
        ><span>{{ text_info.patronymic }}</span>
      </p>
      <p class="info-row-p">{{ text_info_name.id }} : №{{ text_info.id }}</p>
      <p class="info-row-p">
        {{ text_info_name.email }} : {{ text_info.email }}
      </p>
      <p class="info-row-p">
        {{ text_info_name.username }} : {{ text_info.username }}
      </p>
    </div>
  </div>
</template>

<style scoped>
.info-div {
  display: flex;
  align-items: center;
  padding: 20px;
}

.user-img {
  width: 150px;
  flex: 0 0 auto;
  height: 150px;
}

.text-info-div {
  display: flex;
  flex-direction: column;
  margin-left: 30px;
  font-family: "Inter", sans-serif;
}

.initials-p {
  font-size: 1.6em;
  font-weight: bold;
  margin-bottom: 10px;
}

.info-row-p {
  font-size: 1.1em;
  margin-bottom: 5px;
}

@media (max-width: 500px) {
  .initials-p {
    font-size: 1.4em;
  }

  .user-img {
    width: 100px;
    height: 100px;
  }

  .info-row-p {
    font-size: 0.95em;
  }
}

@media (max-width: 400px) {
  .user-img {
    width: 100px;
    height: 100px;
  }

  .info-row-p {
    font-size: 0.75em;
  }

  .user-img {
    width: 70px;
    height: 70px;
  }
}
</style>
