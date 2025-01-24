$( document ).ready(function() {

    // Get references to the class block and other block
    var classBlock = document.getElementById('recipe');
    var headerBlock = document.getElementById('header');
    var bottomBlock = document.getElementById('bottom');

    // Calculate the desired height
    var windowHeight = window.innerHeight;
    var headerBlockHeight = headerBlock.offsetHeight;
    var bottomBlockHeight = bottomBlock.offsetHeight;
    // var classBlockHeight = windowHeight - headerBlockHeight - bottomBlockHeight - classBlock.style.paddingTop - classBlock.style.paddingBottom;
    var classBlockHeight = windowHeight - headerBlockHeight - bottomBlockHeight;
    console.log(windowHeight)
    console.log(headerBlockHeight)
    console.log(bottomBlockHeight)
    console.log(classBlockHeight)

    // Set the height of the class block
    classBlock.style.height = classBlockHeight + 'px';

    var sectionInfoBlock = document.getElementById('sectioninfo')
    var ingredientRecipeBlock = document.getElementById('sectioningredientrecipe')

    var sectionInfoBlockHeight = sectionInfoBlock.offsetHeight;
    // var ingredientlistinnerboxBlockPadding = ingredientRecipeBlock.style.paddingTop;
    var ingredientlistinnerboxBlockPadding = parseInt(window.getComputedStyle(ingredientRecipeBlock).getPropertyValue('padding-top'));
    var ingredientRecipeBlockHeight = classBlockHeight - sectionInfoBlockHeight - ingredientlistinnerboxBlockPadding;

    console.log(sectionInfoBlockHeight)
    console.log(ingredientlistinnerboxBlockPadding)
    console.log(ingredientRecipeBlockHeight)

    ingredientRecipeBlock.style.height = ingredientRecipeBlockHeight + 'px';

    var ingredienttitleinnerboxBlock = document.getElementById('ingredienttitleinnerbox')
    var ingredientlistinnerboxBlock = document.getElementById('ingredientlistinnerbox')

    var ingredienttitleinnerboxBlockHeight = ingredienttitleinnerboxBlock.offsetHeight;
    var ingredientlistinnerboxBlockHeight = ingredientRecipeBlockHeight - ingredienttitleinnerboxBlockHeight - 20;

    ingredientlistinnerboxBlock.style.height = ingredientlistinnerboxBlockHeight + 'px';

    var recipetitleinnerboxBlock = document.getElementById('recipetitleinnerbox')
    var recipelistinnerboxBlock = document.getElementById('recipelistinnerbox')

    var recipetitleinnerboxBlockHeight = recipetitleinnerboxBlock.offsetHeight;
    var recipelistinnerboxBlockHeight = ingredientRecipeBlockHeight - recipetitleinnerboxBlockHeight - 20;

    recipelistinnerboxBlock.style.height = recipelistinnerboxBlockHeight + 'px';

    $('h3').textfill({
        maxFontPixels: 60,
        explicitWidth: 1460
        // explicitHeight: 1460
    });
});