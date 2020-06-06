export const state = () => ({
  posts: []
})

export const mutations = {
  set (state, posts) {
    state.posts = posts
  }
}

export const actions = {
  async get_posts ({ commit, state }) {
    return await this.$axios.$get(
      'posts/',
      {
        headers: state.token ? {
          token: state.token
        } : {}
      }
    ).then((res) => {
      commit('set', res)
    })
  }
}
