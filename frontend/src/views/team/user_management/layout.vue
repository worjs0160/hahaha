<template>
  <v-container class="pa-0" fluid style="height: 100%">
    <template>
      <v-btn-toggle class="pr-2" v-model="idx" mandatory tile group>
        <v-btn id="0" class="mr-2 px-1 d-none d-sm-flex" @click="changeSubView">
          직원승인
        </v-btn>
        <v-btn id="1" class="mr-2 px-1 d-none d-sm-flex" @click="changeSubView">
          선수매칭
        </v-btn>
        <v-btn id="2" class="mr-2 px-1 d-none d-sm-flex" @click="changeSubView">
          선수정보관리
        </v-btn>
      </v-btn-toggle>
    </template>

    <!-- 컴포넌트 전환 영역 -->
    <div style="height: 85%" class="pa-5">
      <component
        :is="this.seltab.componentName"
        @coverSetChild="loadingCover"
      >
      </component>
    </div>
  </v-container>
</template>

<script>
import approve from "./approve.vue";
import matching from "./matching.vue";
import information from "./information.vue";

export default {
  components: { approve, matching, information },
  data: () => ({
    subTabs: {
      직원승인: { idx: 0, componentName: "approve" },
      선수매칭: { idx: 1, componentName: "matching" },
      선수정보관리: { idx: 2, componentName: "information" },
    },
    seltab: { idx: 0, componentName: "approve" },
  }),
  computed: {
    idx: {
      get() {
        return this.seltab.idx;
      },
      set() {
        return;
      },
    },
  },
  methods: {
    changeSubView: function(event) {
      // 메소드 안에서 사용하는 `this` 는 Vue 인스턴스를 가리킵니다
      const clickedTab = event.target.innerText;
      const tab = this.subTabs[clickedTab];
      this.seltab = tab;
    },
    //MainLayout으로 로딩상태 전달
    loadingCover(val){
      this.$emit('coverSetChild',val);
    },
  },
};
</script>
