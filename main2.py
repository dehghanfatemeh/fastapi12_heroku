# https://infinite-ridge-30160.herokuapp.com/

import requests
r=requests.get('https://infinite-ridge-30160.herokuapp.com/')
print(r.status_code)

# print(r.headers)
# print(r.text)
# print(r.content)

# r2=requests.post('https://infinite-ridge-30160.herokuapp.com/average')
# print(r2.status_code)

# da='ali'
# r3=requests.post('https://infinite-ridge-30160.herokuapp.com/shower/?t={da}')
# r3_dict=r.json()

# print(r3_dict)
