
# coding: utf-8

# In[ ]:

# coding: utf-8
# In[ ]:

def backend(list2):
    import json
    with open(list2) as datafile:
        data =json.load(datafile)
    import numpy as np
    year  = []
    for index in range(0,52):
        year.append(data[index]["YEAR"])
    years =np.array(year)
    x = []
    for index in range(0,52):
        x.append(data[index]["COAL "])
    x_train =np.array(x)
    x_train=x_train.reshape((52,1))
    y=[]
    for m in range(0,52):
        y.append(data[m]["NATURAL GAS"])
    temp = np.array(y)
    temp=temp.reshape((52,1))
    x_train= np.column_stack((x_train, temp))
    y=[]
    for index in range(0,52):
        y.append(data[index]["GLOBAL OIL"])
        temp = np.array(y)
        temp=temp.reshape((52,1))
        x_train=np.column_stack((x_train, temp))
        y=[]
    for index in range(0,52):
        y.append(data[index]["PRIMARY CONSUMPTION"])
        temp = np.array(y)
        temp=temp.reshape((52,1))
        x_train=np.column_stack((x_train, temp))
        y=[]
    for index in range(0,52):
        y.append(data[index]["AVG CO2 EMISSIONS"])
        temp = np.array(y)
        temp=temp.reshape((52,1))
        y_train=temp


    i=0
    base = min(y_train)
    range = max(y_train) - base
    for x in y_train:
        x = (x-base)/range
        y_train[i]=x
        i=i+1
    i=0
    while i < 4:
        xi = x_train[:,i] 
        base = min(xi)
        range = max(xi) - base
        for x in xi:
            x = (xi-base)/range
        x_train[:,i] = x
        i=i+1
    
    x_train= np.column_stack((x_train, y_train))
    x_train= np.column_stack((x_train, years))

    import pandas as pd
    s = pd.DataFrame(x_train)
    s.columns=['COAL ' , 'NATURAL GAS' , 'GLOBAL OIL' , 'PRIMARY CONSUMPTION' , 'AVG CO2 EMISSIONS' , 'YEAR']
    # In[4]:

    df1 = s[['COAL ' , 'NATURAL GAS' , 'GLOBAL OIL' , 'PRIMARY CONSUMPTION' , 'AVG CO2 EMISSIONS' , 'YEAR']]
    def to_json(df1,df2):
        d = [ 
            dict([
                (colname, row[i]) 
                for i,colname in enumerate(df1.columns)
                ])
                for row in df1.values
            ]
        return json.dump(d, open(df2 + '.json', 'w'))

    to_json(df1, 'my_filename')
    with open('my_filename.json') as json_data:
        t=json.load(json_data)
    json_data.close()
    
