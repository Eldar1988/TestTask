<template>
  <q-page class="flex flex-center column">
    <h1 class="text-h6">Image uploader</h1>
    <q-uploader
      :url="`${this.$store.getters.getServerURL}/api/image_actions/${user.id}/`"
      style="width: 500px; max-width: 80%"
      field-name="image"
      class="q-mt-md"
      max-file-size="2097152"
      method="POST"
      :headers="[{name: 'Authorization', value: `Token ${token}`}]"
      @rejected="uploadFileRejected"
      @uploaded="notifier('File uploaded', 'positive')"
    />
  </q-page>
</template>

<script>
import uploadFileRejected from "src/service/upload_file_rejected"
import notifier from "src/service/notifier"

export default {
  name: 'PageIndex',
  computed: {
    token() {
      return localStorage.getItem('token')
    }
  },
  data() {
    return {
      image: null,
      user: null
    }
  },

  mounted() {
    this.getUser()
  },
  methods: {
    uploadFileRejected,
    notifier,
    getUser() {
      this.user = this.$store.getters.getUser
    }
  }
}
</script>
