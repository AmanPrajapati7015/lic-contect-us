from flask import Flask, render_template, url_for, request
import requests;


# def sendToTel(str){
#     import requests


# }

app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return "hello world"

@app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    str = ""
    for key in output.keys():
        str += f"{key} \t : {output[key]} \n"


    # sendToTel(str)
    print(str)


    return render_template("thanks.html")
    




if __name__ == "__main__":
    app.run(debug=True)