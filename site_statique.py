import markdown2
import argparse
import os


parser = argparse.ArgumentParser(description="Markdown to HTML")
parser.add_argument('-i','--input', type = str, required = True, metavar = '', help = 'dossier contenant les fichiers markdown à convertir en html')
parser.add_argument('-o','--output',type = str, required = True, metavar = '', help='dossier où seront mis les fichiers html crée pour le site statique')


args = parser.parse_args()


fichier_md = args.input
dossiers_html = args.output

dossiers = os.listdir(fichier_md)


def converter(fichier_md, dossiers_html) :
    compteur = 0
    for fichiers in dossiers:
        with open (f'{fichier_md}/{fichiers}',"r") as file :
            convert_html = markdown2.markdown(file.read())
            fichier_html = open(f'{dossiers_html}/index{compteur}.html',"w")
            fichier_html.write(convert_html)
            fichier_html.close()
            compteur += 1

converter(fichier_md, dossiers_html)            