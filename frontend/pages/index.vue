<template>
  <v-layout>
    <v-container class="mx-3">
      <v-row no-glutters justify="space-around">
        <v-col v-for="post in $store.state.posts.posts" :key="post.id" cols="12" sm="6" class="justify-space-around">
          <PostCard :post="post" />
        </v-col>
      </v-row>
    </v-container>
  </v-layout>
</template>

<script>
import PostCard from '~/components/posts/card.vue'

export default {
  components: { PostCard },
  async fetch () {
    await this.$store.dispatch('posts/get_posts')
  }
}
</script>
