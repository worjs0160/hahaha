<template>
  <header class="d-flex" elevation="0">
    <v-col xs="4" sm="4" md="4" id="search-area" class="d-none d-sm-flex">
        <v-text-field
          placeholder="선수 검색"
          prepend-inner-icon="mdi-magnify"
          clearable
          clear-icon="mdi-close-thick"
          hide-details
          class="mr-2"
          style="width: 200px"
          v-model="search"
        >
        </v-text-field>
        <v-btn v-on:click="searchName()">검색</v-btn>

        <v-btn icon>
          <v-icon>mdi-filter-variant</v-icon>
        </v-btn>
    </v-col>
    <v-col xs="4" sm="4" md="4" id="search-area" class="ma-1 d-flex d-sm-none" style="padding: revert;">
      <v-menu :close-on-content-click="false" transition="scroll-x-transition">
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="primary"
            class="ma-2"
            v-bind="attrs"
            v-on="on"
            icon
          >
            <v-icon>mdi-account-search</v-icon>
          </v-btn>
        </template>
        <v-col class="ma-auto d-flex" style="background-color:white">
          <v-text-field
              placeholder="선수 검색"
              prepend-inner-icon="mdi-magnify"
              clearable
              clear-icon="mdi-close-thick"
              hide-details
              class="mr-2"
              style="width: 200px"
              v-model="search"
          >
          </v-text-field>

          <v-btn v-on:click="searchName()">검색</v-btn>

          <v-btn icon>
            <v-icon>mdi-filter-variant</v-icon>
          </v-btn>
        </v-col>
      </v-menu>
    </v-col>
    <v-spacer></v-spacer>
    <div class="align-sm-self-end mt-sm-0">
      <slot name="sub-tabs"> </slot>
    </div>
  </header>
</template>

<script>
import eventBus from "/src/main.js";

export default {
  methods: {
    //UserList로 검색어 데이터를 보냄(eventbus 사용)
    searchName: function () {
      eventBus.$emit("searchEvent", this.search);
    },
  },
  data: () => ({
    search: "",
    show:false,
    selectedTab: undefined,
  }),
};
</script>

<style></style>
