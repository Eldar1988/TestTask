import axios from "axios"
import notifier from "src/service/notifier"
import setToken from "src/service/set_token"


export default {
  state: {
    user: null
  },
  actions: {

    async fetchUserToken({commit}, user) {
      try {
        await axios.post(`${this.getters.getServerURL}/auth/token/login/`, {
          username: user.username,
          password: user.password
        }).then(response => {
          let token = response.data.auth_token
          setToken(token)
          this.dispatch('fetchUserByToken', token)
        })
      } catch (e) {
        if (e.message === 'Request failed with status code 400') notifier('Invalid username or password')
        else notifier(e.message)
      }
    },
    async fetchUserByToken({commit}, token) {
      try {
        await axios.get(`${this.getters.getServerURL}/auth/users/me/`, {
          headers: {'Authorization': `Token ${token}`}
        }).then(response => {
          commit('setUser', response.data)
          notifier(`Welcome, ${response.data.username}!`, 'positive')
          this.$router.push('/')
        })
      } catch (e) {
        notifier(e.message)
      }
    },
    async registerUser({commit}, user) {
      try {
        await axios.post(`${this.getters.getServerURL}/auth/users/`, {
          username: user.username,
          password: user.password,
          email: user.email
        }).then(response => {
          notifier('created', response.status === 201 ? 'positive' : 'dark')
          return 'created'
        })
      } catch (e) {
        notifier(e.message)
      }
    }
  },
  mutations: {
    setUser(state, data) {
      state.user = data
    }
  },
  getters: {
    getUser: (state) => state.user
  }
}
