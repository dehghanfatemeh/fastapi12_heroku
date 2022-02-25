# https://infinite-ridge-30160.herokuapp.com/

import requests
r=requests.get('https://infinite-ridge-30160.herokuapp.com/')
print(r.headers)
print(r.text)

r2=requests.post('https://infinite-ridge-30160.herokuapp.com/means')
r2_dict=r.json()
print(r2.status_code)

# da='ali'
# r3=requests.post('https://infinite-ridge-30160.herokuapp.com/shower/?t={da}')
# r3_dict=r.json()

# print(r3_dict)