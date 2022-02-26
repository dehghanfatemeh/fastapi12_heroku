from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import json
import pandas as pd
app=FastAPI()

Students={
    'ali':[12,17.7,18],
    'sara':[14.25,18,15.75],
    'hasan':[10,14.75,13.56],
    'reza':[11.5,16.5,13.25]
}

df=pd.DataFrame(Students,columns=Students.keys())


class stu(BaseModel):
    name: str
    number1: float
    number2: float
    number3: float

@app.get('/')
def read():
    # df.drop(index='ave',axis=0,inplace=True)
    df_json=df.to_json()
    return json.loads(df_json)

@app.get('/average')
def average():
    a={}
    for i in df.columns:
        s=df[i].mean()
        i={i:s}
        a.update(i)
    a=pd.Series(a)
    a_json=a.to_json()
    return json.loads(a_json)


@app.post('/insert/')
def insert(student:stu):
    if student.name in df.columns:
            raise HTTPException(status_code=404,detail='This student is available')
    else:    
        # s=(student.number1+student.number2+student.number3)/3
        df[student.name]=[student.number1,student.number2,student.number3]
        df_json=df.to_json()
        return json.loads(df_json)

@app.put('/update/{name}')
def update(name:str):

    if name in df.columns:
        for i in df.columns:
            for j in df.index:
                df.loc[j,i]=df.loc[j,i]+1        
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')

@app.delete('/delete/{name}')
def delete(name:str):
    if name in df.columns:
        df.drop(columns=name,axis=1,inplace=True)
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')
