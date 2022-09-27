const authStore = {
  state: {
    access_token: "",
    refresh_token: "",
  },
  getters: {
    getToken: function(state) {
      return state;
    },
  },
  mutations: {
    setToken: function(state, payload) {
      state.access_token = payload.access_token;
      state.refresh_token = payload.refresh_token;
    },
    setAccess: function(state, payload) {
      state.access_token = payload;
    },
  },
  actions: {},
};

export default authStore;
