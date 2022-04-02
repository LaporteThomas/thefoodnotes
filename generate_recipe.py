
from os import path

def create_html_recipe(recipe, sectionId, color):
    if path.isfile("./recette/" + sectionId + "/" + recipe.namefile + ".html") == False:
        f = write_head("./recette/" + sectionId + "/" + recipe.namefile, color)
        write_title(f, recipe.name, color)
        write_info(f, recipe.infos, color)
        write_ingredient_info(f, recipe.ingredient, color)
        write_recipe_step(f, recipe.step, color)
        end_html(f, recipe.source)
        f.close()

def write_head(recipe, color):
    f = open(recipe + ".html", "w")
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"en\">\n\n")

    f.write("\t<!-- Basic -->\n")
    f.write("\t<meta charset=\"utf-8\">\n")
    f.write("\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\n")   
   
    f.write("\t<!-- Mobile Metas -->\n")
    f.write("\t<meta name=\"viewport\" content=\"width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no\">\n\n")
 
    f.write("\t<!-- Site Metas -->\n")
    f.write("\t<title>les recettes.</title>\n")  
    f.write("\t<meta name=\"keywords\" content=\"\">\n")
    f.write("\t<meta name=\"description\" content=\"\">\n")
    f.write("\t<meta name=\"author\" content=\"\">\n\n")

    f.write("\t<!-- Site Icons -->\n")
    f.write("\t<link rel=\"shortcut icon\" href=\"images/favicon.ico\" type=\"image/x-icon\" />\n")
    f.write("\t<link rel=\"apple-touch-icon\" href=\"images/apple-touch-icon.png\">\n\n")

    f.write("\t<!-- Site CSS -->\n")
    f.write("\t<link rel=\"stylesheet\" href=\"../../style_recipe.css\">\n")
    f.write("\t<!-- Responsive CSS -->\n")
    f.write("\t<link rel=\"stylesheet\" href=\"../../css/responsive_recipe.css\">\n\n")

    f.write("</head>\n")

    return f

def write_title(f, name, color):
    f.write("<body>\n\n")

    f.write("\t<div class=\"box\">\n")
    f.write("\t\t<div id=\"header\" class=\"header\">\n")
    f.write("\t\t\t<div class=\"container-header\">\n")
    f.write("\t\t\t\t<h3> <a href=\"../../index.html\">" + name + "<span style=\"color:#" + color + ";\">.</span></a></h3>\n")
    f.write("\t\t\t</div>\n")
    f.write("\t\t</div>\n\n")

def write_info(f, infos, color):
    f.write("\t\t<div class=\"box-recipe\">\n")
    f.write("\t\t\t<div class=\"section-info\">\n")
    f.write("\t\t\t\t<div class=\"container-info\" style=\"background-color: #" + color + ";\">\n")
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
    f.write("\t\t\t\t\t\t<div class=\"container-inner-box\">\n")
    f.write("\t\t\t\t\t\t\t<h2>" + info_type + "</h2>\n")
    f.write("\t\t\t\t\t\t\t<p>" + info_quantity + "</p>\n")
    f.write("\t\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t\t</div>\n")


def write_ingredient_info(f, ingredient, color):
    f.write("\t\t\t<div class=\"section-ingredient\">\n")
    f.write("\t\t\t\t<div class=\"container-ingredient\">\n")
    f.write("\t\t\t\t\t<div class=\"ingredient-title-inner-box\">\n")
    f.write("\t\t\t\t\t\t<h2>les ingrédients<span style=\"color:#" + color + ";\">.</span></h2>\n")
    f.write("\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t\t<div class=\"ingredient-list-inner-box\">\n")
    f.write("\t\t\t\t\t\t<ul>\n")

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
    f.write("\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t</div>\n")
    f.write("\t\t\t</div>\n")

def write_recipe_step(f, recipe_step, color):
    f.write("\t\t\t<div class=\"section-recipe\">\n")
    f.write("\t\t\t\t<div class=\"container-recipe\">\n")
    f.write("\t\t\t\t\t<div class=\"recipe-title-inner-box\">\n")
    f.write("\t\t\t\t\t\t<h2>la recette<span style=\"color:#" + color + ";\">.</span></h2>\n")
    f.write("\t\t\t\t\t</div>\n")
    f.write("\t\t\t\t\t<div class=\"recipe-list-inner-box\">\n")
    f.write("\t\t\t\t\t\t<ol>\n")

    for step in recipe_step:
        f.write("\t\t\t\t\t\t\t<li><span style=\"font-weight:400;\">" + step + "</span></li>\n")
    
    f.write("\t\t\t\t\t\t</ol>\n")
    f.write("\t\t\t\t\t</div><!-- end container -->\n")
    f.write("\t\t\t\t</div><!-- end section -->\n")
    f.write("\t\t\t</div>\n")
    f.write("\t\t</div>\n")
    f.write("\t</div>\n")

def end_html(f, source):
    # if source != "":
    #     f.write("\t<p>source : " + source + "</p>\n\n")
    f.write("\t<!-- ALL JS FILES -->\n")
    f.write("\t<script src=\"../../js/all.js\"></script>\n")

    f.write("</body>\n")
    f.write("</html>\n")
