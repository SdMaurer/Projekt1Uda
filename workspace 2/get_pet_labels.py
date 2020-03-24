#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Solmaz RahimiMaurer
# DATE CREATED:                  15.03.2020                
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

#filename_list = listdir("pet_images/")
#filename_list = listdir("uploaded_images/")

#print("\nPrints 10 filenames from folder pet_images/")
#for idx in range(0, 10, 1):
#for idx in range(0, 4, 1):
#    print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
   # image_dir=''.join(map(str, filename_list)) #change list to string
#print(image_dir)


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
#def get_pet_labels(image_dir):
# 
def get_pet_labels(image_dir):
    in_files = listdir(image_dir)
    
    results_dic=dict()
    
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
           
            
            #file_name = os.path.splitext(filename_list[idx])[0]
            
            file_name = in_files[idx].split("_")
            
            
            
            pet_name=""
            
            for word in file_name:
                if word.isalpha():
                    pet_name +=word + " "
            pet_name=pet_name.strip() . lower()
            
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_name]
            else:
                print("** Warning: Key=", filenames[idx],
                      "already exists in results_dic with value =",
                      results_dic[filenames[idx]])
                print("\nPrinting all key-value pairs in dictionary results_dic:")
                for key in results_dic:
                    print("Filename=", key, "   Pet Label=", results_dic[key])
            
    #word_list_pet_image = low_pet_image.split("_")

    return results_dic
#print("\nEmpty Dictionary results_dic - n items=", items_in_dic)
    #return(results_dic)
   
    
    

