# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 03:53:27 2019

@author: srishti
"""
import chatterbot
from chatterbot import ChatBot
import re
from chatterbot.comparisons import levenshtein_distance
from chatterbot.comparisons import SynsetDistance
import requests
import uuid
import json
import flask
import os
from werkzeug import secure_filename
import random
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request,redirect,send_from_directory,send_file,jsonify
app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

location=""
def setlocation(link):
    global location
    location=link
    
    

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


    
    

@app.route('/',methods = ['POST', 'GET'])
def hello():
    print("hey")
    return render_template('indexr.html')
    
    

@app.route('/uploaded',methods = ['POST', 'GET'])
def star():
    print("hello")
    null=None
    with sqlite3.connect("golu.db") as conn:
        con=conn.cursor()
        if request.method == 'POST':
            #loc=request.form["loc"]
            #print(loc)
            option = request.form["selectBox1"]
            if option=="Feedback":
                text=request.form['fed']
                print("bye")
                if text=="":
                    print("null")
                else :
                    print("Not null")
                    cursor=con.execute("INSERT INTO feedback(comments) VALUES(?)",[text])
                    return ("Feedback registerd")
           
            elif option=="Complaint":
                print("in complaint")
                option2 = request.form["selectBox2"]
                if(option2=="agent"):
                    print("in agent")
                    ca_no=request.form["ca"]
                    name=request.form["getname"]
                    issue=request.form["issue"]
                    contact=request.form["contact"]
                    email=request.form["email"]
                    lis = con.execute("SELECT CA from general")
                    ca=int(ca_no)
                    for row in lis:
                        print("searching")
                        print(row)
                        print(row[0])
                        print(ca)
                        
                        if row[0] == ca:
                            print(row[0])
                            print(ca)
                            print("found")
                            detail=con.execute("Select Name, Address from general where CA=?",[ca])
                            for row1 in detail:
                                name=row1[0]
                                address=row1[1]
                            result=con.execute("INSERT INTO agent(ca,name,issue,contact,email) VALUES(?,?,?,?,?)",[ca,name,issue,contact,email])
                            return ("CA: "+ca_no+" Owner:  "+name+" Address: "+address+" An agent will soon contact you.")
                    return "Incorrect CA.Please enter again."
                elif option2=="electrician":
                    print("in elec")
                    ca_no=request.form["ca"]
                    name=request.form["getname"]
                    address=request.form["address"]
                    contact=request.form["contact"]
                    email=request.form["email"]
                    
                    check=0
                    option3 = request.form["selectBox3"]
                    if option3=="yes":
                        check=1
                    lis = con.execute("SELECT CA from general")
                    ca=int(ca_no)
                    for row in lis:
                        print("searching")
                        print(row)
                        print(row[0])
                        print(ca)
                        if row[0] == ca:
                            print(row[0])
                            print(ca)
                            print("found")
                            cid=random.randint(100000,999999)
                            print(cid)
                            print(location)
                            id=str(cid)
                            detail=con.execute("Select Name, Address from general where CA=?",[ca])
                            for row1 in detail:
                                name=row1[0]
                                address=row1[1]
                            result=con.execute("INSERT INTO electrician(ca,name,address,contact,email,cid,link) VALUES(?,?,?,?,?,?,?)",[ca,name,address,contact,email,cid,location])
                            return ("CA: "+ca_no+" Owner:  "+name+" Address: "+address+" An electrician will soon contact you."+" COMPLAINT ID : "+id)
                    return "Incorrect CA.Please enter again."
            elif option=="Query":
                return redirect('/bot')
 

@app.route('/bot')
def botty():
    return render_template('home.html')


@app.route('/query',methods = ['POST','GET'])
def hellohey():
    bot_input1=request.form["text"]
    bot_input=clean_text(bot_input1)
    bot_output = str(bot.get_response(bot_input))
    print(bot_output)  
    #return render_template('home.html')
    return jsonify({"status":"success","response":bot_output})

@app.route('/postmethod', methods = ['POST'])
def get_post_javascript_data():
    jsdata = request.form['javascript_data']
    print(jsdata)
    setlocation(jsdata)
    return jsdata
           
                    
                        
        
                
if __name__ == '__main__':
    app.run(debug=True)