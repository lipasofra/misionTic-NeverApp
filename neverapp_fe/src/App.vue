<template>

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Handlee&display=swap" rel="stylesheet">
    <title>Neverapp</title>
  </head>

  <div id="app" class="app">

    <div class="header">
      <h1>Neverapp</h1>

      <nav>
          <button v-if="!is_auth" v-on:click="loadHome">Inicio</button>
          <button v-if="is_auth" v-on:click="loadAccount">Cuenta</button>
          <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
          <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
          <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
          
        </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:loadAccount="loadAccount"
        v-on:logOut="logOut"
        v-on:loadHome="loadHome"
      >
      </router-view>
    </div>

    <div class="footer">
      <h3>Neverapp</h3>
      <h4>Una página para tu comodidad</h4>      
    </div>

  </div>
  
</template>




<script>
export default {
  name: 'App',

  data: function(){
      return{
        is_auth: false
      }
  },

  components: {
  },

  

  methods:{
    verifyAuth: function() {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "account"});
    },

    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },

    
    loadSignUp: function(){
      this.$router.push({name: "signUp"})
    },

    loadHome: function() {
      this.$router.push({ name: "home" });
    },

    
    completedLogIn: function(data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },


    completedSignUp: function(data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },

    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },

    loadAccount: function(){
      this.$router.push({name: "account"})
    },

  },

  created: function(){
    this.verifyAuth()
  }

}
</script>




<style>

  .app{
    margin: 0;
    padding: 0;
    font-family: 'Handlee', cursive;
  }

    
  .header{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 5vh; 
    min-height: 40px;
    font-family: 'Handlee', cursive;

    background-color: #93D9A3 ;
    color:#A03C78  ;

    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    font-size: 30px;
    text-align: center;
    padding-left: 10px;
  }

  .header nav {
    width: 53%;
    display: flex;
    justify-content: flex-end;
    align-content: center;
    flex-wrap: wrap;
    flex-direction: row;
    align-items: center;
    height: 100%;
    background-color: rgba(255, 255, 255, 0);
    border: none;
    box-shadow: none;
  }

  .header nav button{
    color: white;
    padding: 10px 20px;
    background-color: rgba(255, 255, 255, 0);
    border-radius: 12%;
    border: none;
  }

  .header nav button:hover{
    color: #283747;
    background: #E5E7E9;
    border: 1px solid #E5E7E9;
  }

  
  .footer{
    margin: 0%;
    padding: 0;
    width: 100%;
    height: 5vh; 
    min-height: 40px;
    font-family: 'Handlee', cursive;

    background-color: #93D9A3 ;
    color:#E5E7E9  ;

    display: flex;
    justify-content: space-between;
    align-items: center;

    position: fixed;
    bottom: 0;

  }

  .footer h3{
    height: 50%;
    padding-left: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
  }

  .footer h4{
    padding-right: 10px;
    color:#A03C78;
    font-size: 30px;
  }

</style>
