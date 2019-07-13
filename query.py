# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 07:34:45 2019

@author: srishti
"""

import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os



from chatterbot.comparisons import levenshtein_distance
from chatterbot.comparisons import SynsetDistance

#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
import sqlite3
import json
from datetime import datetime
import csv
# You will have to download the set of stop words the first time
#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#stop_words = stopwords.words('english')
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    return text

bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
              
    logic_adapters=[
        #{
         #   'import_path': 'chatterbot.logic.BestMatch'
        #},
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'I am Srishti Kohli',
            'output_text': 'Welcome Highness. Sir Rahul Bajaj love you da mostest.'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.50,
            "statement_comparison_function": chatterbot.comparisons.SynsetDistance#,
            #"response_selection_method": chatterbot.response_selection.get_first_response
        },
        
        #'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ])

#trainer = ChatterBotCorpusTrainer(bot)
#bot.set_trainer(ListTrainer)

#for files in os.listdir('C:/Users/rbaja/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
#	data = open('C:/Users/rbaja/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files , 'r').readlines()
#	trainer.train(data)
#trainer.train("chatterbot.corpus.english.conversations")
#trainer.train("chatterbot.corpus.english.greetings")
    # Importing the dataset
lines = open('faq23.txt', encoding = 'utf-8', errors = 'ignore').read().split('#####')
trainer=ListTrainer(bot)         
clean_lines=[]          
for _line in lines:
    clean_lines.append(clean_text(_line))
    
for i in range(0,len(clean_lines),2):
    l=[]
    l.append(clean_lines[i])
    l.append(clean_lines[i+1])
    i=i+2
    trainer.train(l)



while True:
    bot_input=input("Enter text : ")
    if(bot_input=="bye"):
        print("byebye")
        break
    bot_output = bot.get_response(bot_input)
    print(bot_output)    
