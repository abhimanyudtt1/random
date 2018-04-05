from flask import Flask,render_template,request,json,redirect,url_for



app = Flask(__name__)
@app.route("/showPassword",methods= ['POST','GET'])
def main():
    print request.args.get('user'),',',request.args.get('password')
    return 'done!'


app.run(host = '0.0.0.0',debug=True)