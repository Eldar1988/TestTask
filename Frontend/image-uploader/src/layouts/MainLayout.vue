<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title>
          <router-link to="/" class="text-white">
            Image uploader
          </router-link>
        </q-toolbar-title>

        <div v-if="user">
          <q-btn
            :label="user.username"
            icon="person"
            color="white"
            outline
            to="/profile"
          />
        </div>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>

export default {
  name: 'MainLayout',
  data() {
    return {}
  },
  computed: {
    user() {
      return this.$store.getters.getUser
    }
  }
}
</script>
