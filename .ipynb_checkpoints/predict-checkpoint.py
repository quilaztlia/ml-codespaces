import pickle

with open(filename, 'rb') as f_in:
        pickle.load(f_in)

    print(f'model save as {filename}')

churn = pipeline.predict_proba(customer)

if churn >= 0.5:
    print('send promo')
else:
    print('do nothing')

churn


print('churn', churn)
