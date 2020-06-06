<template>
  <v-app>
    <div>
      <v-app-bar color="secondary">
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-spacer />

        <nuxt-link to="/">
          <v-toolbar-title class="white--text">
            Blog
          </v-toolbar-title>
        </nuxt-link>

        <v-spacer />

        <div v-if="$store.state.account.logged">
          <v-btn icon nuxt to="/account">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </div>
        <div v-else color="secondary">
          <v-btn class="mr-2" nuxt to="/register">
            Register
          </v-btn>
          <v-btn nuxt to="/login">
            Login
          </v-btn>
        </div>
      </v-app-bar>
    </div>

    <nuxt />
  </v-app>
</template>

<script>
export default {
  async fetch () {
    await this.$store.dispatch('account/refresh')
  }
}
</script>

<style lang="scss">
a, a:hover, a:visited, a:link, a:active {
  text-decoration: none;
  color: white;
}
</style>
