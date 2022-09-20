import json
import requests

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def covid():
    if request.method == 'POST':
        country = request.form["country"]
        print(country)

        url = "https://api.covid19api.com/summary"
        print(url)

        response = requests.get(url).json()
        print(response)

        total_Countries= response["Countries"]
        print(total_Countries)

        for i in range(len(total_Countries)):
            if total_Countries[i]["Country"] == 'country':
                country_stats= total_Countries[i]
                print(country_stats)

                covid_data = {
                    'TotalConfirmed': country_stats['TotalConfirmed'],
                    'TotalDeaths': country_stats['TotaDeaths'] }
                return render_template("covid.html")
    else:
        return render_template("covid.html")
app.run()



























#         https://api.covid19api.com/summary
