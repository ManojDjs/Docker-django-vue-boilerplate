<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br>
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener">vue-cli documentation</a>.
    </p>
    <h3>Installed CLI Plugins</h3>
    <ul>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel" target="_blank" rel="noopener">babel</a></li>
      <li><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint" target="_blank" rel="noopener">eslint</a></li>
    </ul>
    <h3>Essential Links {{list}}</h3>
    <ul v-for="(item, index) in list" v-bind:key="index">
      <li>{{item}}</li>
    </ul>

  </div>
</template>

<script>

export default {
  name: 'HelloWorld',
  props: {
    msg: String
      },

  data() {
    return {
      loading: true,
      list: [1,2,3,4,5,6,7,8,9,10],
      options: {
        itemMargin: 10,
        itemClassName: 'item',
        gridWidth: 100,
        transitionDuration: '.5'
      },
    }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
