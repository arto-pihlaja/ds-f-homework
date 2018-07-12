from flask import request, json, Response
from app import app
import pickle
import pandas as pd

@app.route("/")
@app.route("/index")
def index():
    return "Hello Flask World!"
@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        return "Please use POST!"
    else:                               
        #resp = str(request.json["crime_rate"])
        resp = create_response(request)
        return Response(resp, status=200, mimetype="application/json")
        #return request_json #["crime_rate"]

def create_response(request):
    #return "Processing request!"
    independent_vars = ['crime_rate', 'avg_number_of_rooms', 'distance_to_employment_centers',
                'property_tax_rate', 'pupil_teacher_ratio']
    iv_list = []
    for iv in independent_vars:
        try:
            iv_list.append(request.json[iv])
        except RuntimeError:
            #return Response("Bad request", status = 400)
            return "Bad request"    
# #        crime_rate = independent_vars["crime_rate"]
# #        avg_number_of_rooms = independent_vars["avg_number_of_rooms"]
    model = pickle.load(open(".\\app\\cv_polyfit.pkl","rb"))
    rmse = pickle.load(open(".\\app\\cv_rmse.pkl","rb"))
    df = pd.DataFrame(iv_list).transpose()
    response = {"house_value" : model.predict(df)[0],
        "stddev" : rmse }
    return json.dumps(response)    
