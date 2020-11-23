import re

def surligner_entitees_nommes(entite, texte_decode_tab):
    if entite.text not in texte_decode_tab:
        #print(entite.text)
        #print('Not Found')
        if " " in entite.text:
            #print("boucle for")
            mot_split_tab=[]
            for x in re.split(" |, |\. |\n",entite.text):
                mot_split_tab.append(x)
            chaine_crée=""
            i=0
            for mot in texte_decode_tab:
                i=i+1
                #print("\n")
                #print("mot_split_tab")
                #print(mot_split_tab)
                #print("CHAINE CREE")
                #print(chaine_crée)
                #print('mot')
                #print(mot)
                #print(mot.replace("' ",""))

                mot_avec_css="<b style='color:red'>"+mot_split_tab[0]+"</b>"
                #print("mot_avec_css")
                #print(mot_avec_css)
                #print("entite.text_split")
                #print(mot != mot_split_tab[0] and mot != mot_avec_css)
                if mot != mot_split_tab[0] and mot != mot_avec_css:
                    chaine_crée = chaine_crée + mot
                else:
                    #print("-------------------ENTITE_TEXT TROUVE--------------------")
                    taille_mot_split_tab=len(mot_split_tab);
                    taille=i-2
                    bool="true"
                    for n in range(taille_mot_split_tab):
                        taille=taille+1
                        #print("mot_split_tab[n]")
                        #print(mot_split_tab[n])
                        #print("texte_decode_tab[taille]")
                        #print(texte_decode_tab[taille])
                        mot_avec_css="<b style='color:red'>"+mot_split_tab[n]+"</b>"
                        if(texte_decode_tab[taille] != mot_split_tab[n] and texte_decode_tab[taille] != mot_avec_css):
                            bool="false"
                        else:
                            texte_decode_tab[taille]="<b style='color:red'>"+texte_decode_tab[taille]+"</b>"
                            #print("BIEN JOUE")

                    #print(texte_decode_tab[i-1])
                    #print(texte_decode_tab[i])
                    #print(texte_decode_tab[i+1])
                    #if texte_decode_tab[i+1] == mot_split_tab[0]:
                    #    print("bien")
    else:
        #print("Found")
        #print(texte_decode_tab.index(entite.text))
        texte_decode_tab[texte_decode_tab.index(entite.text)]="<b style='color:red'>"+entite.text+"</b>"

def switch_demo(argument):
    switcher = {
        "text1": "Lettre des dirigeants de Cronstadt au chef blanc Grimm",
        "text2": "À quoi sert l’autorité ?",
        "text3": "Carnet de guerre 1914-1915 de Louis Doisy",
        "text4": "Français, reprenez le pouvoir !",
        "text5": "La Lutte contre l’État",
        "text6": "Le Journal de la Huronne La Houille rouge Juillet 1918",
        "text7": "Le Salut par les Juifs Chapitre 1",
        "text8": "Lettre à Monsieur Frédéric Masson"
    }
    return switcher.get(argument, "Mauvais titre donné")
