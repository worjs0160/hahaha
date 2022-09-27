<template>
  <div>기업 관리 휴가설정 화면입니다.</div>
</template>

<script>
export default {
  async created() {
    await this.loadingCover(true);
    await this.loadingCover(false);
  },
  methods:{
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  }
};
</script>

<style></style>