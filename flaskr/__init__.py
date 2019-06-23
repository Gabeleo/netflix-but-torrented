import os
from flask import Flask, redirect, request, render_template
from depend import htpc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        query = request.form['text']
        htpc.create("https://thepiratebay.org/", query)
        return redirect(htpc.infohash)

if __name__=='__main__':
    app.run(debug=True)