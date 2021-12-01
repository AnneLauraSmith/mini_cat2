from flask import Flask, render_template,flash, request, redirect, url_for
import requests
import json
# import config
from PIL import Image
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route("/")
def index():
    url = "https://api.thecatapi.com/v1/images/search"

    headers = { 'x-api-key': "1d5c2757-81fa-4fc0-acd3-b037ceb35975Y" }
    cat_picture = requests.request("GET", url, headers=headers)
    [{"breeds":[{"weight":{"imperial":"6 - 15","metric":"3 - 7"},"id":"char","name":"Chartreux","cfa_url":"http://cfa.org/Breeds/BreedsCJ/Chartreux.aspx","vetstreet_url":"http://www.vetstreet.com/cats/chartreux","vcahospitals_url":"https://vcahospitals.com/know-your-pet/cat-breeds/chartreux","temperament":"Affectionate, Loyal, Intelligent, Social, Lively, Playful","origin":"France","country_codes":"FR","country_code":"FR","description":"The Chartreux is generally silent but communicative. Short play sessions, mixed with naps and meals are their perfect day. Whilst appreciating any attention you give them, they are not demanding, content instead to follow you around devotedly, sleep on your bed and snuggle with you if you’re not feeling well.","life_span":"12 - 15","indoor":0,"lap":1,"alt_names":"","adaptability":5,"affection_level":5,"child_friendly":4,"dog_friendly":5,"energy_level":2,"grooming":1,"health_issues":2,"intelligence":4,"shedding_level":3,"social_needs":5,"stranger_friendly":5,"vocalisation":1,"experimental":0,"hairless":0,"natural":0,"rare":0,"rex":1,"suppressed_tail":0,"short_legs":0,"wikipedia_url":"https://en.wikipedia.org/wiki/Chartreux","hypoallergenic":1,"reference_image_id":"j6oFGLpRG"}],"id":"K3eHRIQXM","url":"https://cdn2.thecatapi.com/images/K3eHRIQXM.jpg","width":1600,"height":1200}]

    cat_picture = cat_picture.json()
    [{'breeds': [], 'id': 'b03', 'url': 'https://cdn2.thecatapi.com/images/b03.jpg', 'width': 500, 'height': 334}]
    cat_picture= cat_picture[0]['url']
    fact_response = requests.get('https://catfact.ninja/fact')
    the_data = fact_response.json()
    print(type(the_data), the_data)
    cat_fact = the_data['fact']
    return render_template("index.html", cat_picture=cat_picture, data1=cat_fact)
    data = json.loads(response.text)
    print(the_data)

    return render_template("index.html")#, #cat_picture=cat_picture, data1=cat_fact)

@app.route('/grounding/')
def grounding():
    return render_template("grounding.html")

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/cats/')
def cats():
    return render_template("cats.html")




if __name__ == '__main__':
    app.run(debug=True)


  