// Get references to the class block and other block
var classBlock = document.getElementById('recipe');
var headerBlock = document.getElementById('header');
var bottomBlock = document.getElementById('bottom');

// Calculate the desired height
var windowHeight = window.innerHeight;
var headerBlockHeight = headerBlock.offsetHeight;
var bottomBlockHeight = bottomBlock.offsetHeight;
// var classBlockHeight = windowHeight - headerBlockHeight - bottomBlockHeight - classBlock.style.paddingTop - classBlock.style.paddingBottom;
var classBlockHeight = windowHeight - headerBlockHeight - bottomBlockHeight - 60 - 60;

// Set the height of the class block
classBlock.style.height = classBlockHeight + 'px';

var sectionInfoBlock = document.getElementById('sectioninfo')
var ingredientRecipeBlock = document.getElementById('sectioningredientrecipe')

var sectionInfoBlockHeight = sectionInfoBlock.offsetHeight;
var ingredientRecipeBlockHeight = classBlockHeight - sectionInfoBlockHeight;

ingredientRecipeBlock.style.height = ingredientRecipeBlockHeight + 'px';

var ingredienttitleinnerboxBlock = document.getElementById('ingredienttitleinnerbox')
var ingredientlistinnerboxBlock = document.getElementById('ingredientlistinnerbox')

var ingredienttitleinnerboxBlockHeight = ingredienttitleinnerboxBlock.offsetHeight;
var ingredientlistinnerboxBlockHeight = ingredientRecipeBlockHeight - ingredienttitleinnerboxBlockHeight - 40;

ingredientlistinnerboxBlock.style.height = ingredientlistinnerboxBlockHeight + 'px';
