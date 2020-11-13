<template>
 <div>
   <div id="app">
    <div id="nav">
      <router-link to="/">Signup</router-link> |
      <router-link to="/Login">Login</router-link>
    </div>
    <router-view/>
    </div>
<w-app block>
  <w-card class="md6 maa text-center">
<w-alert :success="success" :error="error" :info="!success &amp;&amp; !error">{{ !success && !error ? 'The form is still pristine' : (success ? 'Success' : 'Error') }}</w-alert>
<p>The form has been validated {{ validated }} time(s).</p>
<w-form @validate="validated++;success = error = false" @success="success = true" @error="error = true">
  <w-input label="First name" :validators="[validators.required]"></w-input>
  <w-input class="mt3" label="Last name" :validators="[validators.required]"></w-input>
  <div class="text-right mt6">
    <w-button type="submit">Validate</w-button>
  </div>
</w-form>
</w-card>
  
  <!-- <w-card class="md6 maa text-center">
 <div class="w-flex align-center justify-center">
    <w-button class="my6">Log in</w-button>
    <w-divider class="mx6" vertical="vertical" color="pink"></w-divider>
    <w-button class="my6">Sign in</w-button>
</div>
</w-card>
  <img alt="Vue logo" src="./assets/logo.png">
      success: null,
  error: null,
  validated: 0,
  validators: {
    required: value => !!value || 'This field is required'
  }
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Rem dolore delectus,
      quisquam ipsa laudantium esse consequatur itaque similique et eligendi eum voluptas
      odit dolor labore eveniet at vel sequi nostrum.

      <template #actions>
        <div class="spacer"></div>
        <w-button class="ma1" bg-color="error" >I disagree</w-button>
        <w-button class="ma1" bg-color="success">I agree</w-button>
      </template>
    </w-card>

  <div class="green-light5--bg pa3">
  <w-spinner fade color="green" />
  <w-spinner fade color="amber" />
  <w-spinner fade color="orange" />
  <w-spinner fade color="error" />
  <w-spinner fade color="pink" />
  </div>
    <div class="green-light5--bg pa3">
  <div class="title4 mt8 mb2">Different color per item</div>
  <w-radio class="mr2" v-model="selection1" name="radio1" color="teal-light1" :return-value="1">Option 1</w-radio>
  <w-radio v-model="selection1" name="radio1" color="teal-light1" :return-value="2">Option 2</w-radio>
  <div class="title4 mt8 mb2">Different color per item</div>
  <w-radio class="mr2" v-model="selection2" name="radio2" color="pink-light3" :return-value="1">Option 1</w-radio>
  <w-radio v-model="selection2" name="radio2" color="blue-light1" :return-value="2">Option 2</w-radio>
  </div>
  
  <w-flex class="wrap">
    <w-button class="ma1" bg-color="success">success</w-button>
    <w-button class="ma1" bg-color="error">error</w-button>
    <w-button class="ma1" bg-color="warning">warning</w-button>
    <w-button class="ma1" bg-color="info">info</w-button>
    <w-button class="ma1" bg-color="primary">primary</w-button>
    <w-button class="ma1" bg-color="secondary">secondary</w-button>
    <w-button class="ma1" bg-color="purple-light4">purple-light4</w-button>
</w-flex>
    <w-switch class="mb3" v-model="fillBar">Fill bar</w-switch>
<w-tabs :items="tabs" :fill-bar="fillBar"></w-tabs>
<w-flex wrap class="text-center">
<w-timeline :items="items" color="success"></w-timeline>
</w-flex>
<w-badge>
    <template #badge>3</template>
    <w-button color="primary">
      <w-icon class="mr1">mdi mdi-email</w-icon>
      Emails
    </w-button>
  </w-badge> -->
</w-app>
</div>
</template>
<script>
export default {
  name: 'App',
  components: {

  },
  data(){
    return{
      success: null,
    error: null,
    validated: 0,
    validators: {
      required: value => !!value || 'This field is required'
      },
      count:4,
      icons:["fa fa-github","fa fa-comment","fa fa-code","fa fa-envelope"],
      list:[{'isLink':false},{'isLink':true,url:"/doo"},{'isLink':true,url:"/foo"},{'isLink':false}],
      backgroundColor:'#17c4c5',
      color:'#ffffff',
      position:'top-left',
      isOpenNewTab:false,
    tabs: [
    { title: 'Tab 1', content: 'Tab 1 content.' },
    { title: 'Tab 2', content: 'Tab 2 content.' },
    { title: 'Tab 3', content: 'Tab 3 content.' },
    { title: 'Tab 4', content: 'Tab 4 content.' },
    { title: 'Tab 5', content: 'Tab 5 content.' }
  ],
  fillBar:true,
  items: [
    { title: 'Item 1', content: 'Content 1', icon: 'wi-check-circle' },
    { title: 'Item 2', content: 'Content 2', icon: 'wi-cross-circle' },
    { title: 'Item 3', content: 'Content 3', icon: 'wi-warning-circle' },
    { title: 'Item 4', content: 'Content 4', icon: 'wi-info-circle' }
  ],
  listItems1: [
    { label: 'Item 1', value: 1 },
    { label: 'Item 2', value: 2 },
    { label: 'Item 3', value: 3 },
    { label: 'Item 4', value: 4 },
    { label: 'Item 5', value: 5, disabled: true }
  ],
  listItems2: [
    { label: 'Star', id: 'star', icon: 'mdi mdi-star' },
    { label: 'Check', id: 'check', icon: 'mdi mdi-check' },
    { label: 'Cross', id: 'cross', icon: 'mdi mdi-close' },
    { label: 'Info', id: 'info', icon: 'mdi mdi-information' },
    { label: 'Warning', id: 'warning', icon: 'mdi mdi-alert' },
    { label: 'Disabled', id: 'disabled', icon: 'mdi mdi-minus-circle', disabled: true }
  ],
  selection1: 2,
  selection2: 1
  }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
