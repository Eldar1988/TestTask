<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  created() {
    if(localStorage.getItem('token') === null || localStorage.getItem('token') === 'null') {
      this.$router.push('/account')
    }
    else {
      this.$store.dispatch('fetchUserByToken', localStorage.getItem('token'))
    }
  },
  watch: {
    '$route.path'() {
      this.redirectNotAuthUser()
    }
  },
  methods: {
    redirectNotAuthUser() {
      if(localStorage.getItem('token') === null || localStorage.getItem('token') === 'null') {
        this.$router.push('/account')
      }
    }
  }
}
</script>
