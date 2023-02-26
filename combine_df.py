import pandas as pd
import numpy as np


def combine(img_list, points_list, csv_output=False):

    # Identification des images sans défauts en comparant les deux listes précédentes

    img_no_defect = img_list.copy()

    for defect in points_list.file_name:

        img_no_defect.drop(img_no_defect[img_no_defect['file_name'] == defect].index, inplace = True)

    img_no_defect = img_no_defect.reset_index(drop=True)


    # Création d'un dataframe avec valeurs à 0 pour les images sans défauts

    zeros = pd.DataFrame(np.zeros(len(img_no_defect), dtype=int))

    img_no_defect = pd.concat([img_no_defect, zeros, zeros, zeros, zeros, zeros], axis=1, ignore_index=True)

    img_no_defect.columns = points_list.columns


    # Concaténation des 2 dataframes pour obtenir une liste des défauts comprenant les images à 0 défauts

    img_list_concat = pd.concat([points_list, img_no_defect], ignore_index=True)

    def_yn = [int(d > 1) for d in img_list_concat.defect_numb]

    def_yn = pd.DataFrame(def_yn, dtype=int)

    img_list_final = pd.concat([img_list_concat, def_yn], axis=1, ignore_index=True)

    col_names = img_list_concat.columns.to_list()

    col_names.append('defect')

    img_list_final.columns = col_names

    if csv_output:
        img_list_concat.to_csv('full_defect_list.csv', index=False)

    return img_list_final