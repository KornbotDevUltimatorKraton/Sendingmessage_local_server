from distutils.log import debug
import socket # Getting the socket to run 
from flask import *
from flask import Flask,flash,json,jsonify,request,current_app,render_template,make_response,url_for,redirect,session,abort,send_from_directory,g # Session input for user 
from werkzeug.exceptions import HTTPException # Werkzeug Web error handlerer library 

Port_sub  = 5000 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
address = "127.0.0.1"

list_path = ['TI_product','NXP_product','ST_product']
list_subpath = ['TI_motor_drive','TI_bms','TI_sensor','NXP_interfaces','NXP_multiplexer','ST_motordriver','ST_sensor','ST_microcontroller']
dict_manufacture = {'TI':'TI_product','NXP':'NXP_product','ST':'ST_product'}
dict_menudoct = {'TI_product':'TI_comdoc','NXP_product':'NXP_comdoc','ST_product':'ST_comdoc'} #component doct
dict_scan_requirement = {'motor':['TI_motor_drive','ST_motor_drive'],'sensors':['TI_sensor','TI_bms'],'mcus':['ST_microcontroller']} 


app = Flask(__name__) 

data_mod = {}
@app.route("/",methods=['GET','POST']) 
def componentsrequire(): 
     if request.method == 'POST': 
          components = request.form['components']
          componentinfo = request.form['componentinfos']
          #requireinfo = request.form['requireinfos'] 
          print(components) 
          print(componentinfo)
          #print(requireinfo)
          #Processing the requirement request here 
          msg = str(components+","+componentinfo)
          sock.sendto(msg.encode('utf-8'),(address,5000))   
          
                           
     return render_template("modify.html")

if __name__=="__main__":
  
      app.run(debug=True,host='0.0.0.0',port=8000)
    




