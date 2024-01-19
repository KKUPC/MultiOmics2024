from unix101 import random_data
from unix101 import analyse_ as an

data = random_data()

df = data.create_data(num_rows=1000, num_cols=10000)

df.to_csv('data.csv', index=False)


model = an()
model.classification_report(df=df)




