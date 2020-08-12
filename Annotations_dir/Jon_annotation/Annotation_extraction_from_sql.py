#!/usr/bin/env python
# coding: utf-8

# ## Extracting Sonja's annotation from *.sqlite files

# In[28]:


import sqlite3
from sqlite3 import Error
import subprocess
import os
import shutil



###################Image labels
Quality_labels =['Normal','Blurry','Foreign_object','Empty','Shadow','Corrupted','Other']
Nuclei_labels  =['Normal','Blurry','No_object','Cutoff_object','Not_oval_shape','Micro_Nuclei','Messed_up','Other']
#Cytosol_labels =['Normal','Blurry','No_object','Dots','Small','Cut_off_object','Black_holes','other']
Cytosol_labels =['Normal','Blurry','No_object','Dots','Small','Cut_off','Black_holes','Pale','other']
#Mithocondria_labels =['Normal','Blurry','No_object','Less_granular','Other']
Mithocondria_labels =['Normal','Blurry','No_object','Evenly_spread','Pale','other']




def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def classify_all_images(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT id,first_label FROM annotate_table where first_label!='';")

    rows = cur.fetchall()
    
    
    return rows

def classify_images_each_channel(label_list,rows,channel):
    

    # Directory 
    directory = channel

    # Parent Directory path 
    parent_dir = "./"

    # Path 
    path = os.path.join(parent_dir, directory) 
    if not os.path.isdir(path):  
        os.mkdir(path) 
        print("Directory '%s' created" %directory) 
  
  
  
    for l in label_list:
        parent_dir = "./"+channel+"/"
        directory  = l
        path = os.path.join(parent_dir, directory) 
        if not os.path.isdir(path):  
            os.mkdir(path) 
    
        
    
    for row in rows:
        labels = row[1].split(',')
        for i in range(len(labels)-1):
            original = r'/home/salka/snic2020-6-41/salma_files/ImageProject/data/Web_game_500_each_April_17/static/img/'+row[0]
            target = r'./'+channel+'/'+labels[i]+'/'+row[0]
            shutil.copyfile(original, target)
            #print(row[1],"\n")
        



def main():
    database = "Quality.sqlite"
  
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. labels:")
        classify_images_each_channel(Quality_labels,classify_all_images(conn),'Quality')
#########################################################################
    database = "Nuclei.sqlite"
  
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. labels:")
        classify_images_each_channel(Nuclei_labels,classify_all_images(conn),'Nuclei')
#########################################################################
    database = "Cytosol.sqlite"
  
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. labels:")
        classify_images_each_channel(Cytosol_labels,classify_all_images(conn),'Cytosol')
#########################################################################
    database = "Mitochondria.sqlite"
  
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. labels:")
        classify_images_each_channel(Mithocondria_labels,classify_all_images(conn),'Mitochondria')

        

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




