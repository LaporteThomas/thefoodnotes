import recipe
from operator import attrgetter
import generate_recipe

def write_head():
    f = open("index.html", "w", encoding='utf-8', errors='ignore')
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
    f.write("\t<link rel=\"stylesheet\" href=\"style.css\">\n")
    f.write("\t<!-- Responsive CSS -->\n")
    f.write("\t<link rel=\"stylesheet\" href=\"css/responsive.css\">\n\n")

    f.write("</head>\n")
    return f

def write_header(f):
    f.write("<body>\n\n")

    f.write("\t<div class=\"box\">\n")
    f.write("\t\t<div class=\"box-header\">\n")
    f.write("\t\t\t<div id=\"header\" class=\"header\">\n")
    f.write("\t\t\t\t<div class=\"container-header\">\n")
    f.write("\t\t\t\t\t<p>the food notes<span id=\"dot-title\">.</span></p>\n")
    f.write("\t\t\t\t</div>\n")
    f.write("\t\t\t</div>\n\n")

def write_section_title(f):
    f.write("\t\t\t<div class=\"section-title\">\n")
    f.write("\t\t\t\t<div class=\"container-title\">\n")
    f.write("\t\t\t\t\t<ul class=\"list-title\">\n")
    f.write("\t\t\t\t\t\t<li><button id=\"ptitdej\" class=\"inner-box-title\">le petit-déjeuner.</button></li>\n")
    f.write("\t\t\t\t\t\t<li><button id=\"gouter\" class=\"inner-box-title\">le goûter.</button></li>\n")
    f.write("\t\t\t\t\t\t<li><button id=\"apero\" class=\"inner-box-title\">l'apéro.</button></li>\n")
    f.write("\t\t\t\t\t\t<li><button id=\"plat\" class=\"inner-box-title\">les plats.</button></li>\n")
    f.write("\t\t\t\t\t\t<li><button id=\"dessert\" class=\"inner-box-title\">les desserts.</button></li>\n")
    f.write("\t\t\t\t\t</ul>\n")
    f.write("\t\t\t\t</div>\n")
    f.write("\t\t\t</div>\n")
    f.write("\t\t</div>\n\n")
    f.write("\t\t<div class=\"box-list\">\n")

def write_recipe_section(f, sectionId, recipes, color):

    if sectionId == "ptitdej":
        f.write("\t\t\t<div id=\"recipe-"+ sectionId + "-container\" class=\"section-recipe recipe-" + sectionId + "\" style=\"display: block;\">\n")
    else:
        f.write("\t\t\t<div id=\"recipe-"+ sectionId + "-container\" class=\"section-recipe recipe-" + sectionId + "\" style=\"display: none;\">\n")
    f.write("\t\t\t\t<div class=\"container-list-recipe\">\n")
    f.write("\t\t\t\t\t<ul class=\"recipe-inner-box\">\n")

    index = 0
    for r in recipes:
        generate_recipe.create_html_recipe(r, sectionId, color, recipes[index - 1], recipes[(index + 1)%len(recipes)])
        index += 1
        f.write("\t\t\t\t\t\t<li><a href=\"./recette/" + sectionId + "/" + r.namefile + ".html\"><span>"+ r.name + "<mark style=\"color:#" + color + ";\">.</mark></span></a></li>\n")

    f.write("\t\t\t\t\t</ul>\n")
    f.write("\t\t\t\t</div><!-- end container -->\n")
    f.write("\t\t\t</div><!-- end section -->\n\n")

def end_html(f):
    f.write("\t\t</div>\n")
    f.write("\t</div>\n\n")

    f.write("\t<!-- ALL JS FILES -->\n")
    f.write("\t<script src=\"js/all.js\"></script>\n\n")
    f.write("\t<script src=\"js/custom.js\"></script>\n\n")
    f.write("\t<script src=\"js/jquery.textfill.js\"></script>\n\n")
    f.write("\t<script src=\"js/jquery.textfill.min.js\"></script>\n\n")

    f.write("</body>\n")
    f.write("</html>\n")

    f.close()

if __name__ == '__main__':
    f = write_head()
    write_header(f)
    write_section_title(f)

    list_ptitdej = recipe.sort_list(recipe.read_csv_recipe("ptitdej.csv"))
    write_recipe_section(f, "ptitdej", list_ptitdej, "fec876")
    
    list_gouter = recipe.sort_list(recipe.read_csv_recipe("gouter.csv"))
    write_recipe_section(f, "gouter", list_gouter, "ddb792")

    list_apero = recipe.sort_list(recipe.read_csv_recipe("apero.csv"))
    write_recipe_section(f, "apero", list_apero, "d5dd9d")

    list_plat = recipe.sort_list(recipe.read_csv_recipe("plat.csv"))
    write_recipe_section(f, "plat", list_plat, "f58c74")

    list_dessert = recipe.sort_list(recipe.read_csv_recipe("dessert.csv"))
    write_recipe_section(f, "dessert", list_dessert, "8ac5ce")
    
    end_html(f)


