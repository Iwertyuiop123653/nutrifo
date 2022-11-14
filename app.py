from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route("/<name>/<amount>")
def home(name, amount):
    try:
        query = f'{amount} {name}'
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'y8kZDhEprK3gpJcaV07caw==tJHv3PL7FCMfKn2h'})
        dataned = response.json()[0]["calories"]
        dataned2 = response.json()[0]["fat_total_g"]
        dataned3 = response.json()[0]["protein_g"]
        dataned4 = response.json()[0]["sugar_g"]
        dataned5 = round(dataned) + round(dataned2) + round(dataned3) + round(dataned4)
        return render_template("index.html", text=str(dataned), data1 = str(dataned2),
        data2 = str(dataned3), data3 = str(dataned4), data4 = str(dataned5))
    except:
        return "Whoops You spelled it wrong"

@app.route("/About")
def About():
    return render_template("about.html")

app.run(debug=True)