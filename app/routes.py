from flask import request
from app import app
import pickle

@app.route("/")
@app.route("/index")
def index():
    return "Hello Flask World!"
@app.route("/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        pass 
    else:        
        return create_response(request)

def create_response(request):
    from flask import jsonify
    request_json = request.get_json()
    independent_vars = ['crime_rate' 'avg_number_of_rooms' 'distance_to_employment_centers'
                'property_tax_rate' 'pupil_teacher_ratio']
    iv_list = []
    for iv in independent_vars:
        try:
            iv_list.append(request_json[iv])
        except RuntimeError:
            #return Response("Bad request", status = 400)
            return "Bad request"
#        crime_rate = independent_vars["crime_rate"]
#        avg_number_of_rooms = independent_vars["avg_number_of_rooms"]
    model = pickle.load("cv_polyfit.pkl")
    response = {"house_value" : model.predict(iv_list),
        "stddev" : model.stddev }
    return jsonify(response)    
