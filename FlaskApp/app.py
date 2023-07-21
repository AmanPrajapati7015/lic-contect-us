from flask import Flask, render_template, request



def send_to_telegram(message):
    import requests
    auth = "6206326589:AAGuXdrMMyFQIvm6kCACAh-7Jmdy8RgJJGU"
    chat_id = "5768401131"
    url = f"https://api.telegram.org/bot{auth}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def add_to_data(data_row):
    import csv
    f = open("data.csv", "a", newline='')
    csvw = csv.writer(f)
    csvw.writerow(data_row)
    f.close()


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

    str = ""
    for key in output.keys():
        str += f"{key} \t : {output[key]} \n"


    send_to_telegram(str)
    add_to_data(output.values())

    return render_template("thanks.html", name=output["name"], date=output["date"], phn_no=output["phn_no"])
    




if __name__ == "__main__":
    app.run(debug=True)