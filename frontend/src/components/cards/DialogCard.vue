<template>
  <v-dialog v-model="dialog" max-width="600">
    <slot :dialog="dialog">
      <v-card>
        <!-- Dialog 재사용을 위해 slot 영역을 지정 -->
        <!-- 임시 Form. 원하는 Form 컴포넌트를 만들어 slot으로 삽입하면 바뀜-->
        <div class="box">
          <h3>폼 컴포넌트를 작성해서 삽입</h3>
        </div>
      </v-card>
    </slot>
  </v-dialog>
</template>
<script>
export default {
  data: () => ({
    dialog: false,
  }),
  methods: {
    closeDialog: function () {
      this.dialog = false;
    },
    showDialog: function () {
      this.dialog = true;
    },
  },
};
</script>

<style scoped>
.box {
  width: 500px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>