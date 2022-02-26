# fastapi12_heroku
General description of the project:
The program is written with [python](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/) and [heroku](https://id.heroku.com/login). I use [pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) to run on the server.


Link api that I deployed on the web : https://shielded-plateau-68883.herokuapp.com/docs

-------------------------------------

In file main.py , I created two apps that only depoted app on the web using Heroku:
link : https://shielded-plateau-68883.herokuapp.com/docs#/

and To output app2 (actually calling app) by typing the `uvicorn main:app2 --reload` command in the terminal
And the X address is written in the browser and you can see the output `http://127.0.0.1:8000/docs`




## Development construction and Deployment rocket
If you want to contribute to the project, the best way is to fork the repository and make your own changes to the code and create a pull request.

A few steps to get started:

1.Clone the repository:`https://github.com/dehghanfatemeh/fastapi12_heroku.git`

2.Install the dependencies:`pip install -r requirements.txt`

3.Make your changes and then `git add . && git commit -m "Your commit message"`

4.Create a pull request

5.Wait for the approval


How to start development server:

1.First, you need to install the dependencies you have not yet: `pip install -r requirements.txt`

2.Run `python -m uvicorn main:app --reload` in the project root directory

3.Open`http://127.0.0.1:8000/docs`in your browser to see the documentation


There several options for you to deploy this app on a remote server, but here is a simple example:

One of the most popular options [Heroku](https://id.heroku.com/login), Heroku provides you a free plan to deploy your web applications as quick as possible. By default, this repository is configured to be deployed on Heroku, all you need to do is to fork this repository, register your account for Heroku from [here](https://signup.heroku.com/login), download the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and run the bellow commands step by step.


At first, you need to login from the CLI:
```
heroku login
```

This will open a web browser and prompts you to login with your account.

After that you logged in via the CLI, you run the bellow command to create a new app on Heroku (if you don't want to create it manually from Heroku dashboard)
```
heroku create [<YOUR_APP_NAME>]
```
It will create an application for you with the given name (if the names is valid and is not already taken by another user).


Then you have to connect to the remote git that Heroku holds for your app:
```
heroku git:remote -a [<YOUR_APP_NAME>]
```

And then you can push the repository to Heroku:
```
git push heroku master
```
Now heroku will deploy your app to the Heroku servers and install the dependencies for you automatically. You can access your app from `http://<YOUR_APP_NAME>.herokuapp.com`


###### Important notes for Heroku users:

-After making changes to your code, you need to run `git add . && git commit -m "Your commit message"` and then `git push heroku master` to deploy your changes to Heroku.

-You can also use `heroku logs` to see the logs of your app on your terminal.

-Every new library that you install must be included in `requirements.txt`  file so that Heroku will install it.

-By default, we are using `gunicorn` as a master process and `uvicorn` as worker processes.

Full documentation to deploy your app on Heroku using git can be found [here](https://devcenter.heroku.com/articles/git). You can also deploy your app using [Github integration](https://devcenter.heroku.com/articles/github-integration) for Heroku.


#### main.py file description:


I enter all the libraries I need:
```python
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import json
import pandas as pd
import requests
```



I create an app and app2 using FastAPI:
```python
app=FastAPI()
app2=FastAPI()
```



I am creating a dictionary of student grades that includes 4 students:
```python
Students={
    'ali':[12,17.7,18],
    'sara':[14.25,18,15.75],
    'hasan':[10,14.75,13.56],
    'reza':[11.5,16.5,13.25]
}
```



I convert the created dictionary to a data frame and specify the dictionary keys as its column name:
```python
df=pd.DataFrame(Students,columns=Students.keys())
```



I create a class that inherits from BaseModel:
```python
class stu(BaseModel):
    name: str
    number1: float
    number2: float
    number3: float
 ```


### app 

Using the get method, we read the data and finally display the data as json:
```python
@app.get('/')
def read():
    df_json=df.to_json()
    return json.loads(df_json)
```



Using the get method, calculate the average score of each student and finally display the output as json:
```python
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
```



Using the post method of a new student insert and if there is such a name in students, it gives an error to the user,finally the output is displayed as json:
```python
@app.post('/insert/')
def insert(student:stu):
    if student.name in df.columns:
            raise HTTPException(status_code=404,detail='This student is available')
    else:    
        df[student.name]=[student.number1,student.number2,student.number3]
        df_json=df.to_json()
        return json.loads(df_json)
```



Using the update method, it only increases the name of the student entered by the unit by one and in the absence of such a name gives the user an error,
finally the output is displayed as json:
```python
@app.put('/update/{name}')
def update(name:str):
    if name in df.columns:
        for i in df.index:
            df.loc[i,name]=df.loc[i,name]+1        
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')
```



Uses the delete method to delete only the student name entered by the user and in the absence of such a name gives the user an error,
finally the output is displayed as json:
```python 
@app.delete('/delete/{name}')
def delete(name:str):
    if name in df.columns:
        df.drop(columns=name,axis=1,inplace=True)
        df_json=df.to_json()
        return json.loads(df_json)
    else:
        raise HTTPException(status_code=404,detail='This student is not available')
```
### app2

Using the Get method, displays a message for app2 in the output:
```python
@app2.get('/')
def read_app2():
    return {'msg':'App 2'}
```

Using the request method, calls app and output the method takes the mean and displays it:
```python
@app2.get('/avg')
def avg():
    result=requests.get('https://shielded-plateau-68883.herokuapp.com/average')
    return result.json()
```






