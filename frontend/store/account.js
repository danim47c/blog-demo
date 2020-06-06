import Cookies from 'js-cookie'

export const state = () => ({
  logged: false,
  id: 0,
  token: ''
})

export const mutations = {
  login (state, payload) {
    state.logged = true
    state.id = payload.id
    state.token = payload.token

    Cookies.set('token', payload.token)
  }
}

export const actions = {
  async refresh ({ commit, state }) {
    const token = Cookies.get('token')

    if (token && !state.token) {
      return await this.$axios.$post(
        'users/check_token/',
        {},
        { headers: { token } }
      ).then((res) => {
        return commit('login', res)
      }).catch((err) => {
        Cookies.remove('token')

        return err
      })
    }
  }
}
