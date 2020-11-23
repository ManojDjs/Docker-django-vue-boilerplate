<template>
<div> 
<!-- The navigation menu will get the value of the "active" variable as a class. -->

 <!-- To stops the page from jumping when a link is clicked 
        we use the "prevent" modifier (short for preventDefault). -->

          <nav v-bind:class="active"  :style=style v-on:click.prevent>

            
            <ul >
            <li  v-if='window.width>800'><h1 class='namehead'>Vue<span class='name'>Jango</span></h1></li>
            <li  ><router-link to='#'><b-icon-person-plus-fill variant="primary" :style=navlist class="h3 mb-2 blue-text"></b-icon-person-plus-fill></router-link></li>
            <li ><router-link to='#'><b-icon-plus-circle variant="primary" :style=navlist class="h3 mb-2" ></b-icon-plus-circle></router-link></li>
            <li ><router-link to='#'><b-icon-search variant="primary" :style=navlist  class="h3 mb-2 blue-text"></b-icon-search></router-link></li>
            <li ><router-link to='#'><b-icon-chat-dots variant="primary" :style=navlist class="h3 mb-2"></b-icon-chat-dots></router-link></li>
            <li ><router-link to='#'><b-icon-person-lines-fill variant="primary" :style=navlist class="h3 mb-2"></b-icon-person-lines-fill> </router-link></li>
          </ul>
          </nav>


</div>
</template>
<script>
export default {
    
}
</script>
<style scoped>
 *{
  margin:0;
  padding:0;
}

body{
  font:15px/1.3 'Open Sans', sans-serif;
  color: #5e5b64;
  text-align:center;
}

li, li:visited {
  outline:none;
  color:#5e5b64;
}

li:hover{
  text-decoration:none;
}

section, footer, header, aside, nav{
  display: block;
}

/*-------------------------
  The menu
--------------------------*/

nav{
  display:inline-block;
  margin:20px auto 15px;
  background-color:#FFFFFF;
  box-shadow:0 1px 1px #ccc;
  border-radius:2px;
  
}

nav ul li{
  display:inline-block;
  padding: 25px 30px;
/*  color:#fff !important; */
  font-weight:bold;
  font-size:20px;
  text-decoration:none !important;
  line-height:1;
  color:black;
/*  text-transform: uppercase; */
/*  background-color:transparent; */

  -webkit-transition:background-color 0.25s;
  -moz-transition:background-color 0.25s;
  transition:background-color 0.25s;
}

nav ul li:first-child{
  border-radius:2px 0 0 2px;
}

nav ul li:last-child{
  border-radius:0 2px 2px 0;
}



p{
  font-size:22px;
  font-weight:bold;
  color:#7d9098;
}

p b{
  color:#ffffff;
  display:inline-block;
  padding:5px 10px;
  background-color:#c4d7e0;
  border-radius:2px;
  text-transform:uppercase;
  font-size:18px;
}
.home{
  font-size:0.3in;
 
}
.name{
  color:#3756dd;
  font-size: 0.875em;
}
.namehead{
  color:#050101;
  font-size: 1.875em;
}


</style>