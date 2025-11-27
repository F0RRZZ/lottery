<script setup>
import { onMounted, ref, defineProps } from "vue";

const space = ref("&nbsp;");

const props = defineProps({
    user_info: Object
})

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
        <span>{{ props.user_info.surname }} {{ space.value }}</span
        ><span>{{ props.user_info.name }} {{ space.value }}</span
        ><span>{{ props.user_info.patronymic }}</span>
      </p>
      <p class="info-row-p">{{ text_info_name.id }} : №{{ props.user_info.id }}</p>
      <p class="info-row-p">
        {{ text_info_name.email }} : {{ props.user_info.email }}
      </p>
      <p class="info-row-p">
        {{ text_info_name.username }} : {{ props.user_info.username }}
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
