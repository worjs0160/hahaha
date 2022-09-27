<template>
  <v-container class="pa-0" fluid style="height: 100%">
    <search-bar-header style="height: 10%">
      <template v-slot:sub-tabs>
        <v-btn-toggle class="pr-2" v-model="idx" mandatory tile group>
          <v-btn class="mr-2 px-1 d-none d-sm-flex" @click="changeSubView">
            선수목록
          </v-btn>
          <v-btn class="mr-2 px-1 d-none d-sm-flex" @click="changeSubView">
            근태관리
          </v-btn>
          <v-btn
            class="mr-2 px-1 d-flex d-sm-none"
            icon
            @click="changeSubView('선수목록')"
          >
            <v-icon>mdi-account-multiple</v-icon>
          </v-btn>
          <v-btn
            class="mr-2 px-1 d-flex d-sm-none"
            @click="changeSubView('근태관리')"
          >
            <v-icon>mdi-format-list-checkbox</v-icon>
          </v-btn>
        </v-btn-toggle>
      </template>
    </search-bar-header>
    <!-- 유저목록과 근태관리 컴포넌트 전환 영역(기본적으로 선수목록) -->
    <div style="height: 85%">
      <component
        :is="this.$store.state.tabStore.selectedSubTab"
        @coverSetChild="loadingCover">
      </component>
    </div>
  </v-container>
</template>

<script>
import UserList from "/src/views/team/attendance/UserList";
import ManageAttendance from "/src/views/team/attendance/ManageAttendance";
import SearchBarHeader from "/src/views/team/attendance/SearchBarHeader";

export default {
  components: { UserList, ManageAttendance, SearchBarHeader },
  data: () => ({
    subTabs: {
      선수목록: { idx: 0, componentName: "UserList" },
      근태관리: { idx: 1, componentName: "ManageAttendance" },
    },

  }),
  mounted: function() {
    this.setSearchbar();
  },
  methods: {
    changeSubView: function(event) {
      if (event == "선수목록" || event == "근태관리") var clickedTab = event;
      else clickedTab = event.target.innerText;
      const tab = this.subTabs[clickedTab];
      this.$store.commit("setSubTab", tab);

      this.setSearchbar();
    },
    setSearchbar: function() {
      const searchArea = document.getElementById("search-area");
      if (this.$store.state.tabStore.selectedSubTab === "ManageAttendance") {
        searchArea.setAttribute("style", "display:none !important");
      } else {
        searchArea.style.display = "block";
      }
    },
    // MainLayout으로 로딩상태 보내기
    loadingCover: function(val){
      this.$emit('coverSetChild',val);
    },
  },
  computed: {
    idx: {
      get() {
        return this.$store.state.tabStore.subIdx;
      },
      set() {
        return;
      },
    },
  },
};
</script>

<style></style>
