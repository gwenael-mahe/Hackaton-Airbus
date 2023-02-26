from os import listdir, getcwd
from os.path import isfile, join

import pandas as pd


# Récupère la liste des noms des images du dossier DB1

def get_img_list(source_folder='\DB1'):

    mypath = getcwd() + source_folder

    img_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    df = pd.DataFrame(img_list)
    df.columns = ['file_name']

    return df


# Récupère le tableau des défauts avec les coordonnées des points

def get_defect_list():

    df = pd.read_csv('DB1_defect_points.csv')

    return df