const selectedUser = {
  state: {
    id: "",
    name: "",
  },
  getters: {
    getSelectedUser: function (state) {
      return state;
    },
  },
  mutations: {
    setSelectedUser: function (state, payload) {
      state.id = payload.id;
      state.name = payload.name;
    },
  },
  actions: {},
};

export default selectedUser;
