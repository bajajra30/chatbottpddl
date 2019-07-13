# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:51:53 2019

@author: srishti
"""

import chatterbot
from chatterbot import ChatBot
import re
from chatterbot.comparisons import levenshtein_distance
from chatterbot.comparisons import SynsetDistance



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
                  #storage_adapter='chatterbot.storage.SQLStorageAdapter',
              
    logic_adapters=[
        #{
         #   'import_path': 'chatterbot.logic.BestMatch'
        #},
    
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
    

    
while True:
    bot_input1=input("Enter text : ")
    bot_input=clean_text(bot_input1)
    if(bot_input=="bye"):
        print("byebye")
        break
    bot_output = bot.get_response(bot_input)
    print(bot_output)  