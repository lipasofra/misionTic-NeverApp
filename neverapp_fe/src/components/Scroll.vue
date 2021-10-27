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
                    
                    <h2 class="nombreMenu">Menu 1</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">tiempo preparación</p>
                    <p class="dificultad">nivel dificultad</p>              
                </div>


               <div class="carousel-item">
                    
                    <h2 class="nombreMenu">Menu 2</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">tiempo preparación 2</p>
                    <p class="dificultad">nivel dificultad 2</p>              
                </div>

                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">Menu 3</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">tiempo preparación</p>
                    <p class="dificultad">nivel dificultad</p>              
                </div>

                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">Menu 4</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">tiempo preparación</p>
                    <p class="dificultad">nivel dificultad</p>              
                </div>

                <div class="carousel-item">
                    
                    <h2 class="nombreMenu">Menu 5</h2>  
                    <div class="linea-division"></div>
                    <p class="tiempo">tiempo preparación</p>
                    <p class="dificultad">nivel dificultad</p>              
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
        user: {
        username: "",
        password: "",
        },
    };
},
    methods: {
        
    },
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
        margin: 0;
        display: inline;
        font-weight: 500;
        text-transform: uppercase;

    }

    .tiempo, .dificultad{
        color: #A03C78;
        margin: 7px 0;
        font-size: 20px;
        font-weight: 600;
        
        margin-top: 0;


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
        justify-content: center;
        align-items: center;
        user-select: none;
        margin-left: 20px;
    }

   

    .carousel-item__details--title{
        background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0) 100%);
        font-size: 50px;
        opacity: 0;
        transition: 450ms opacity;
        padding: 10px;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
                

    }

    .carousel-item__details--dificultad{
        
        font-size: 50px;
        opacity: 0;
        transition: 450ms opacity;
        padding: 10px;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

    }

    .carousel-item__details--tiempo{
        background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0) 100%);
        font-size: 50px;
        opacity: 0;
        transition: 450ms opacity;
        padding: 10px;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

    }

    
    .carousel-item__details p{
        margin: 0px;
    }
    /*.carousel-item__details:hover{
        opacity: 1;
        color: white;
    }*/




</style>