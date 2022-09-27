<template>
  <v-container>
    <div>
      <v-date-picker no-title multiple></v-date-picker>
    </div>
    <!-- 훈련 내용 작성 -->
    <v-form class="pr-2">
      <v-card-text class="pb-0">
        <v-container>
          <v-row class="pa-0">
            <v-col cols="12" class="pa-0">
              <!-- 훈련 내용 Input 영역 -->
              <v-textarea
                placeholder="훈련 내용"
                filled
                clearable
                outlined
                auto-grow
              ></v-textarea>
            </v-col>
          </v-row>
        </v-container>
      </v-card-text>
    </v-form>
  </v-container>
</template>

<script>
export default {
  props: {
    training: {
      id: Number,
      title: String,
      contents: String,
    },
  },
  data: () => ({}),
  components: {},
};
</script>

<style>
</style>