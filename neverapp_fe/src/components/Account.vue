<template>
    <div class="information">
        <h1>¡Bienvenido <span> {{username}} </span>!</h1>
        <h2>Tus menús favoritos son:</h2>

        <ul class="lista">
            <li v-for="favorito of favoritos" :key="favorito">{{ favorito }}</li>
        </ul>

        
        
    </div>
</template>

<script>
import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: "Account",
    
    data: function(){
        return {
            username: localStorage.getItem('username') || "none",
            favoritos:[],
            loaded: false,
        }
    },

    methods: {
       getData: async function () {

            if (localStorage.getItem("token_access") === null || localStorage.getItem("token_refresh") === null) {
                this.$emit('logOut');
                return;
            }

            await this.verifyToken();

            let token = localStorage.getItem("token_access");
            let userId = jwt_decode(token).user_id.toString();

            axios.get(`https://neverapp-des.herokuapp.com/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})

                .then((result) => {
                    this.favoritos = result.data.favorite_menus;
                    this.loaded = true;
                    })
                .catch(() => {
                    this.$emit('logOut');
                });
        },

        verifyToken: function () {
            return axios.post("https://neverapp-des.herokuapp.com/refresh/", {refresh: localStorage.getItem("token_refresh")}, {headers: {}})

                .then((result) => {
                    localStorage.setItem("token_access", result.data.access);
                })
                .catch(() => {
                    this.$emit('logOut');
                });
        }
    },

    created: async function(){
        this.getData();
    },
}
</script>

<style>
    .information{
        margin: 0;
        padding: 0%;
        width: 100%;
        height: 100%;
        min-height: 90vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        background-color: rgba(205, 243, 162, 0.6);
    }

    .information h1{
        font-size: 60px;
        color: #A03C78;
    }

    .information h2{
        font-size: 40px;
        color: #A03C78;
    }

    .information span{
        color: #A03C78;
        font-weight: bold;
    }

    .lista{
        color: #A03C78;
        font-weight: bold;
        font-size: 50px;
    }

</style>