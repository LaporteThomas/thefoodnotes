let countButtonPtitDej = true;
let countButtonGouter = false;
let countButtonApero = false;
let countButtonPlat = false;
let countButtonDessert = false;
let countButtonSauce = false;
$( document ).ready(function() {

    $("#ptitdej").on("click",function(){
        document.getElementById("dot-title").style.color = "#fec876";
        if (countButtonPtitDej == false){countButtonPtitDej = toggle_element("ptitdej", "#fec876");}

        if (countButtonGouter){countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}
    });

    $("#gouter").on("click",function(){
        document.getElementById("dot-title").style.color = "#ddb792";
        if (countButtonGouter == false){countButtonGouter = toggle_element("gouter", "#ddb792");}

        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}
    });

    $("#apero").on("click",function(){
        document.getElementById("dot-title").style.color = "#d5dd9d";
        if (countButtonApero == false){countButtonApero = toggle_element("apero", "#d5dd9d");}

        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}
    });

    $("#plat").on("click",function(){
        document.getElementById("dot-title").style.color = "#f58c74";
        if (countButtonPlat == false){countButtonPlat = toggle_element("plat", "#f58c74");}

        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}	
    });
    $("#dessert").on("click",function(){
        document.getElementById("dot-title").style.color = "#8ac5ce";
        if (countButtonDessert == false){countButtonDessert = toggle_element("dessert", "#8ac5ce");}

        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}
    });
});

function untoggle_element(x){
    $("".concat("#recipe-", x, "-container")).toggle();
    if (window.matchMedia("(orientation: landscape)").matches){
        document.getElementById(x).style.backgroundColor = "#EAEAE7";
        document.getElementById(x).style.borderTop = "0px solid #151f26";
        document.getElementById(x).style.borderBottom = "0px solid #151f26";
    }
    else if (window.matchMedia("(orientation: portrait)").matches){
        document.getElementById(x).style.backgroundColor = "#EAEAE7";
        document.getElementById(x).style.borderLeft = "0px solid #151f26";
        document.getElementById(x).style.borderRight = "0px solid #151f26";
    }
    return false;
}

function toggle_element(x, color){
    $("".concat("#recipe-", x, "-container")).toggle();
    document.getElementById(x).style.backgroundColor = color;
    if (window.matchMedia("(max-width: 480px) and (orientation: landscape)").matches){
        document.getElementById(x).style.borderTop = "0.5px solid #151f26";
        document.getElementById(x).style.borderBottom = "0.5px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 768px) and (orientation: landscape)").matches){
        document.getElementById(x).style.borderTop = "1px solid #151f26";
        document.getElementById(x).style.borderBottom = "1px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 1279px) and (orientation: landscape)").matches){
        document.getElementById(x).style.borderTop = "2px solid #151f26";
        document.getElementById(x).style.borderBottom = "2px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 1919px) and (orientation: landscape)").matches){
        document.getElementById(x).style.borderTop = "3px solid #151f26";
        document.getElementById(x).style.borderBottom = "3px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 2559px) and (orientation: landscape)").matches){
        document.getElementById(x).style.borderTop = "4px solid #151f26";
        document.getElementById(x).style.borderBottom = "4px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 480px) and (orientation: portrait)").matches){
        document.getElementById(x).style.borderLeft = "0.5px solid #151f26";
        document.getElementById(x).style.borderRight = "0.5px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 768px) and (orientation: portrait)").matches){
        document.getElementById(x).style.borderLeft = "1px solid #151f26";
        document.getElementById(x).style.borderRight = "1px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 1079px) and (orientation: portrait)").matches){
        document.getElementById(x).style.borderLeft = "2px solid #151f26";
        document.getElementById(x).style.borderRight = "2px solid #151f26";
    }
    else if (window.matchMedia("(max-width: 1439px) and (orientation: portrait)").matches){
        document.getElementById(x).style.borderLeft = "3px solid #151f26";
        document.getElementById(x).style.borderRight = "3px solid #151f26";
    }    
    else if (window.matchMedia("(orientation: portrait)").matches){
        document.getElementById(x).style.borderLeft = "4px solid #151f26";
        document.getElementById(x).style.borderRight = "4px solid #151f26";
    }   
    else{
        document.getElementById(x).style.borderTop = "4px solid #151f26";
        document.getElementById(x).style.borderBottom = "4px solid #151f26";
    }
    return true;
}