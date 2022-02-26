# https://shielded-plateau-68883.herokuapp.com/
import json
import requests
r=requests.get('https://shielded-plateau-68883.herokuapp.com/')
print(r.status_code)

r_json=r.json()
print(len(r_json))

r_str=json.dumps(r_json,indent=2)

print(r_str)

print(r.text)
print(r.content)


# ================================================================================

# r2=requests.post('https://shielded-plateau-68883.herokuapp.com/')
# print(r2.status_code)

# # da='ali'
# r3=requests.post('https://shielded-plateau-68883.herokuapp.com//update/?name={ali}')
# # r3_dict=r.json()

# print(r3)
