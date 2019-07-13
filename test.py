# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 05:32:33 2019

@author: srishti
"""

import requests
import uuid
import json
import flask
import os
from werkzeug import secure_filename
import sqlite3
from sqlite3 import Error


with sqlite3.connect("golu.db") as conn:
    con=conn.cursor()
    ca=1
    name="rahul"
    issue="ok"
    contact=2384894891
    email="shu@jsk.cjd"
    result=con.execute("INSERT INTO agent(ca,name,issue,contact,email) VALUES(?,?,?,?,?)",[ca,name,issue,contact,email])
                        
        
  



