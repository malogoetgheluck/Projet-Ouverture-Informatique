import ast
import pygame

class Background:

    def init(save):
        if save == "continue":
            with open("save_data.txt", 'r') as fichier:
                (data_brutes_salles,data_brute_depart) = fichier.read().split("&")
                Background.data_salles = ast.literal_eval(data_brutes_salles.replace("\n","").replace("                ",""))
                Background.data_depart = ast.literal_eval(data_brute_depart)
        elif save == "begin":
            with open("departure_data.txt", 'r') as fichier:
                (data_brutes_salles,data_brute_depart) = fichier.read().split("&")
                Background.data_salles = ast.literal_eval(data_brutes_salles)
                Background.data_depart = ast.literal_eval(data_brute_depart)

    
    #def get_salles_data(self,new_salles):
        #Renvoie le dictionnaire correspondant a la salle demandée
        #return(self.data_salles[new_salles])

    def save(current_salle, current_position, bool_sword, id_key):
        #Sauvegarde

        data_new_depart = {}
        data_new_depart["Salle"] = current_salle
        data_new_depart["Position"] = current_position
        data_new_depart["Epee"] = bool_sword
        data_new_depart["Clees"] = id_key

        f = open("save_data.txt", 'w')
        f.write(str(Background.data_salles)+"&"+str(data_new_depart)) # data_new_depart contient les nouvelles positions de départ du joueur
        f.close()

        # f2 = open("save_info.txt", 'w') #On crée un second fichier pour sauvegarder les données de save_data.txt
        # with open("save_data.txt", 'r') as fichier:
        #     DATA = ast.literal_eval(fichier.read().split("&")[0].replace("\n","").replace("                ",""))
        # f2.write(str(DATA))
        # f2.close()
    
        

#with open("departure_data.txt", 'r') as fichier:
#    DATA = ast.literal_eval(fichier.read().split("&")[0].replace("\n","").replace("                ",""))
#print(DATA["Salle_014"])
#print(type(DATA))
#print(type(ast.literal_eval("{'foo' : 'bar', 'hello' : 'world'}")))