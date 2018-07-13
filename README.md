# ds-f-homework
##Python homework
Predicts average house prices in an area, based on certain attributes of the area.

Data exploration and a regression model in _Jupyter_, then use the trained model in a _Flask app_.
The Flask app takes independent variables as input (JSON) and gives the dependent variable (average house price) as output.

Start commands (in Windows):
`python -m flask run`

Sample call to local app:
`curl -X POST -H "Content-Type: application/json" -d "{ \"crime_rate\" : 0.1, \"avg_number_of_rooms\": 4.0,   \"distance_to_employment_centers\": 6.5,   \"property_tax_rate\": 330.0,   \"pupil_teacher_ratio\": 19.5 }" http://localhost:5000/predict`

Corresponding response:
`{"house_value": 14.88522883103972, "stddev": 5.451689034705581}`
