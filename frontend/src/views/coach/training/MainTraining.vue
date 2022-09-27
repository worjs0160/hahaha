<template>
  <component
    :is="isSelectedComponent" @child="setComponent"
    @coverSetChild="loadingCover"
  >
  </component>
</template>

<script>
import UserList from "/src/views/coach/training/UserList";
import TrainingRecord from "/src/views/coach/training/TrainingRecord";

export default {
  data: () => ({
    isSelectedComponent: "UserList",
  }),
  components: {
    UserList,
    TrainingRecord,
  },
  methods: {
    setComponent: function(component) {
      this.isSelectedComponent = component;
    },
    //MainLayout으로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>

<style></style>
