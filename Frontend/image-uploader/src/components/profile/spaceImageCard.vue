<template>
  <div>
    <q-card
    >
      <q-img
        :src="image.image"
        class="image"
      >
        <q-btn
          icon="delete"
          color="white"
          text-color="negative"
          dense
          size="sm"
          class="q-ma-sm"
          @click="deleteImage(image.id)"
        />
      </q-img>
      <q-btn
        label="Update image"
        size="sm"
        color="primary"
        class="q-ma-sm"
        @click="imageUpdateDialog = true"
        unelevated
      />
      <q-btn
        label="Image story"
        size="sm"
        color="primary"
        class="q-ma-sm"
        @click="showActions = true"
        unelevated
      />
    </q-card>


    <!--    Image Actions Story   -->
    <q-dialog
      v-model="showActions"
    >
      <q-card
        style="width: 500px; max-width: 90%"
      >
        <q-toolbar style="padding: 0; min-height: auto">
          <q-toolbar-title class="bg-primary text-white q-pa-md">
            <div class="flex justify-between q-px-md" style="align-items: center">
              <p class="text-h6">Image story</p>
              <q-btn
                icon="close"
                flat padding="0"
                v-close-popup
              />
            </div>
          </q-toolbar-title>
        </q-toolbar>
        <div
          v-for="(action, index) in image.actions"
          :key="index"
          class="q-ma-sm"
        >
          <q-card
            bordered
            class="shadow-0"
          >
            <div class="row q-pa-sm">
              <div class="col-3">
                <q-img
                  :src="action.from_image"
                  class="rounded-borders"
                />
              </div>
              <div class="col-9 q-pl-sm">
                <p>{{ action.date }}</p>
                <p class="text-bold">{{ action.type }}</p>
              </div>
            </div>
          </q-card>
        </div>
      </q-card>
    </q-dialog>

    <!--    Image Update   -->
    <q-dialog
      v-model="imageUpdateDialog"
    >
      <q-uploader
        :url="`${this.$store.getters.getServerURL}/api/image_actions/${image.id}/`"
        style="width: 500px; max-width: 80%"
        field-name="image"
        class="q-mt-md"
        max-file-size="2097152"
        method="PUT"
        @rejected="uploadFileRejected"
        @uploaded="fileUploaded"
      />
    </q-dialog>
  </div>
</template>

<script>
import notifier from "src/service/notifier"
import uploadFileRejected from "src/service/upload_file_rejected"

export default {
  name: "spaceImageCard",
  props: {
    image: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      imageUpdateDialog: false,
      showActions: false
    }
  },
  computed: {
    user() {
      return this.$store.getters.getUser
    }
  },
  methods: {
    deleteImage(id) {
      this.$store.dispatch('deleteImage', id)
    },
    fileUploaded() {
      this.$store.dispatch('fetchImages', this.user.id)
      notifier('Image updated', 'positive')
      this.imageUpdateDialog = false
    },
    uploadFileRejected

  }
}
</script>

<style scoped>

</style>
