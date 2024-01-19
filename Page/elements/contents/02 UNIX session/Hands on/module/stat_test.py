from unix101 import random_data
from unix101 import analyse_ as an

data = random_data()
df = data.create_data(num_rows=10000, num_cols=1000)



model = an()
model.classification_report(df=df)