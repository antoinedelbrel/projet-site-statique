import markdown2
import argparse
import os


parser = argparse.ArgumentParser(description="Markdown to HTML")
parser.add_argument('i','--input', type = str, required = True, metavar = '', help = 'dossier contenant les fichiers markdown à convertir en html')
parser.add_argument('-o','--output',type = str, required = True, metavar = '', help='dossier où seront mis les fichiers html crée pour le site statique')


args = parser.parse_args()




