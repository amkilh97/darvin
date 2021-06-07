from flask import Flask,request
import pandas as pd
from _collections import OrderedDict
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app=Flask(__name__)


@app.route('/api')
def get():
    male=float(request.args['Male'])
    age=float(request.args['Age'])
    smoking=float(request.args['Smoking'])
    chol=float(request.args['Chol'])
    bp=float(request.args['BP'])
    hrate=float(request.args['Hrate'])
    glue=float(request.args['Glue'])
    data='framingham.csv'
    df=pd.read_csv(data,na_values='',na_filter='0')
    fname=['male','age','cigsPerDay','totChol','sysBP','heartRate','glucose']
    tname=['TenYearCHD']
    x=df[fname]
    y=df[tname]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.000001,random_state=123)
    new_data=OrderedDict([('male',male),('age',age),('cigsPerDay',smoking),('totChol',chol),('sysBP',bp),('heartRate',hrate),('glucose',glue)])
    new_data=pd.Series(new_data).values.reshape(1,-1)
    linear_regression_model = LinearRegression()
    linear_regression_model.fit(x_train,y_train)
    return str(linear_regression_model.predict(new_data))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('love')
    app.run()
