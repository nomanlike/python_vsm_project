import re
import string
import sys
import os
from os import listdir
from os.path import isfile, join
import PySimpleGUI as sg
from jokes import talks as talks
from config import file_path
from maids_and_butlers import remove_punctuation, words_count, frequency_of_words, word_exist
import random
import copy
#https://github.com/peermohtaram/Vector-Space-Model/blob/master/Vector_Space_Model.ipynb



def readFile(filename):
    filehandle = open(filename, encoding='utf-16-le')
    # https://stackoverflow.com/questions/4190683/python-string-replace-for-utf-16-le-file

    strong = filehandle.read()
    filehandle.close()
    return strong


def query_joke():
    i = random.choice(talks)
    layout = [[sg.Text(i)],
              [sg.InputText(key='textbox')],
              [sg.Button('Ok'), sg.Button('Exit')],
              [sg.Multiline(size=(30, 5))],
              ]
    window = sg.Window(title="18125068\'s query", layout=layout).Finalize()
    event, values = window.read()
    window.close()
    if event in (None, 'Exit'):
        exit(0)
        return
    if values['textbox'] in (None, ''):
        return
    return values['textbox']

while True:
    query = None
    while query is None:
        query = query_joke()

    # clean up the unnecessary things(punctuation) then split the query
    query_clean=remove_punctuation(query)
    query_splice=query_clean.split()
    query_existence=word_exist(query_splice)
    score=[]
    onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]
    #https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory

    #possibe to split query and then check for word existence first!
    #Then score it as -1 if there is no such word
    #if there is, score it as 0 then go up
    for item in onlyfiles:
        take = file_path + '/' + item
        current = readFile(take)
        temp=remove_punctuation(current)
        # split the text
        temp2=temp.split()
        # word existence in text
        temp_exist=word_exist(temp2)
        # how many words? which one exists?
        lord=[]
        counterstrike=0
        for stuff in query_existence:
            if stuff in temp_exist:
                lord.append(1)
                counterstrike+=1
            else:
                lord.append(0)
        #it works with vietnamese too, Don't sweat too much
        if counterstrike>0:
            text_map=words_count(temp2)
            text_copy=copy.deepcopy(text_map)
            text_freq=frequency_of_words(text_copy,len(temp2))

        else:
            score.append(-1)
            #scoring of this data is -1
    layout = [
        [sg.Button('Exit')],
        [sg.Button('Next Query')],
        [sg.Text(size=(30, 20),background_color='white')],
             ]
    window = sg.Window(title="18125068\'s result", layout=layout).Finalize()
    event, value = window.read()
    print(value)
    window.close()
    if event in (None, 'Exit'):
        exit(0)


