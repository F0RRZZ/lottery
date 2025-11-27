<script setup>
import { ref } from "vue";

const props = defineProps({
  lotteries: Array,
});

const curBigDrawIndex = ref(0);
const nameOfImgTransition = ref("");

const nextLeftDraw = () => {
  nameOfImgTransition.value = "change-draw-left";
  curBigDrawIndex.value =
    (curBigDrawIndex.value - 1 + props.lotteries.length) %
    props.lotteries.length;
};

const nextRightDraw = () => {
  nameOfImgTransition.value = "change-draw-right";
  curBigDrawIndex.value = (curBigDrawIndex.value + 1) % props.lotteries.length;
};
</script>

<template>
  <div class="carousel-div">
    <img
      @click="nextLeftDraw"
      class="img-arrow img-arrow-left"
      src="/main-page/left-arrow.svg"
      alt="left-arrow"
    />

    <div class="gallery">
      <div class="gallery-group-imgs">
        <router-link :to="`/lottery/${lotteries[curBigDrawIndex].id}`">
          <transition :name="nameOfImgTransition" mode="out-in">
            <img
              :key="curBigDrawIndex"
              :src="`http://localhost:1337${lotteries[curBigDrawIndex].preview_big}`"
              alt="big-draw-image"
            />
          </transition>
        </router-link>
      </div>
    </div>

    <img
      @click="nextRightDraw"
      class="img-arrow img-arrow-right"
      src="/main-page/right-arrow.svg"
      alt="right-arrow"
    />
  </div>
</template>

<style scoped>
.carousel-div {
  display: flex;
  justify-content: space-between;
  margin: 65px 20px 65px 20px;
}

.img-arrow {
  width: 70px;
  cursor: pointer;
}

.img-arrow-left {
  margin-right: 30px;
}

.img-arrow-right {
  margin-left: 30px;
}

.gallery {
  display: flex;
  overflow-x: auto;
  border-radius: 40px;
  box-shadow: 0px 0px 25px grey;
  transition: border-radius 0.3s ease;
}

.gallery::-webkit-scrollbar {
  display: none;
}

.gallery-group-imgs {
  display: flex;
}

.gallery img {
  width: 100%;
  cursor: pointer;
  will-change: transform, opacity;
}

@media (max-width: 1025px) {
  .gallery {
    border-radius: 30px;
  }

  .carousel-div {
    margin-right: 10px;
    margin-left: 10px;
  }

  .img-arrow {
    width: 40px;
    cursor: pointer;
  }

  .img-arrow-left {
    margin-right: 5px;
  }

  .img-arrow-right {
    margin-left: 5px;
  }
}

@media (max-width: 700px) {
  .gallery {
    border-radius: 20px;
  }

  .carousel-div {
    margin-right: 5px;
    margin-left: 5px;
  }

  .img-arrow {
    width: 25px;
    cursor: pointer;
  }
}

@media (max-width: 450px) {
  .gallery {
    border-radius: 15px;
  }

  .img-arrow {
    width: 15px;
    cursor: pointer;
  }

  .img-arrow-left {
    margin-right: 0px;
  }

  .img-arrow-right {
    margin-left: 0px;
  }
}
</style>

<style scoped>
.change-draw-left-enter-active,
.change-draw-left-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.change-draw-left-enter-from {
  opacity: 0;
  transform: translateX(-100%);
}

.change-draw-left-enter-to {
  opacity: 1;
  transform: translateX(0);
}

.change-draw-left-leave-from {
  opacity: 1;
  transform: translateX(0);
}

.change-draw-left-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
</style>

<style scoped>
.change-draw-right-enter-active,
.change-draw-right-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}

.change-draw-right-enter-from {
  opacity: 0;
  transform: translateX(100%);
}

.change-draw-right-enter-to {
  opacity: 1;
  transform: translateX(0);
}

.change-draw-right-leave-from {
  opacity: 1;
  transform: translateX(0);
}

.change-draw-right-leave-to {
  opacity: 0;
  transform: translateX(-100%);
}
</style>
