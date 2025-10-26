<script setup>
import { ref, defineProps } from "vue";

defineProps({
  title: String,
});

const cardsDraw = ref([
  {
    id: 0,
    image: "/main-page/example-small-card-draw-1.png",
  },
    {
    id: 1,
    image: "/main-page/example-small-card-draw-2.png",
  },

]);
</script>

<template>
  <div class="main-div">
    <p class="p-title">{{ title }}</p>

    <div class="carousel-div">
      <div class="group-of-carousel">
        <img
          v-for="item in cardsDraw"
          :key="item.id"
          :src="item.image"
          :alt="'Розыгрыш №' + item.id"
        />
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
</style>
