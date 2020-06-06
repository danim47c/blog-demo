<template>
  <div>
    <v-hover v-slot:default="{ hover }">
      <v-card :elevation="hover ? 16 : 0" nuxt :to="`/posts/${post.id}`">
        <v-card-title v-text="post.title" />

        <v-card-text v-text="post.content" />

        <v-card-actions>
          <v-list-item>
            <v-btn outlined rounded nuxt :to="`/users/${post.author.id}`">
              <v-icon class="mr-2">
                mdi-account
              </v-icon>
              <span class="subheading" v-text="post.author.username" />
            </v-btn>

            <v-row
              align="center"
              justify="end"
            >
              <v-chip outlined>
                <v-avatar left>
                  <v-icon>mdi-heart</v-icon>
                </v-avatar>
                <span v-text="post.likes.length" />
              </v-chip>
              <v-chip outlined class="ml-3">
                <v-avatar left>
                  <v-icon>mdi-eye</v-icon>
                </v-avatar>
                <span v-text="post.visits.length" />
              </v-chip>
            </v-row>
          </v-list-item>
        </v-card-actions>
      </v-card>
    </v-hover>
  </div>
</template>

<script>
export default {
  props: {
    post: {
      type: Object,
      required: true
    }
  }
}
</script>
