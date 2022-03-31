let countButtonPtitDej = false;
let countButtonGouter = false;
let countButtonApero = false;
let countButtonPlat = false;
let countButtonDessert = false;
let countButtonSauce = false;
$( document ).ready(function() {
    $("#ptitdej").on("click",function(){
        if (countButtonPtitDej == false){
            $("#recipe-ptitdej-container").toggle();
            document.getElementById("ptitdej").style.backgroundColor = "#fec876";
            countButtonPtitDej = true;
        }
        if (countButtonGouter){
            $("#recipe-gouter-container").toggle();
            countButtonGouter = false;
            document.getElementById("gouter").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonApero){
            $("#recipe-apero-container").toggle();
            countButtonApero = false;
            document.getElementById("apero").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonPlat){
            $("#recipe-plat-container").toggle();
            countButtonPlat = false;
            document.getElementById("plat").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonDessert){
            $("#recipe-dessert-container").toggle();
            countButtonDessert = false;
            document.getElementById("dessert").style.backgroundColor = "#EAEAE7";
        }
    });
    $("#gouter").on("click",function(){
        if (countButtonGouter == false){
            $("#recipe-gouter-container").toggle();
            countButtonGouter = true;
            document.getElementById("gouter").style.backgroundColor = "#ddb792";
        }
        if (countButtonPtitDej){
            $("#recipe-ptitdej-container").toggle();
            countButtonPtitDej = false;
            document.getElementById("ptitdej").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonApero){
            $("#recipe-apero-container").toggle();
            countButtonApero = false;
            document.getElementById("apero").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonPlat){
            $("#recipe-plat-container").toggle();
            countButtonPlat = false;
            document.getElementById("plat").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonDessert){
            $("#recipe-dessert-container").toggle();
            countButtonDessert = false;
            document.getElementById("dessert").style.backgroundColor = "#EAEAE7";
        }
    });
    $("#apero").on("click",function(){
        if (countButtonApero == false){
            $("#recipe-apero-container").toggle();
            countButtonApero = true;
            document.getElementById("apero").style.backgroundColor = "#d5dd9d";
        }
        if (countButtonPtitDej){
            $("#recipe-ptitdej-container").toggle();
            countButtonPtitDej = false;
            document.getElementById("ptitdej").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonGouter){
            $("#recipe-gouter-container").toggle();
            countButtonGouter = false;
            document.getElementById("gouter").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonPlat){
            $("#recipe-plat-container").toggle();
            countButtonPlat = false;
            document.getElementById("plat").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonDessert){
            $("#recipe-dessert-container").toggle();
            countButtonDessert = false;
            document.getElementById("dessert").style.backgroundColor = "#EAEAE7";
        }
    });
    $("#plat").on("click",function(){
        if (countButtonPlat == false){
            $("#recipe-plat-container").toggle();
            countButtonPlat = true;
            document.getElementById("plat").style.backgroundColor = "#f58c74";
        }	
        if (countButtonPtitDej){
            $("#recipe-ptitdej-container").toggle();
            countButtonPtitDej = false;
            document.getElementById("ptitdej").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonGouter){
            $("#recipe-gouter-container").toggle();
            countButtonGouter = false;
            document.getElementById("gouter").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonApero){
            $("#recipe-apero-container").toggle();
            countButtonApero = false;
            document.getElementById("apero").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonDessert){
            $("#recipe-dessert-container").toggle();
            countButtonDessert = false;
            document.getElementById("dessert").style.backgroundColor = "#EAEAE7";
        }
    });
    $("#dessert").on("click",function(){
        if (countButtonDessert == false){
            $("#recipe-dessert-container").toggle();
            countButtonDessert = true;
            document.getElementById("dessert").style.backgroundColor = "#8ac5ce";
        }
        if (countButtonPtitDej){
            $("#recipe-ptitdej-container").toggle();
            countButtonPtitDej = false;
            document.getElementById("ptitdej").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonGouter){
            $("#recipe-gouter-container").toggle();
            countButtonGouter = false;
            document.getElementById("gouter").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonApero){
            $("#recipe-apero-container").toggle();
            countButtonApero = false;
            document.getElementById("apero").style.backgroundColor = "#EAEAE7";
        }
        if (countButtonPlat){
            $("#recipe-plat-container").toggle();
            countButtonPlat = false;
            document.getElementById("plat").style.backgroundColor = "#EAEAE7";
        }
    });
});