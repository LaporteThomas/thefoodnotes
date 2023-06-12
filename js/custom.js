let countButtonPtitDej = true;
let countButtonGouter = false;
let countButtonApero = false;
let countButtonPlat = false;
let countButtonDessert = false;
let countButtonSauce = false;

let changeButtonPtitDej = true;
let changeButtonGouter = false;
let changeButtonApero = false;
let changeButtonPlat = false;
let changeButtonDessert = false;
let changeButtonSauce = false;
$( document ).ready(function() {
    $('a').textfill({
        maxFontPixels: 30,
        changeLineHeight: true
    });

    $("#ptitdej").on("click",function(){
        document.getElementById("dot-title").style.color = "#fec876";
        if (countButtonGouter){countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonPtitDej == false){countButtonPtitDej = toggle_element("ptitdej", "#fec876");}
    });

    $("#gouter").on("click",function(){
        document.getElementById("dot-title").style.color = "#ddb792";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonGouter == false){countButtonGouter = toggle_element("gouter", "#ddb792");}

        if (changeButtonGouter == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true
            });
            changeButtonGouter = true;
        }
    });

    $("#apero").on("click",function(){
        document.getElementById("dot-title").style.color = "#d5dd9d";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonApero == false){countButtonApero = toggle_element("apero", "#d5dd9d");}

        if (changeButtonApero == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true
            });
            changeButtonApero = true;
        }
    });

    $("#plat").on("click",function(){
        document.getElementById("dot-title").style.color = "#f58c74";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonPlat == false){countButtonPlat = toggle_element("plat", "#f58c74");}

        if (changeButtonPlat == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true
            });
            changeButtonPlat = true;
        }
    });
    $("#dessert").on("click",function(){
        document.getElementById("dot-title").style.color = "#8ac5ce";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        if (countButtonDessert == false){countButtonDessert = toggle_element("dessert", "#8ac5ce");}

        if (changeButtonDessert == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true
            });
            changeButtonDessert = true;
        }
    });
});

function untoggle_element(x){
    $("".concat("#recipe-", x, "-container")).toggle();
    document.getElementById(x).style.backgroundColor = "#EAEAE7";
    if (x=="ptitdej"){
        document.getElementById(x).style.borderLeft = "4px solid #EAEAE7";
    }
    else if (x=="gouter"){
        document.getElementById("ptitdej").style.borderRight = "4px solid #EAEAE7";
    }
    else if (x=="apero"){
        document.getElementById("gouter").style.borderRight = "4px solid #EAEAE7";
    }
    else if (x=="plat"){
        document.getElementById("apero").style.borderRight = "4px solid #EAEAE7";
    }
    else if (x=="dessert"){
        document.getElementById("plat").style.borderRight = "4px solid #EAEAE7";
    }
    document.getElementById(x).style.borderRight = "4px solid #EAEAE7";
    return false;
}

function toggle_element(x, color){
    $("".concat("#recipe-", x, "-container")).toggle();
    document.getElementById(x).style.backgroundColor = color;
    if (x=="ptitdej"){
        document.getElementById(x).style.borderLeft = "4px solid #151f26";
        document.getElementById(x).style.borderRight = "4px solid #151f26";
    }
    else if (x=="gouter"){
        document.getElementById(x).style.borderRight = "4px solid #151f26";
        // document.getElementById(x).style.borderLeft = "4px solid #ddb792";
        document.getElementById("ptitdej").style.borderRight = "4px solid #151f26";
    }
    else if (x=="apero"){
        document.getElementById(x).style.borderRight = "4px solid #151f26";
        // document.getElementById(x).style.borderLeft = "4px solid #d5dd9d";
        document.getElementById("gouter").style.borderRight = "4px solid #151f26";
    }
    else if (x=="plat"){
        document.getElementById(x).style.borderRight = "4px solid #151f26";
        // document.getElementById(x).style.borderLeft = "4px solid #f58c74";
        document.getElementById("apero").style.borderRight = "4px solid #151f26";
    }   
    else if (x=="dessert"){
        document.getElementById(x).style.borderRight = "4px solid #151f26";
        // document.getElementById(x).style.borderLeft = "4px solid #8ac5ce";
        document.getElementById("plat").style.borderRight = "4px solid #151f26";
    }

    // $('a').textfill({
    //     maxFontPixels: 30,
    //     changeLineHeight: true
    // });

    // if (window.innerWidth >= 768) {
    //     $('a').textfill({
    //         maxFontPixels: 30
    //     });
    // } else {
    //     $('a').textfill({
    //         maxFontPixels: 24
    //     });
    // }        
    return true;
}