
import requests
    
url = 'http://localhost:9696/predict'

customer = {
    "gender": "female",
    "seniorcitizen": 1,
    "partner": "no",
    "dependents": "yes",
    "phoneservice": "yes",
    "multiplelines": "no",
    "internetservice": "dsl",
    "onlinesecurity": "yes",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "one_year",
    "paperlessbilling": "no",
    "paymentmethod": "bank_transfer_(automatic)",
    "tenure": 62,
    "monthlycharges": 56.15,
    "totalcharges": 3487.95,
    "x": 1
}

response = requests.post(url, json=customer)
churn = response.json()
print(f'Response of ML Churn Service: {churn}')

if churn['churn_probability'] >= 0.5:
    print('send promo')
else:
    print('do nothing')

churn

print('churn', churn['churn_probability'])