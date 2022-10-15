const tabStore = {
  state: {
    idx: 0,
    subIdx: 0,
    selectedTab: "Contributor",
    selectedSubTab: "",
  },
  getters: {
    getTab: function(state) {
      return state;
    },
  },
  mutations: {
    setComponent: function(state, payload) {
      state.idx = payload.idx;
      state.selectedTab = payload.componentName;
    },
    setSubTab: function(state, payload) {
      state.subIdx = payload.idx;
      state.selectedSubTab = payload.componentName;
    },
  },
  actions: {},
};

export default tabStore;
