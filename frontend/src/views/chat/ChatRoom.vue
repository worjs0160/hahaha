<template>
  <div class="inner-wrap" fluid fill-height inner-wrap>
    <Message-List :msgs="msgDatas" class="msg-list"></Message-List>
    <Message-Form @submitMessage="sendMessage" @joinChatRoom="makeJoin" class="msg-form" ></Message-Form>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex';
import MessageList from '@/views/chat/MessageList.vue';
import MessageForm from '@/views/chat/MessageForm.vue';
import Constant from '@/constant';

export default {
  name: 'ChatRoom',
  data() {
    return {
      datas: [],
    };
  },
  components: {
    'Message-List': MessageList,
    'Message-Form': MessageForm,
  },
  computed: {
    ...mapState({
      'msgDatas': state => state.socket.msgDatas,
    }),
  },
  async created() {
    const $ths = this;
    await this.$socket.on('chat', (data) => {
      this.pushMsgData(data);
      $ths.datas.push(data);
    });
  },
  methods: {
    ...mapMutations({
      'pushMsgData': Constant.PUSH_MSG_DATA,
    }),
    sendMessage(msg) {
      this.pushMsgData({
        from: {
          name: '나',
        },
        msg,
      });
      this.$sendMessage({
        name: this.$route.params.username,
        msg,
      });
    },
    makeJoin(roomid){
      this.$socket.emit('join', roomid);
    }
  },
};
</script>

<style>
.msg-form {
  bottom: -28px;
  position: absolute;
  left: 0;
  right: 0;
}
.msg-list {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 60px;
  overflow-x: scroll;
}
</style>