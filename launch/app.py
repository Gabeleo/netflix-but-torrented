import os
from flask import Flask, redirect, request, render_template
import subprocess
import json 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':

        query = request.form['text']
        url = '"url" :' + 'https://thepiratebay.org/search/' + query.replace(' ', '%20') + '/0/99/0'

        with open('urls.json', 'w') as infile:
                json.dump(url, infile)

        subprocess.call(["cd", "C:\\Users\\Gabe\\dev\\NBT\\launch\\dependencies\\spider\\spider\\spiders"], shell=True)
        subprocess.call(["python", "pirate_spider"])

        #change file path when executing in deployment or on another machine
        path = 'C:\\Users\\Gabe\\dev\\nbt\\launch\\dependencies\\spider\\spider\\spiders\\title.json'
        with open(path, 'w') as link:
                infohash = json.load(link)
                return redirect(infohash)

if __name__=='__main__': 
    app.run(debug=True)