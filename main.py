from flask import Flask, render_template, request, redirect
import loadBalancer as lb
import json


app = Flask(__name__)
with open("config.json", mode="r") as config_file:
    content = json.load(config_file)


load_balancer = lb.LoadBalancer(content["ipList"])

@app.route('/')
def form():
    return render_template('index.html')


@app.route('/data', methods=['POST'])
def data():
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        try:
            load_balancer.sendText(form_data['color'], form_data['text'])
        except:
            print("debiluwa")

        return redirect('/')


app.run(host='localhost', port=2137)
