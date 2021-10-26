<template>
<div class="greetings">
    <h1>¡Hola<span> {{username}} </span>!...</h1>
    

<div class="buscador">
    
    <form action="" method="post" target="_blank">
<p class="barra">
    Inroduce tus alimentos: <input type="search" name="busquedamusica" placeholder="Pollo , aceitunas, camaron, brocoli...">
    <input type="submit" value="Buscar">

</p>

</form>
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
.greetings , .buscador {
margin: 0;
padding: 0%;
height: 100%;
width: 100%;

display: flex;
justify-content: center;
align-items: center;
}

.greetings h1 , .buscador{
font-size: 50px;
color: #283747;
}

.greetings, .buscador span{
color: crimson;
font-weight: bold;
}




</style>