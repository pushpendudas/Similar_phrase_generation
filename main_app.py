# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 18:24:13 2020

@author: Biswajit
"""
from flask import Flask, render_template, request
from phrase_generation import get_similar_prases
app = Flask(__name__)


@app.route('/similar_sentence_generation', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        phrase = request.form['phrase']
        simi_sent_dict = get_similar_prases(phrase)
        return render_template('sample_output.html', result=simi_sent_dict)
    return render_template('sample_input.html', error=error)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
