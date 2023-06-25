// Get references to the class block and other block
var classBlock = document.getElementById('recipe');
var headerBlock = document.getElementById('header');
var bottomBlock = document.getElementById('bottom');

// Calculate the desired height
var windowHeight = window.innerHeight;
var headerBlockHeight = headerBlock.offsetHeight;
var bottomBlockHeight = bottomBlock.offsetHeight;
var classBlockHeight = windowHeight - headerBlockHeight - bottomBlockHeight;

// Set the height of the class block
classBlock.style.height = classBlockHeight + 'px';

var sectionInfoBlock = document.getElementById('sectionInfo')
var ingredientRecipeBlock = document.getElementById('sectionIngredientRecipe')

var sectionInfoBlockHeight = sectionInfoBlock.offsetHeight;
var ingredientRecipeBlockHeight = classBlockHeight - sectionInfoBlockHeight;

ingredientRecipeBlock.style.height = ingredientRecipeBlockHeight + 'px;'
