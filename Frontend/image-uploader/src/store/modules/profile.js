import axios from 'axios'
import notifier from "src/service/notifier"

export default {
  state: {
    images: null
  },
  actions: {
    async fetchImages({commit}) {
      try {
        await axios.get(`${this.getters.getServerURL}/api/images/${this.getters.getUser.id}/`)
          .then(response => commit('setImages', response.data))
      } catch (e) {
        notifier(e.message)
      }
    },
    async deleteImage({dispatch}, id) {
      try {
        await axios.get(`${this.getters.getServerURL}/api/image_actions/${id}`)
          .then(response => {
            if (response.status === 200) {
              notifier('Image deleted')
              dispatch('fetchImages', this.getters.getUser.id)
            }
          })
      } catch (e) {
        notifier(e.message)
      }
    },
  },
  mutations: {
    setImages(state, data) {
      state.images = data
    }
  },
  getters: {
    getImages: (state) => state.images
  }
}
