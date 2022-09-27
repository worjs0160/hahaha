<template>
  <div class="inner-wrap">
    <v-text-field
      v-model="msg"
      label="보낼 메세지를 입력하세요."
      placeholder="보낼 메세지를 입력하세요."
      solo
      @keyup.13="submitMessageFunc"
    ></v-text-field>
    <v-text-field
      placeholder="방 이름"
      prepend-inner-icon="mdi-magnify"
      clearable
      clear-icon="mdi-close-thick"
      hide-details="auto"
      class="mr-2"
      v-model="roomNumber"
    ></v-text-field>

    <v-btn small class="pa-0" @click="joinRoom()">입장</v-btn>
  </div>
</template>

<script>
export default {
  name: 'MessageForm',
  data() {
    return {
      msg: '',
      roomNumber: '',
    };
  },
  methods: {
    submitMessageFunc() {
      if (this.msg.length === 0) return false;
      this.$emit('submitMessage', this.msg);
      this.msg = '';
      return true;
    },
    joinRoom() {
      if(!this.roomNumber){
        console.log("방 이름을 입력해주세요.");
        return ;
      }
      this.$emit('joinChatRoom', this.roomNumber);
    }
  },
};
</script>