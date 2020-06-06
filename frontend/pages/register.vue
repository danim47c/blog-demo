<template>
  <v-layout class="d-flex flex-column justify-center align-center">
    <v-col cols="8">
      <v-text-field
        v-model="username"
        label="Username"
        counter
        maxlength="128"
        :rules="[rules.required]"
      />
    </v-col>
    <v-col cols="8">
      <v-text-field
        v-model="password"
        :append-icon="password_show ? 'mdi-eye' : 'mdi-eye-off'"
        :type="password_show ? 'text' : 'password'"
        :rules="[rules.required]"
        name="input-10-1"
        label="Password"
        @click:append="password_show = !password_show"
      />
    </v-col>
    <v-col cols="8">
      <div class="d-flex justify-center align-center">
        <v-checkbox v-model="tc_accept" label="Accept terms & conditions" :rules="[rules.required]" />
      </div>
    </v-col>
    <v-col cols="8">
      <div class="d-flex justify-center align-center">
        <v-btn :disabled="!(username && password && tc_accept)" @click="register()">
          Register
        </v-btn>
      </div>
    </v-col>

    <v-dialog
      v-model="dialog"
      persistent
      width="300"
    >
      <v-card>
        <v-progress-linear
          indeterminate
          class="mb-0"
        />
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="dialog_taken"
      width="300"
    >
      <v-card>
        <v-card-title>
          Username Taken
        </v-card-title>

        <v-card-actions>
          <v-spacer />

          <v-btn
            text
            @click="dialog_taken = false; username = ''"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {
      username: '',
      password: '',
      tc_accept: false,
      password_show: false,
      dialog: false,
      dialog_taken: false,
      rules: {
        required: value => !!value || 'This field is required'
      }
    }
  },
  methods: {
    register () {
      this.dialog = true

      this.$axios.post(
        '/users/register/',
        {
          username: this.username,
          password: this.password
        }
      ).then(
        (res) => {
          this.$store.commit('account/login', res)
          this.$router.push('/')
        }
      ).catch(
        (err) => {
          if (err.response && err.response.status === 422) {
            this.dialog_taken = true
          }
        }
      )

      this.dialog = false
    }
  }
}
</script>
