<template>

    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Handlee&display=swap" rel="stylesheet">
        <title>Resultados</title>
    </head>

    <body>

        <section class="carousel">

            <div class="carousel__container">
                
                <div class="carousel-item">
                    <img class="carousel-item__img" src="" alt="...">
                    <div class="carousel-item__details">
                        <p class="carousel-item__details--nombreMenu">Nombre del menú</p>  
                        <p class="carousel-item__details--dificultad">nivel dificultad</p>
                        <p class="carousel-item__details--tiempo">tiempo preparación</p>
                    </div>                
                </div>


                <div class="carousel-item">
                    <img class="carousel-item__img" src="" alt="...">
                    <div class="carousel-item__details">
                        <p class="carousel-item__details--title">Nombre del menú</p>  
                        <p class="carousel-item__details--dificultad">nivel dificultad</p>
                        <p class="carousel-item__details--tiempo">tiempo preparación</p>
                    </div>                
                </div>
                
            </div>
        </section>

    </body>

</template>

<script>
import axios from "axios";





export default {
    name: "Scroll",
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
    body{
        margin:0px;
        font-family: 'Handlee', cursive;
        
    }

    .titulo {
        font-size: 40px;
        font-family: 'Handlee', cursive;
        margin-bottom: 40px;
        color: white;
    }

    .carousel{
        width: 100%;
        overflow: scroll;
        padding: 30px;
        position: relative;
        background-color: #CDF3A2
    }

    .carousel__container{
        white-space: nowrap;
        margin: 70px 0px;
        padding-bottom: 10px;
    }
    .carousel-item{
        background-color: #ED8E7C;
        width: 200px;
        height: 250px;
        border-radius: 20px;
        overflow: hidden;
        margin-right: 10px;
        display:inline-block;
        cursor:pointer;
        transition: 450ms all;
        transform-origin: center left;
        position: relative;
        align-items: baseline;
    }
    .carousel-item:hover ~ .carousel-item {
        transform: translate3d(100px, 0, 0);
    }
    .carousel__container:hover .carousel-item{
        opacity: 0.3;
    }
    .carousel__container:hover .carousel-item:hover{
        transform: scale(1.5);
        opacity: 1;
    }
    .carousel-item__img{
        width: 200px;
        height: 250px;
        object-fit: cover;
    }
    .carousel-item__details--nombreMenu{
        background: linear-gradient(to top, rgba(0, 0, 0, 0.9) 0%, rgba(0, 0, 0, 0) 100%);
        font-size: 10px;
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
    .carousel-item__details img{
        height: 25px;
    }
    .carousel-item__details p{
        margin: 0px;
    }
    .carousel-item__details:hover{
        opacity: 1;
        color: white;
    }




</style>