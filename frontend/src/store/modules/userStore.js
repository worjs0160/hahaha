const userStore = {
  state: {
    id: "",
    username: "",
    name: "",
    email: "",
    userType: "",
    phoneNum: "",
    team: "",
    company: "",
    serverDate: "",
    sportType: "",
    comID: "",
    teamID: "",
    managerNum: "",
  },
  getters: {
    getUser: function(state) {
      return state;
    },
  },
  mutations: {
    setId: function(state, id) {
      state.id = id;
    },
    setUser: function(state, payload) {
      state.id = payload.id;
      state.username = payload.username;
      state.name = payload.name;
      state.email = payload.email;
      state.userType = payload.userType;
      state.phoneNum = payload.phoneNum;
      //state.teamID = payload.teamID;
      state.company = payload.company;
      state.sportType = payload.sportType;
      state.comID = payload.comID;
      state.managerNum = payload.comNum;
    },
    setEmployee: function(state, payload) {
      state.teamID = payload.teamID.id;
      state.teamAllowedIP = payload.teamID.allowedIP;
    },
    setDate: function(state, payload) {
      const inputedDate = new Date(payload.date);

      const year = inputedDate.getFullYear();
      let month = "0" + (inputedDate.getMonth() + 1);
      let date = "0" + inputedDate.getDate();

      month = month.slice(-2);
      date = date.slice(-2);

      state.serverDate = year + "-" + month + "-" + date;
    },
  },
  actions: {},
};

export default userStore;
