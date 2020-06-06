<template>
  <div>
    <p>Hola: {{ $route.params.id }}</p>
  </div>
</template>

<script>
export default {
  async fetch () {
    await this.$store.dispatch('posts/get_posts')
  }
}
</script>
