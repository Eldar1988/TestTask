<template>
  <q-page class="q-pa-md">
    <div class="flex justify-between">
      <q-breadcrumbs>
        <q-breadcrumbs-el icon="home" to="/"/>
        <q-breadcrumbs-el label="Profile"/>
      </q-breadcrumbs>
      <q-btn
        label="Logout"
        @click="logout"
        color="dark"
        class="q-px-sm"
        size="sm"
      />
    </div>
    <div class=" q-mt-md">
      <h1 class="text-h6">Images</h1>
      <div class="row">
        <div
          v-for="(image, index) in images"
          :key="index"
          class="col-6 col-sm-4 col-lg-3"
          style="padding: 2px"
        >
          <space-image-card :image="image"/>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script>
import SpaceImageCard from "components/profile/spaceImageCard"

export default {
  name: "Profile",
  components: {SpaceImageCard},
  computed: {
    images() {
      return this.$store.getters.getImages
    }
  },
  created() {
    this.$store.dispatch('fetchImages')
  },
  methods: {
    logout() {
      localStorage.setItem('token', null)
      location.reload()
    }
  }
}
</script>

<style lang="sass">
.image
  height: 400px
  @media screen and (max-width: 992px)
    height: 300px
  @media screen and (max-width: 650px)
    height: 200px

</style>
