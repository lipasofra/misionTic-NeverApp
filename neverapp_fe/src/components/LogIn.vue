<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>

      <form v-on:submit.prevent="processLogInUser">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <button type="submit">Iniciar Sesion</button>
      </form>
    </div>
  </div>
</template>




<script>
import axios from "axios";
export default {
    name: "LogIn",
    data: function () {
    return {
        user: {
        username: "",
        password: "",
        },
    };
},
methods: {
    processLogInUser: function () {
        axios.post("https://neverapp-des.herokuapp.com/login/", this.user, {
            headers: {},
        })
        .then((result) => {
            let dataLogIn = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
            };
            this.$emit("completedLogIn", dataLogIn);
        })
        .catch((error) => {

            if (error.response.status == "401")
                alert("ERROR 401: Credenciales Incorrectas.");
        });
    },
},
};
</script>



<style>

    .logIn_user{
        margin: 0;
        padding: 0%;
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color:rgba(205, 243, 162, 0.6) ;
        min-height: 90vh;
    }

    .container_logIn_user {
        border: 3px solid #A03C78;
        border-radius: 20px;
        width: 30%;
        height: 70%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .logIn_user h2{
        color: #A03C78;
    }

    .logIn_user form{
        width: 70%;
    }

    .logIn_user input{
        height: 40px;
        width: 100%;
        box-sizing: border-box;
        padding: 10px 20px;
        margin: 5px 0;
        border: 1px solid #A03C78;
        background: rgba(255, 255, 255, 0.4);
        border: 2px solid white;
        padding-bottom: 10px;
        border-radius: 25px;
        color: black;
    }

    .logIn_user button{
        width: 100%;
        height: 40px;
        color: #E5E7E9;
        background: #A03C78;
        border: 1px solid #E5E7E9;
        border-radius: 25px;
        padding: 0px 25px;
        margin: 10px 0;
        margin-bottom: 30px;
    }

    .logIn_user button:hover{
        color: #E5E7E9;
        border: 1px solid #283747;
        cursor: pointer;
        }

</style>