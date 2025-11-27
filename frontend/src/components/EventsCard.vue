<script setup>
import { ref, defineProps } from "vue";

defineProps({
  title: String,
  lotteries: Array,
});
</script>

<template>
  <div class="main-div">
    <p class="p-title">{{ title }}</p>

    <div class="carousel-div">
      <div class="group-of-carousel">
        <router-link
          v-for="item in lotteries"
          :key="item.id"
          :to="`/lottery/${item.id}`"
        >
          <img :src="item.image" :alt="'Розыгрыш №' + item.id" />
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-div {
  margin: 65px 0px 65px 0px;
}

.p-title {
  font-size: 2em;
  font-weight: bold;
  margin-left: 20px;
}

.carousel-div {
  display: flex;
  justify-content: center;
  gap: 1em;
}

.group-of-carousel {
  display: flex;
  width: 100%;
  gap: 2em;
  overflow-x: auto;
  padding: 30px;
}

.group-of-carousel img {
  width: 450px;
  border-radius: 40px;
  box-shadow: 0px 0px 25px grey;
  transition: border-radius 0.3s ease;
  cursor: pointer;
}

@media (max-width: 1025px) {
  .group-of-carousel img {
    width: 365px;
    border-radius: 34px;
  }
}

@media (max-width: 700px) {
  .p-title {
    font-size: 1.6em;
  }

  .group-of-carousel img {
    width: 280px;
    border-radius: 27px;
  }
}

@media (max-width: 450px) {
  .p-title {
    font-size: 1.45em;
  }

  .group-of-carousel img {
    width: 195px;
    border-radius: 20px;
  }
}
</style>
