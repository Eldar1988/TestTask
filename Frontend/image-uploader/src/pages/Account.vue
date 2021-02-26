<template>
<q-page class="flex justify-center">
  <div
    style="width: 500px; max-width: 90%; margin-top: 100px"
  >
  <q-tabs
    v-model="tab"
    dense
    class="bg-grey-3 text-grey-7"
    active-color="primary"
    indicator-color="primary"
    align="justify"
  >
    <q-tab name="login" label="Login" />
    <q-tab name="register" label="Register" />
  </q-tabs>
  <q-tab-panels v-model="tab" animated class="q-mt-md">
    <q-tab-panel name="login">
      <div class="text-h6">Login</div>
      <!--  Login form  -->
      <q-card
        bordered
        class="q-py-lg q-px-md q-mt-md shadow-0 text-center"
      >
        <q-input
          v-model="loginFormData.username"
          label="Username"
          outlined
        />
        <q-input
          v-model="loginFormData.password"
          label="Password"
          outlined
          class="q-mt-sm"
          type="password"
        />
        <q-btn
          label="Login"
          color="primary"
          class="q-mt-md q-px-md"
          @click="login(loginFormData)"
        />
      </q-card>
    </q-tab-panel>

    <q-tab-panel name="register">
      <div class="text-h6">Register</div>
      <!--  Register form  -->
      <q-card
        bordered
        class="q-py-lg q-px-md q-mt-md shadow-0 text-center"
      >
        <q-input
          v-model="registerFormData.username"
          label="Username"
          outlined
        />
        <q-input
          v-model="registerFormData.email"
          label="Email"
          outlined
          class="q-mt-sm"
          type="email"
        />
        <q-input
          v-model="registerFormData.password"
          label="Password"
          outlined
          class="q-mt-sm"
          type="password"
        />
        <q-btn
          label="Register"
          color="primary"
          class="q-mt-md q-px-md"
          @click="register(registerFormData)"
        />
      </q-card>
    </q-tab-panel>
  </q-tab-panels>
  </div>
</q-page>
</template>

<script>
export default {
  name: "Account",
  data() {
    return {
      loginFormData: {
        username: null,
        password: null,
      },
      registerFormData: {
        username: null,
        email: null,
        password: null,
      },
      tab: 'login'
    }
  },
  methods: {
    validate(data) {
      let valid = true
      data.forEach((item) => {
        if(!item) valid = false
        return valid
      })
      if(!valid) this.$q.notify({message: 'All fields required', position: 'top'})
      return valid
    },
    login(user) {
      let validate = this.validate([user.username, user.password])
      if (validate) this.$store.dispatch('fetchUserToken', user)
    },
    async register(user) {
      let validate = this.validate([user.username, user.email, user.password])
      if (validate) {
        await this.$store.dispatch('registerUser', user)
        this.tab = 'login'
      }
    }
  }
}
</script>

<style lang="sass">
.q-tab-panel
  padding: 0 !important
</style>
