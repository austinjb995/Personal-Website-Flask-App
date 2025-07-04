#!/usr/bin/env python

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == ['GET']:
        if (request.args.get('num') == None):
            return render_template('squarenum.html')
        elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid Number</h1></body></html>"
        else:
            number = request.args.get('num')
            sq = int(number)  * int(number)
            return render_template('answer.html', squareofnum=sq, num=number)
    
    """
    if request.method == 'POST':
        if(request.form['num'] == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"
        else:
            number = request.form['num']
            sq = int(number) * int(number)
            return render_template('answer.html', 
                            squareofnum=sq, num=number)
    # If the method is GET,render the HTML page to the user
    if request.method == 'GET':
        return render_template("squarenum.html")
       """ 
        
if __name__ == '__main__':
    app.run(debug=True)
