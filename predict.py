import pickle
from typing import Any, Dict
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, ConfigDict, Field
from typing import Literal

class Customer(BaseModel):    
    model_config = ConfigDict(extra='forbid') 
    
    gender: Literal["female", 'male']
    seniorcitizen: Literal[0, 1]
    partner: Literal["no", "yes"]
    dependents: Literal["no", "yes"]
    phoneservice: Literal["no", "yes"]
    multiplelines: Literal["no", "yes"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes"]
    onlinebackup: Literal["no", "yes"]
    deviceprotection: Literal["no", "yes"]
    techsupport: Literal["no", "yes"]
    streamingtv: Literal["no", "yes"]
    streamingmovies: Literal["no", "yes"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["no", "yes"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0) 
    totalcharges: float = Field(..., ge=0.0)

class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool

app = FastAPI(title='predict-churn')

@app.get('/predict')
def ping():
    return 'Predict waff!'

with open('model.bin', 'rb') as f_in:
        pipeline = pickle.load(f_in)
print(f'model load as')

def predict_one(customer: Customer): #
     result = pipeline.predict_proba(customer)[0, 1]
     return float(result)

@app.post('/predict')
def predict(customer: Customer)-> PredictResponse:
     prob = predict_one(customer.model_dump())
     return  PredictResponse(
          churn_probability= prob,
          churn= bool(prob >= 0.5)
     )
     print('aahr')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0', port=9696)

    