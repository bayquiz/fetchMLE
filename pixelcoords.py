# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 13:32:59 2022

@author: bayqu
"""
import numpy as np
import ast
import matplotlib.pyplot as plt
from flask import Flask, render_template, make_response, jsonify, request

app = Flask(__name__)
PORT = 3200
HOST = '0.0.0.0'

@app.route("/")
def home():
    return "<h1 style='color:blue'> Fetch MLE Work!!</h1>"

@app.route("/temp")
def template():
    return render_template('index.html')

@app.route("/coords", methods = ['POST'])
def qs():

    dims = request.form['dimensions'] #from the form
    corners = request.form["corners"] #from the form
    # I'm assuming the input is correct....

    answer = run(dims, corners) #run the solving function

    res = make_response(jsonify(answer), 200)
    #res = make_response(jsonify({"error": "No Query String"}), 404)
    return res

def run(dimensions, corners):
            
        # DIMENSIONS: tuple defining heigh and width of the image in pixels
        #   (10, 12) = 10 rows and 12 columns 
        # CORNER POINTS: list of 2 element tuples defining x and y coords of corner
        #   points of the image. Its four (x, y) pairs.
        #   [(1.5, 1.5), (4, 1.5), (1.5, 8), (4.0, 8)]
        # they can be in ANY ORDER: must determine top left,  bottom left, etc
        
        #GOAL: calculate and return x, y coords of placement of pixels so that 
        # they are evenly spaced within the rectangle defined by corner points
        # shape should be m,n,2 : rows, columns, 2
    
        #plt.plot(*map(list, zip(*corners)), 'ko')
        #plt.grid()
        #plt.show()
        dimensions = ast.literal_eval(dimensions) #since its a string from the web
        corners = ast.literal_eval(corners) #since its a string from the web 


        #now we need to determine the orientation of the corners
        newCorners = sorted(corners, key = lambda y: [y[1], y[0]])
        #now we have: bottom left, bottom right, top right, top left
        
        #now we need to evenly space points
        br = [newCorners[0], newCorners[1]] #these are bottom coords
        print("BR: ", br)
        bottomrow = np.linspace(br[0][0], br[1][0], num = dimensions[0]) #this evenly spaces points
        bottomrow = np.around(bottomrow, 2) #rounding to look nice
    
        
        sides = [newCorners[0], newCorners[2]] # these are left side coords
        siderow = np.linspace(sides[0][1], sides[1][1], num = dimensions[1]) #evenly spacing points
        siderow = np.around(siderow, 2) #rounding to look nice
        
        xx, yy = np.meshgrid(bottomrow, siderow) #meshgrid to create rectangle
        #plt.plot(xx, yy, 'ko')
        #plt.show()
    
        idk = [[a_, b_] for a_, b_ in zip(xx.flatten(), yy.flatten())] #getting the proper coordinate formatting
        
        #now get the proper shape
        done = [idk[i:i + dimensions[0]] for i in range(0, len(idk), dimensions[0])] #making it look pretty
        #print(done)
        return done


############################################
# TESTING FUNCTIONALITY
###########################################
"""
dims = (3,3)
corners = [(1,3), (1, 1), (3,3), (3,1)]
#call function
run(dims, corners)
dims2 = (10, 12)
corners2 = [ (1.5, 1.5), (4.0, 1.5), (1.5, 8), (4, 8) ]
coords2 = run(dims2, corners2)
"""

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host = HOST, port = PORT)