
from os import path
from pathlib import Path

def create_html_recipe(recipe, sectionId, color, recipePrevious, recipeNext):
    if path.isfile("./recette/" + sectionId + "/" + recipe.namefile + ".html") == False:
        f = write_head("./recette/" + sectionId + "/" + recipe.namefile)
        write_title(f, recipe.name, sectionId)
        write_info(f, recipe.infos, color)
        write_ingredient_info(f, recipe.ingredient, color)
        write_recipe_step(f, recipe.step, color)
        write_following_recipe(f, sectionId, recipePrevious, recipeNext, color)
        end_html(f, recipe.source)
        f.close()

def write_head(recipe):
    filename_path = Path(recipe + ".html")
    filename_path.parent.mkdir(parents=True, exist_ok=True)
    f = open(filename_path, "w", encoding='utf-8', errors='ignore')
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"en\">\n\n")

    f.write("\t<!-- Basic -->\n")
    f.write("\t<meta charset=\"utf-8\">\n")
    f.write("\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\n")   
   
    f.write("\t<!-- Mobile Metas -->\n")
    f.write("\t<meta name=\"viewport\" content=\"width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no\">\n\n")
 
    f.write("\t<!-- Site Metas -->\n")
    f.write("\t<title>the food notes.</title>\n")  
    f.write("\t<meta name=\"keywords\" content=\"\">\n")
    f.write("\t<meta name=\"description\" content=\"\">\n")
    f.write("\t<meta name=\"author\" content=\"\">\n\n")

    f.write("\t<!-- Site Icons -->\n")
    f.write("\t<link rel=\"shortcut icon\" href=\"images/favicon.ico\" type=\"image/x-icon\" />\n")
    f.write("\t<link rel=\"apple-touch-icon\" href=\"images/apple-touch-icon.png\">\n\n")

    f.write("\t<!-- Site CSS -->\n")
    f.write("\t<link rel=\"stylesheet\" href=\"../../style_recipe.css\">\n")
    f.write("\t<!-- Responsive CSS -->\n")
    f.write("\t<!-- <link rel=\"stylesheet\" href=\"../../css/responsive_recipe.css\"> -->\n\n")

    f.write("</head>\n")

    return f

def write_title(f, name, sectionId):
    ptitdej_text = "<span style=\"font-weight:900;\">p'tit-déj</span>" if sectionId == "ptitdej" else "p'tit-déj"
    gouter_text = "<span style=\"font-weight:900;\">goûter</span>" if sectionId == "gouter" else "goûter"
    apero_text = "<span style=\"font-weight:900;\">apéro</span>" if sectionId == "apero" else "apéro"
    plat_text = "<span style=\"font-weight:900;\">plats</span>" if sectionId == "plat" else "plats"
    dessert_text = "<span style=\"font-weight:900;\">desserts</span>" if sectionId == "dessert" else "desserts"
    
    f.write("<body>\n\n")

    f.write("\t<div class=\"box\">\n")
    f.write("\t\t<div class=\"box-header\">\n")
    f.write("\t\t\t<div class=\"section-title\">\n")
    f.write("\t\t\t\t<div class=\"container-title\">\n")
    f.write("\t\t\t\t\t<ul class=\"list-title\">\n")
    f.write("\t\t\t\t\t\t<li><a href=\"../../index.html#recipe-ptitdej-container\"><button id=\"ptitdej\" class=\"inner-box-title\">" + ptitdej_text + "</button></a></li>\n")
    f.write("\t\t\t\t\t\t<li><a href=\"../../index.html#recipe-gouter-container\"><button id=\"gouter\" class=\"inner-box-title\">" + gouter_text + "</button></a></li>\n")
    f.write("\t\t\t\t\t\t<li><a href=\"../../index.html#recipe-apero-container\"><button id=\"apero\" class=\"inner-box-title\">" + apero_text + "</button></a></li>\n")
    f.write("\t\t\t\t\t\t<li><a href=\"../../index.html#recipe-plat-container\"><button id=\"plat\" class=\"inner-box-title\">" + plat_text + "</button></a></li>\n")
    f.write("\t\t\t\t\t\t<li><a href=\"../../index.html#recipe-dessert-container\"><button id=\"dessert\" class=\"inner-box-title\">" + dessert_text + "</button></a></li>\n")
    f.write("\t\t\t\t\t</ul>\n")
    f.write("\t\t\t\t</div>\n")
    f.write("\t\t\t</div>\n")
    f.write("\t\t</div>\n\n")

    f.write("\t\t<div class=\"container-list-title\">\n")
    f.write("\t\t\t<h1></span  id=\"title-list\">" + name.upper() + "</span></h1>\n")
    f.write("\t\t</div>\n\n")

def write_info(f, infos, color):
    f.write("\t\t<div id=\"recipe\" class=\"box-recipe\">\n")
    f.write("\t\t\t<div id=\"sectioninfo\" class=\"section-info\">\n")
    f.write("\t\t\t\t<div class=\"container-info\">\n")
    for index, (key, value) in enumerate(infos.items()):
            write_block_info(f, key, value)
    
    if len(infos) < 4:
        for i in range(4-len(infos)):
            f.write("\t\t\t\t\t<div class=\"infos-inner-box\">\n")
            f.write("\t\t\t\t\t</div>\n")

    f.write("\t\t\t\t</div><!-- end container -->\n")
    f.write("\t\t\t</div><!-- end section -->\n\n")

def write_block_info(f, info_type, info_quantity):
    f.write("\t\t\t\t\t<div class=\"infos-inner-box\">\n")
    f.write("\t\t\t\t\t\t<p><span style=\"font-family: Climate Crisis;\">" + info_type.upper() + "</span><br>" + info_quantity.capitalize() + "</p>\n")
    f.write("\t\t\t\t\t</div>\n")


def write_ingredient_info(f, ingredient, color):
    f.write("\t\t\t<div id=\"sectioningredientrecipe\" class=\"section-ingredient-recipe\">\n")
    f.write("\t\t\t\t<div class=\"section-ingredient\">\n")
    f.write("\t\t\t\t\t<div id=\"ingredienttitleinnerbox\" class=\"ingredient-title-inner-box\">\n")
    f.write("\t\t\t\t\t\t<h2>ingrédients</h2>\n")
    f.write("\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t\t\t<ul id=\"ingredientlistinnerbox\" class=\"ingredient-list-inner-box\">\n")

    nb_ingredient = 0
    for list_ingredient in ingredient:
        for key, value in list_ingredient.items():
            if key == "title":
                if nb_ingredient == 0:
                    f.write("\t\t\t\t\t\t\t<li>" + value + "<span style=\"font-weight:700;color:#" + color + ";\">.</span></li>\n")
                    nb_ingredient += 1
                else:
                    f.write("\t\t\t\t\t\t\t<li style=\"padding-top:25px;\">" + value + "<span style=\"font-weight:700;color:#" + color + ";\">.</span></li>\n")
                    nb_ingredient += 1
            else:
                f.write("\t\t\t\t\t\t\t<li>" + value + "<span style=\"font-weight:400;\"> " + key + "</li>\n")
                nb_ingredient += 1
    
    f.write("\t\t\t\t\t\t</ul>\n")
    f.write("\t\t\t\t</div>\n")

def write_recipe_step(f, recipe_step, color):
    f.write("\t\t\t\t<div class=\"section-recipe\">\n")
    f.write("\t\t\t\t\t<div id=\"recipetitleinnerbox\" class=\"recipe-title-inner-box\">\n")
    f.write("\t\t\t\t\t\t<h2>recette</h2>\n")
    f.write("\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t\t<ol class=\"recipe-list-inner-box\" id=\"recipelistinnerbox\">\n")

    for step in recipe_step:
        f.write("\t\t\t\t\t\t<li><span style=\"font-weight:400;\">" + step + "</span></li>\n")
    
    f.write("\t\t\t\t\t</ol>\n")
    f.write("\t\t\t\t</div>\n")
    f.write("\t\t\t</div>\n")
    f.write("\t\t</div>\n")

def write_following_recipe(f, sectionId, recipePrevious, recipeNext, color):
    f.write("\t\t<div class=\"section-list-recipe\" id=\"bottom\">\n")
    f.write("\t\t\t<div class=\"container-list-recipe\">\n")
    f.write("\t\t\t\t<a class=\"recipe-previous recipe-" + sectionId + "\" href=\"./" + recipePrevious.namefile + ".html\">\n")
    f.write("\t\t\t\t\t<h2>🞀 "+ recipePrevious.name + "<span style=\"color:#" + color + ";\">.</span></h2>\n")
    f.write("\t\t\t\t</a>\n")
    f.write("\t\t\t\t<a class=\"recipe-next recipe-" + sectionId + "\" href=\"./" + recipeNext.namefile + ".html\">\n")
    f.write("\t\t\t\t\t<h2>"+ recipeNext.name + "<span style=\"color:#" + color + ";\">.</span> 🞂</h2>\n")
    f.write("\t\t\t\t</a>\n")
    f.write("\t\t\t</div><!-- end section -->\n")
    f.write("\t\t</div>\n")
    f.write("\t</div>\n")

def end_html(f, source):
    # if source != "":
    #     f.write("\t<p>source : " + source + "</p>\n\n")
    f.write("\t<!-- ALL JS FILES -->\n")
    f.write("\t<script src=\"../../js/all.js\"></script>\n")
    f.write("\t<script src=\"../../js/js_recipe.js\"></script>\n")

    f.write("\t<script src=\"../../js/jquery.textfill.js\"></script>\n")
    f.write("\t<script src=\"../../js/jquery.textfill.min.js\"></script>\n")


    f.write("</body>\n")
    f.write("</html>\n")
