<template>
  <div id="q-app">
    <router-view />
  </div>
</template>
<script>
export default {
  name: 'App',
  beforeCreate() {
    if(localStorage.getItem('token') === null || localStorage.getItem('token') === 'null') {
      this.$router.push('/account')
    }
    else {
      this.$store.dispatch('fetchUserByToken', localStorage.getItem('token'))
    }
  }
}
</script>
