#vershtml.py version 1.1.1
from script import surligner_entitees_nommes,switch_demo

import keyword, html,nltk,spacy,re,shlex

header="<!DOCTYPE html><html> <head> <title>Technologie du langage</title><style>.text{text-align:center}h2{text-align:center}</style></head><body>"
intro="<h1 style='text-align:center'>Technologie du langage</h1>"
fin="</pre></code>"

print("Liste des textes : text1, text2, text3, text4, text5, text6, text7, text8")
nom_texte=input("Entrez le nom du texte à analyser : ")
#nom_texte="";
if(nom_texte != ""):
    titre=switch_demo(nom_texte)
    titre_html = "<h2>Titre du texte : '<i>"+titre+"</i>'</h2>"
    texte=open("./Corpus/"+nom_texte+".txt", 'r', encoding='UTF-8')
    print("Analyse en cours...")
    lines = texte.read()
    texte_decode=""
    for ligne in lines:
        texte_decode += ligne;
    #print(texte_decode)
    tokens=nltk.word_tokenize(texte_decode)
    pos_tokens = nltk.pos_tag(tokens)
    phrase_analyse = nltk.ne_chunk(pos_tokens)

    entites_nommees = []
    for arbre in phrase_analyse :
        if hasattr(arbre, 'label') :
            entite_text=' '.join(f[0] for f in arbre.leaves())
            entite_label = arbre.label()
            entites_nommees.append((entite_text, entite_label))
    #print("NLTK\n")

    texte_decode_tab=[]
    for x in re.split(" |, |\. |\n",texte_decode):
        texte_decode_tab.append(x)
    index=0


    tableau_nltk="\n <div class='text'><h2>Résultats obtenus avec NLTK</h2>"
    print("Analyse NLTK\n")
    for EN in entites_nommees :
        tableau_nltk +=(EN[0])+"\n | "+(EN[1])+"<br>"
        #print(EN[0])
        if EN[0] in texte_decode_tab:
            texte_decode_tab[texte_decode_tab.index(EN[0])]="<b style='color:red'>"+EN[0]+"</b>"
    #print("\n")

    #print(texte_decode_tab)

#SPACY : corpus fr_core_news_sm
    modele_SM = spacy.load("fr_core_news_sm")
    document = modele_SM(texte_decode)
    print("Analyse SpaCy en_core_web_sm\n")
    tableau_spacy="\n <h2>Résultats obtenus avec Spacy (fr_core_news_sm)</h2>"
    for entite in document.ents:
        tableau_spacy += entite.text+"\n | "+entite.label_+"<br>"
        surligner_entitees_nommes(entite, texte_decode_tab)

#SPACY : corpus fr_core_news_md
    modele_MD = spacy.load("fr_core_news_md")
    document = modele_SM(texte_decode)
    print("Analyse SpaCy en_core_web_md\n")
    tableau_spacy="\n <h2>Résultats obtenus avec Spacy (fr_core_news_md)</h2>"
    for entite in document.ents:
        tableau_spacy += entite.text+"\n | "+entite.label_+"<br>"
        surligner_entitees_nommes(entite, texte_decode_tab)

#SPACY : corpus fr_core_news_lg
    modele_LG = spacy.load("fr_core_news_lg")
    document = modele_SM(texte_decode)
    print("Analyse SpaCy en_core_web_lg\n")
    tableau_spacy+="\n <h2>Résultats obtenus avec Spacy (fr_core_news_lg)</h2>"
    for entite in document.ents:
        tableau_spacy += entite.text+"\n | "+entite.label_+"<br>"
        surligner_entitees_nommes(entite, texte_decode_tab)

    tableau_spacy += "</div>"
    texte_decode_html=tableau_nltk+tableau_spacy+fin


    fichier=open("analyse_en.htm","w")
    fichier.write(header)
    fichier.write(intro)
    fichier.write(titre_html)
    for listitem in texte_decode_tab:
            fichier.write('%s\n' % listitem)
    fichier.write(texte_decode_html)
    fichier.close()
    print("L'analyse des entites nommées du texte : "+titre+" est prêt dans le fichier analyse_en.htm")
else:
    print("Vous n'avez pas rentré de texte")
