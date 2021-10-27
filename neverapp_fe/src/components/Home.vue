<template>
 

<div class="buscador">

    <h2 class="main__title">¿Qué tienes para comer hoy?</h2>

    <div class="barra">
        <input class="input" type="text" placeholder="Pollo , aceitunas, camaron, brocoli...">
    </div>
    <div class="boton">
        <input type="submit" value="Buscar">
    </div>


</div>


   

</template>


<script>

export default {
    name: "Home",
    
    data: function(){
        return {
            username: localStorage.getItem('username') || ""
        }
    }
}

</script>


<style>
    .buscador {
        background-color:rgba(205, 243, 162, 0.6) ;
        padding: 0%;
        height: 100%;
        width: 100%;

        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }

    .buscador h2{
        font-size: 50px;
        color: #A03C78;
        padding-top: 10%;
        margin-bottom: 15px;
    }

    .barra {
        background-color: rgba(255, 255, 255, 0.4);
        border: 2px solid white;
        padding-bottom: 10px;
        border-radius: 25px;
        color: white;
        
        
        font-size: 16px;
        height: 40px;
        margin-bottom: 20px;
        width: 80%;
        
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }

    .input{

        background-color: rgba(255, 255, 255, 0);
        border: none;
        color: white;
        
        
        font-size: 16px;
        height: 40px;
        width: 100%;
        padding-left: 20px;
        padding-top: 10px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
    }

    




</style>