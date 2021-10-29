<template>

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Handlee&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
        <title>Resultados</title>
    </head>

    <body>

        <section class="carousel">

            <h1 class="titulo">Hoy puedes cocinarte:</h1>

            <div class="carousel__container">
    
                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">{{resultados[0].nameMenu}}</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">{{resultados[0].time}}</p>
                    <p class="dificultad">{{resultados[0].level}}</p>              
                </div>


               <div class="carousel-item">
                    
                    <h2 class="nombreMenu">{{resultados[1].nameMenu}}</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">{{resultados[1].time}}</p>
                    <p class="dificultad">{{resultados[1].level}}</p>              
                </div>

               <div class="carousel-item">
                    
                    <h2 class="nombreMenu">{{resultados[2].nameMenu}}</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">{{resultados[2].time}}</p>
                    <p class="dificultad">{{resultados[2].level}}</p>              
                </div>

                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">{{resultados[3].nameMenu}}</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">{{resultados[3].time}}</p>
                    <p class="dificultad">{{resultados[3].level}}</p>              
                </div>

                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">{{resultados[4].nameMenu}}</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">{{resultados[4].time}}</p>
                    <p class="dificultad">{{resultados[4].level}}</p>              
                </div>
                
            </div>
        </section>


    </body>

</template>

<script>
import axios from "axios";
import M from 'materialize-css';
import "../main.js"

export default {
    name: "Scroll",

    mounted() {
      M.AutoInit();
    },

    data: function () {
    return {
        resultados: [
            {nameMenu: "menu1",
            time: "2 mins",
            level: "1",
            },
            {nameMenu: "menu2",
            time: "4 mins",
            level: "2",
            },
            {nameMenu: "menu3",
            time: "6 mins",
            level: "1",
            },
            {nameMenu: "menu4",
            time: "8 mins",
            level: "2",
            },
            {nameMenu: "menu5",
            time: "10 mins",
            level: "1",
            },
            
        ]
        
    };
},
    methods: {
      /*getData: async function () {

        

        axios.get(`https://neverapp-des.herokuapp.com/user/${userId}/`, {headers: {'Authorization': `Bearer ${token}`}})

            .then((result) => {
                this.favoritos = result.data.favorite_menus;
                this.loaded = true;
                })
            .catch(() => {
                this.$emit('logOut');
            });
        },*/

       
    },

    /*created: async function(){
        this.getData();
    },*/
}
</script>



<style>
    *{
        margin: 0; 
        padding: 0;
        box-sizing: border-box;
        
    }

    .titulo {
        font-size: 40px;
        font-family: 'Handlee', cursive;
        margin-bottom: 40px;
        color: #A03C78;
        position: center;
    }

    .nombreMenu{
        font-size: 30px;
        color: black;
        margin-bottom: 25px;
        display: inline;
        font-weight: 500;
        text-transform: uppercase;

    }

    .tiempo, .dificultad{
        color: #A03C78;
        margin-top: 10px;
        font-size: 20px;
        font-weight: 600;
        
        


    }

    .linea-division{
        width: 80%;
        height: 2px;
        background-color: black;


    }

    .carousel{
        width: 100%;
        overflow: scroll;
        padding: 30px;
        position: relative;
        background-color: #CDF3A2;
        height: 100%;
        min-height: 90vh;
        display: flex;
        flex-wrap: nowrap;
        flex-direction: row;
        justify-content: center;
    }

    .carousel__container{
        white-space: nowrap;
        margin: 70px 0px;
        padding-bottom: 10px;
        min-height: 500px;
    }
    .carousel-item{
        background-color: #ED8E7C;
        width: 500px;
        height: 500px;
        border-radius: 15px;
        display:flex;
        flex-direction: column;
        justify-content: flex-end;
        align-items: center;
        user-select: none;
        margin-left: 20px;
    }

   
    
    .carousel-item__details p{
        margin: 0px;
    }
    /*.carousel-item__details:hover{
        opacity: 1;
        color: white;
    }*/




</style>