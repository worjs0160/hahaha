<template>
  <v-toolbar height="50" elevation="0">
    <v-row>
      <div class="d-flex align-center ma-2">
        <slot name="search_form">
          <v-text-field
            placeholder="선수 검색"
            prepend-inner-icon="mdi-magnify"
            clearable
            clear-icon="mdi-close-thick"
            hide-details="auto"
            class="mr-2"
            style="width: 200px"
          ></v-text-field>

          <v-btn small class="pa-0">검색</v-btn>
        </slot>
        <slot name="custom_slot">
          <v-btn icon>
            <v-icon>mdi-filter-variant</v-icon>
          </v-btn>
        </slot>
      </div>
      <v-spacer></v-spacer>
      <!-- <v-col class="align-self-center" style="text-align: center;"> -->
      <v-btn-toggle class="align-self-center" tile group>
        <slot name="save_slot">
          <v-btn v-on:click="selectedComponent1">선수목록</v-btn>
        </slot>
      </v-btn-toggle>
      <!-- </v-col> -->
    </v-row>
  </v-toolbar>
</template>

<script>
export default {
  methods: {
    selectedComponent1: function() {
      this.$emit("selectedComponent1", "UserList");
    },
    selectedComponent2: function() {
      this.$emit("selectedComponent2", "AttendanceList");
    },
    userDetail: function(key1, key2) {
      this.first_index = key1;
      this.second_index = key2;
    },
  },
  data() {
    return {
      filter: ["이름", "종목", "성별"],
    };
  },
};
</script>
