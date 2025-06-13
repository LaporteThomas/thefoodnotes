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
        changeLineHeight: true,
        explicitWidth: 160,
        explicitHeight: 160
    });

    $("#ptitdej").on("click",function(){
        document.getElementById("title-list").textContent="p'tit-déj";
        if (countButtonGouter){countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonPtitDej == false){countButtonPtitDej = toggle_element("ptitdej", "#fec876");}
    });

    $("#gouter").on("click",function(){
        document.getElementById("title-list").textContent="goûter";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonApero){ countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonGouter == false){countButtonGouter = toggle_element("gouter", "#ddb792");}

        if (changeButtonGouter == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true,
                explicitWidth: 160,
                explicitHeight: 160
            });
            changeButtonGouter = true;
        }
    });

    $("#apero").on("click",function(){
        document.getElementById("title-list").textContent="apéro";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonApero == false){countButtonApero = toggle_element("apero", "#d5dd9d");}

        if (changeButtonApero == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true,
                explicitWidth: 160,
                explicitHeight: 160
            });
            changeButtonApero = true;
        }
    });

    $("#plat").on("click",function(){
        document.getElementById("title-list").textContent="plat";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonDessert){countButtonDessert = untoggle_element("dessert");}

        if (countButtonPlat == false){countButtonPlat = toggle_element("plat", "#f58c74");}

        if (changeButtonPlat == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true,
                explicitWidth: 160,
                explicitHeight: 160
            });
            changeButtonPlat = true;
        }
    });
    $("#dessert").on("click",function(){
        document.getElementById("title-list").textContent="dessert";
        if (countButtonPtitDej){countButtonPtitDej = untoggle_element("ptitdej");}

        else if (countButtonGouter){ countButtonGouter = untoggle_element("gouter");}

        else if (countButtonApero){countButtonApero = untoggle_element("apero");}

        else if (countButtonPlat){countButtonPlat = untoggle_element("plat");}

        if (countButtonDessert == false){countButtonDessert = toggle_element("dessert", "#8ac5ce");}

        if (changeButtonDessert == false){
            $('a').textfill({
                maxFontPixels: 30,
                changeLineHeight: true,
                explicitWidth: 160,
                explicitHeight: 160
            });
            changeButtonDessert = true;
        }
    });
});

function untoggle_element(x){
    $("".concat("#recipe-", x, "-container")).toggle();
    document.getElementById(x).style.fontWeight = 400;
    
    return false;
}

function toggle_element(x, color){
    $("".concat("#recipe-", x, "-container")).toggle();
    document.getElementById(x).style.fontWeight = 900;   
    return true;
}

function showSectionFromHash() {
    const hash = window.location.hash;
    if (hash) {
        // Hide all sections first
        $('.section-recipe').hide();
        
        // Show the section from hash
        $(hash).show();
        
        // Update the title
        const sectionId = hash.replace('#recipe-', '').replace('-container', '');
        document.getElementById("title-list").textContent = sectionId;
        
        // Update button states
        $('.inner-box-title').css('font-weight', '400');
        $('#' + sectionId).css('font-weight', '900');
        
        // Update the corresponding count variables
        countButtonPtitDej = (sectionId === 'ptitdej');
        countButtonGouter = (sectionId === 'gouter');
        countButtonApero = (sectionId === 'apero');
        countButtonPlat = (sectionId === 'plat');
        countButtonDessert = (sectionId === 'dessert');
    }
}

// Function to update URL hash
function updateHash(sectionId) {
    window.location.hash = `#recipe-${sectionId}-container`;
}

// Call the function when the page loads
$(document).ready(function() {
    showSectionFromHash();

    // Update click handlers for buttons
    $("#ptitdej").on("click", function() {
        updateHash('ptitdej');
    });

    $("#gouter").on("click", function() {
        updateHash('gouter');
    });

    $("#apero").on("click", function() {
        updateHash('apero');
    });

    $("#plat").on("click", function() {
        updateHash('plat');
    });

    $("#dessert").on("click", function() {
        updateHash('dessert');
    });
});