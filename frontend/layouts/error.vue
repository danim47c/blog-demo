<template>
  <v-app>
    <h1 v-if="error.statusCode === 404">
      Page not found
    </h1>
    <h1 v-else>
      An error occurred
    </h1>
    <nuxt-link to="/">
      Home page
    </nuxt-link>
  </v-app>
</template>

<script>
export default {
  props: { error: { type: Object, required: true } }
}
</script>
