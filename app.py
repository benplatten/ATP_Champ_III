from flask import Flask, render_template, request

from creative_builder_test import head_to_head

DEBUG = True
HOST = '127.0.0.1'
PORT = 5000

app = Flask(__name__)

@app.route("/")
def home():   

    return render_template("home.html")

@app.route('/receivedata', methods=['POST'])
def receive_data():
    template_type = request.form['template_type']
    if template_type == '1':
    	player1Name = request.form['player1Name']
    	player2Name = request.form['player2Name']
    	data = head_to_head(player1Name,player2Name)
    	return render_template("receivedata.html", data=data)

    else:
    	return render_template("receivedata.html", data='error')


    #if template_type == 2:
    #	do this
    #if template_type == 3:
   # 	do this
    #if template_type == 4:
    #	do this


    


if __name__ == "__main__":
    app.run(debug=DEBUG,host=HOST,port=PORT)