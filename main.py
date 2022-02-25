from fastapi import FastAPI,HTTPException
import json
import pandas as pd
app=FastAPI()

Students={
    'ali':[12,17.7,18],
    'sara':[14.7,18,15.5],
    'hasan':[10,14.75,13.56],
    'reza':[11.5,16.5,13.25]
}

df=pd.DataFrame(Students,columns=Students.keys())

@app.get('/')
def read():
    df_json=df.to_json()
    return json.loads(df_json)

@app.post('/average')
def average():
    a=[]
    s=0
    for i in df.columns:
        for j in df.index:
            s=df.loc[j,i]+s
        s=s/len(df.index)
        a.append(s)
        s=0
    df.loc['ave']=a
    df_json=df.to_json()
    return json.loads(df_json)

@app.put('/update/{name}')
def update(name:str):
    if name in df.columns:
        df[name]=df[name].apply(lambda y: y+1)
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')

@app.delete('/delete/{name}')
def delete(name:str):
    if name in df.columns:
        df.drop(columns=name,axis=0,inplace=True)
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')
