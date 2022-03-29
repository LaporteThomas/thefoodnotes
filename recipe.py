import csv
import generate_recipe
from operator import attrgetter

class Recipe:

    def __init__(self, name="", namefile = "", source = "", infos=dict(), ingredient=list(), step=list()):
      self.name = name
      self.namefile = namefile
      self.infos = infos
      self.ingredient = ingredient
      self.step = step
      self.source = source

    def __str__(self):
        s = "Nom: %s\n" % (self.name)
        s += "File: %s.html\n" % (self.namefile)
        s += "Infos:\n"
        for element in self.infos.keys():
            s += "\t%s %s\n" % (element, self.infos[element])
        s += "Ingredients:\n"
        for liste_ingredient in self.ingredient:
            for element in liste_ingredient.keys():
                if liste_ingredient[element]!="":
                    s += "\t%s %s\n" % (liste_ingredient[element], element)
                else:
                    s += "\t%s\n" % (element)
            s += "\n"
        s += "Etapes:\n"
        for element in self.step:
            s += "\t%s\n" % (element)
        return s

    def __repr__(self):
        return '{' + self.name + ', ' + self.namefile + '}'
    
    def __lt__(self, other):
        return self.namefile < other.namefile

def sort_list(list_recipe):
    for iter_num in range(len(list_recipe)-1,0,-1):
            for idx in range(iter_num):
                if list_recipe[idx]>list_recipe[idx+1]:
                    temp = list_recipe[idx]
                    list_recipe[idx] = list_recipe[idx+1]
                    list_recipe[idx+1] = temp
    
    return list_recipe

def read_csv_recipe(filename):
    list_recipe = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        line_count = 0
        name=""
        namefile=""
        source=""
        infos = dict()
        list_ingredient = list(dict())
        ingredient = dict()
        step = list()
        for row in spamreader:
            if row_is_empty(row):
                list_ingredient.append(ingredient)
                list_recipe.append(Recipe(name, namefile, source, infos, list_ingredient, step))
                name=""
                namefile=""
                source=""
                infos = dict()
                ingredient = dict()
                list_ingredient = list(dict())
                step = list()
                line_count = 0
            else:
                if line_count == 0:
                    name = row[0]
                    namefile = row[1]
                    source = row[2]
                    line_count += 1
                else:
                    if row[0] != "" or row[1] != "":
                        infos[row[0]] = row[1]

                    if row[2] != "" and row[3] == "":
                        if line_count != 1:
                            list_ingredient.append(ingredient)
                            ingredient = dict()
                        ingredient["title"] = row[2]
                    elif row[2] != "" or row[3] != "":
                        ingredient[row[3]] = row[2]

                    if row[4] != "":
                        step.append(row[4])
                    line_count += 1

        list_ingredient.append(ingredient)
        list_recipe.append(Recipe(name, namefile, source, infos, list_ingredient, step))
    
    return list_recipe

def row_is_empty(row):
    for r in row:
        if r != "":
            return False
    
    return True

# if __name__ == '__main__':
#     list_recipe = read_csv_recipe("gouter.csv")
#     sort_list(list_recipe)
#     for r in list_recipe:
#             print(r)