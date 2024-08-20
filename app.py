from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import numpy as np
import pandas as pd
import pickle
import joblib
import json
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory='templates')

## Nous allons créer une variable de classe particulière
class InputVar(BaseModel):
  age : float
  bmi : float
  bp : float
  s1 : float
  s2 : float
  s3 : float
  s4 : float
  s5 : float
  s6 : float

## Load model form disk
regmodel = joblib.load(open('regmodel.pkl', 'rb'))
scalar = joblib.load(open('scaling.pkl', 'rb'))

# Creation de notre endpoint
# @app.get('/')
# def index():
#   return {'message': 'Hello world'}

# @app.post('/predict')
# def prediction(data: InputVar):
#     try:
#         # Convert input data to DataFrame
#         input_data = pd.json_normalize(data.model_dump())
        
#         # Check if input data has the expected number of features
#         expected_features = ['age', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
#         if list(input_data.columns) != expected_features:
#             raise HTTPException(status_code=400, detail="Input data has incorrect features. Expected features are: " + ", ".join(expected_features))
        
#         # Ensure the input data has the correct order of features
#         input_data = input_data[expected_features]

#         # Add a missing feature (if any) with default value of 0.0
#         if len(input_data.columns) < 10:
#             input_data['s7'] = 0.0

#         # Scale the data
#         scaled_data = scalar.transform(input_data)

#         # Perform prediction
#         predicted = regmodel.predict(scaled_data)

#         # Return prediction as JSON response
#         return {'diabetes_progression_prediction': predicted[0]}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})



@app.post("/predict")
def predict(request: Request,
            age: float = Form(...),
            bmi: float = Form(...),
            bp: float = Form(...),
            s1: float = Form(...),
            s2: float = Form(...),
            s3: float = Form(...),
            s4: float = Form(...),
            s5: float = Form(...),
            s6: float = Form(...)):
    try:
      s7 = 0.0
      data = [age, bmi, bp, s1, s2, s3, s4, s5, s6, s7]
      data = np.array(data).reshape(1, -1)
      scaled_data = scalar.transform(data)
      prediction = regmodel.predict(scaled_data)[0]
      return templates.TemplateResponse("home.html", {"request": request, "prediction_text": f"The diabete progression is {prediction:.2f}"})
    except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))



if __name__== '__main__':
  uvicorn.run(app)