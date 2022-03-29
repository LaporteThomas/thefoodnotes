import recipe
from operator import attrgetter
import generate_recipe

def initiate_html():
    f = open("index.html", "w")
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
    f.write("\t<link rel=\"stylesheet\" href=\"style.css\">\n")
    f.write("\t<!-- Responsive CSS -->\n")
    f.write("\t<link rel=\"stylesheet\" href=\"css/responsive.css\">\n\n")

    f.write("</head>\n")
    f.write("<body>\n\n")

    f.write("\t<div id=\"header_title\" class=\"header_title\">\n")
    f.write("\t\t<div class=\"container_header_title\">\n")
    f.write("\t\t\t<img src=\"./images/lesrecettesdetooba.svg\" style =\"height:50%;margin:auto\">\n")
    # f.write("\t\t\t<h3>les recettes de tooba.</h3>\n")
    f.write("\t\t</div>\n")
    f.write("\t</div>\n\n")

    return f

def write_title_section(f, title, id, color, isfirst):
    f.write("\t<button id=\"" + id + "\" class=\"section_title\" style =\"background-color:#" + color + ";\">\n")
    f.write("\t\t<div class=\"container_title\">\n")
    f.write("\t\t\t<h3>" + title + ".</h3>\n")
    f.write("\t\t</div>\n")
    f.write("\t</button>\n\n")

def write_recipe_section(f, sectionId, recipes, color):

    f.write("\t<div id=\"recipe_"+ sectionId + "_container\" class=\"recipe_" + sectionId + "\" style=\"display: none;\">\n")
    f.write("\t\t<div class=\"container_list_recipe\">\n")
    f.write("\t\t\t<ul class=\"recipe-inner-box left\">\n")

    if (len(recipes) % 2) == 0:
        half = int(len(recipes) / 2)
    else:
        half = int(len(recipes) / 2) + 1

    for r in recipes[:half]:
        generate_recipe.create_html_recipe(r, sectionId, color)
        f.write("\t\t\t\t<li><a href=\"./recette/" + sectionId + "/" + r.namefile + ".html\">"+ r.name + "<span style=\"color:#" + color + ";\">.</span></a></li>\n")
    
    f.write("\t\t\t</ul>\n")
    f.write("\t\t\t<ul class=\"recipe-inner-box right\">\n")

    for r in recipes[half:]:
        generate_recipe.create_html_recipe(r, sectionId, color)
        f.write("\t\t\t\t<li><a href=\"./recette/" + sectionId + "/" + r.namefile + ".html\">"+ r.name + "<span style=\"color:#" + color + ";\">.</span></a></li>\n")
    
    f.write("\t\t\t</ul>\n")
    f.write("\t\t</div><!-- end container -->\n")
    f.write("\t</div><!-- end section -->\n\n")

def end_html(f):   
    f.write("\t<!-- ALL JS FILES -->\n")
    f.write("\t<script src=\"js/all.js\"></script>\n")

    f.write("\t<script>\n")
    f.write("\tlet countButtonPtitDej = 0;\n")
    f.write("\tlet countButtonGouter = 0;\n")
    f.write("\tlet countButtonApero = 0;\n")
    f.write("\tlet countButtonPlat = 0;\n")
    f.write("\tlet countButtonDessert = 0;\n")
    f.write("\t$( document ).ready(function() {\n")
    f.write("\t\t$(\"#ptitdej\").on(\"click\",function(){\n")
    f.write("\t\t\t$(\"#recipe_ptitdej_container\").toggle();\n")
    f.write("\t\t\tcountButtonPtitDej += 1;\n")
    f.write("\t\t\tif (countButtonPtitDej % 2 == 0) {\n")
    f.write("\t\t\t\tdocument.getElementById(\"ptitdej\").style.borderRadius = \"25px 25px 25px 25px\";\n")
    f.write("\t\t\t} else {\n")
    f.write("\t\t\t\tdocument.getElementById(\"ptitdej\").style.borderRadius = \"25px 25px 0px 0px\";\n")
    f.write("\t\t\t}\n")
    f.write("\t\t});\n")
    f.write("\t\t$(\"#gouter\").on(\"click\",function(){\n")
    f.write("\t\t\t$(\"#recipe_gouter_container\").toggle();\n")
    f.write("\t\t\tcountButtonGouter += 1;\n")
    f.write("\t\t\tif (countButtonGouter % 2 == 0) {\n")
    f.write("\t\t\t\tdocument.getElementById(\"gouter\").style.borderRadius = \"25px 25px 25px 25px\";\n")
    f.write("\t\t\t} else {\n")
    f.write("\t\t\t\tdocument.getElementById(\"gouter\").style.borderRadius = \"25px 25px 0px 0px\";\n")
    f.write("\t\t\t}\n")
    f.write("\t\t});\n")
    f.write("\t\t$(\"#apero\").on(\"click\",function(){\n")
    f.write("\t\t\t$(\"#recipe_apero_container\").toggle();\n")
    f.write("\t\t\tcountButtonApero += 1;\n")
    f.write("\t\t\tif (countButtonApero % 2 == 0) {\n")
    f.write("\t\t\t\tdocument.getElementById(\"apero\").style.borderRadius = \"25px 25px 25px 25px\";\n")
    f.write("\t\t\t} else {\n")
    f.write("\t\t\t\tdocument.getElementById(\"apero\").style.borderRadius = \"25px 25px 0px 0px\";\n")
    f.write("\t\t\t}\n")
    f.write("\t\t});\n")
    f.write("\t\t$(\"#plat\").on(\"click\",function(){\n")
    f.write("\t\t\t$(\"#recipe_plat_container\").toggle();\n")
    f.write("\t\t\tcountButtonPlat += 1;\n")
    f.write("\t\t\tif (countButtonPlat % 2 == 0) {\n")
    f.write("\t\t\t\tdocument.getElementById(\"plat\").style.borderRadius = \"25px 25px 25px 25px\";\n")
    f.write("\t\t\t} else {\n")
    f.write("\t\t\t\tdocument.getElementById(\"plat\").style.borderRadius = \"25px 25px 0px 0px\";\n")
    f.write("\t\t\t}\n")
    f.write("\t\t});\n")
    f.write("\t\t$(\"#dessert\").on(\"click\",function(){\n")
    f.write("\t\t\t$(\"#recipe_dessert_container\").toggle();\n")
    f.write("\t\t\tcountButtonDessert += 1;\n")
    f.write("\t\t\tif (countButtonDessert % 2 == 0) {\n")
    f.write("\t\t\t\tdocument.getElementById(\"dessert\").style.borderRadius = \"25px 25px 25px 25px\";\n")
    f.write("\t\t\t} else {\n")
    f.write("\t\t\t\tdocument.getElementById(\"dessert\").style.borderRadius = \"25px 25px 0px 0px\";\n")
    f.write("\t\t\t}\n")
    f.write("\t\t});\n")
    f.write("\t});\n")
    f.write("\t</script>\n")

    f.write("</body>\n")
    f.write("</html>\n")

    f.close()

if __name__ == '__main__':
    f = initiate_html()

    list_ptitdej = recipe.sort_list(recipe.read_csv_recipe("ptitdej.csv"))
    # list_ptitdej.sort()
    write_title_section(f, "le petit-déjeuner", "ptitdej", "fec876", True)
    write_recipe_section(f, "ptitdej", list_ptitdej, "fec876")
    
    list_gouter = recipe.sort_list(recipe.read_csv_recipe("gouter.csv"))
    # list_gouter.sort()
    write_title_section(f, "le gouter", "gouter", "ddb792", False)
    write_recipe_section(f, "gouter", list_gouter, "ddb792")

    list_apero = recipe.sort_list(recipe.read_csv_recipe("apero.csv"))
    # list_gouter.sort()
    write_title_section(f, "l'apero", "apero", "d5dd9d", False)
    write_recipe_section(f, "apero", list_apero, "d5dd9d")

    list_plat = recipe.sort_list(recipe.read_csv_recipe("plat.csv"))
    # list_gouter.sort()
    write_title_section(f, "les plats", "plat", "f58c74", False)
    write_recipe_section(f, "plat", list_plat, "f58c74")

    list_dessert = recipe.sort_list(recipe.read_csv_recipe("dessert.csv"))
    # list_gouter.sort()
    write_title_section(f, "les desserts", "dessert", "8ac5ce", False)
    write_recipe_section(f, "dessert", list_dessert, "8ac5ce")
    
    end_html(f)


