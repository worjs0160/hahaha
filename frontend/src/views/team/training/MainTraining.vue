<template>
  <component
    :is="isSelectedComponent" @child="setComponent"
    @coverSetChild="loadingCover"
  >
  </component>
</template>

<script>
import UserList from "/src/views/team/training/UserList";
import TrainingRecord from "/src/views/team/training/TrainingRecord";

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
    // MainLayout으로 로딩상태 보내기
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>

<style></style>
