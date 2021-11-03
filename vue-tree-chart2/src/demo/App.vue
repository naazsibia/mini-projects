<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title>Tree Chart</v-toolbar-title>
    </v-toolbar>

    <router-view style="width: 100%; height: 100%;" />
  </v-app>
</template>

<script lang="ts">
import * as Cons from './router/constant'

export default {
  name: 'App',
  data() {
    return {
      Cons
    }
  }
}
</script>

<style lang="less" scoped>
.menu-item {
  display: inline-block;
  display: flex;
  height: 100%;
  margin: 0;
}
</style>
