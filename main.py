from fastapi import FastAPI
import json
import pandas as pd
app=FastAPI()

students={
    'ali':[12,17.7,18],
    'sara':[14.7,18,15.25],
    'hasan':[10,20,13.56]
}

df=pd.DataFrame(students,columns=students.keys())

df_json=df.to_json()

@app.get('/')
def read():
    return json.loads(df_json)


@app.post('/means')
def means():
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


@app.post('/shower/{t}')
def shower(t:str):
    d=df[t]
    d_json=d.to_json()
    return json.loads(d_json)


@app.put('/update/{st}')
def update(st:str):
    df[st]=df[st].apply(lambda y: y+1 )
    df_json=df.to_json()
    return json.loads(df_json)
