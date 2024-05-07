# coding: utf-8

import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from markdownify import markdownify as md

def download_resource(url, path):
    path = Path(path)
    response = requests.get(url)
    fname = url.split('/')[-1]
    with open(path/fname, mode="wb") as file:
        file.write(response.content)

def bootstrap(problem, file_path='.'):
    #problem = 3
    #notebook_dir = Path('D:\Projects\projecteuler\\notebooks')
    if not file_path:
        file_path = '.'
    notebook_dir = Path(file_path)

    #######
    # create folder
    #######
    # get the title for the folder name
    URL = 'https://projecteuler.net/'

    page = requests.get(URL+'problem=' + str(problem))
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find("h2").text

    folder_name = f"{int(problem):04d}_{title.lower().replace(' ','_')}"

    # make a folder with this name
    os.mkdir(notebook_dir/folder_name)



    ######
    # create notebook
    ######

    # make a notebook in that folder
    notebook_dict = dict()
    notebook_dict['cells'] = []

    cell_dict = dict()
    cell_dict['cell_type'] = 'markdown'
    cell_dict['metadata'] = {}
    cell_dict['source'] = []


    page = requests.get(URL+"minimal="+ str(problem))
    intro_text = md(page.text)



    notebook_dict['cells'] = [cell_dict]


        
    #####
    # download resources
    #####

    # search through page.text
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')

    resource_folder = notebook_dir/folder_name/'resources'

    if not resource_folder.exists():
        os.mkdir(resource_folder)
        print("Downloading resources...")
    else:
        print("No resources to download.")


    for link in links:
        resource_name = link['href'].split('/')[-1]
        download_resource(URL+link['href'], resource_folder)
        print(f"Resource '{resource_name}' downloaded!")


    #### 
    # relink resources in the markdown to our resource folder
    ####
    for link in links:
        fname = link['href'].split('/')[-1]

        resource_path = 'resources/' + fname

        intro_text = intro_text.replace(link['href'], resource_path)
        

    # clean up unneccessary text for downloads
    intro_text = intro_text.replace(" (right click and 'Save Link/Target As...')", '')
    # now add the text to the notebook
    cell_dict['source'].append(intro_text)

        
    print(f"Creating notebook at '{notebook_dir.absolute()}'")
    import json
    with open(notebook_dir/folder_name/'notebook.ipynb', 'w') as nb:
        json.dump(notebook_dict,nb, ensure_ascii=False, indent=4)