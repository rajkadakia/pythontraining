import requests
params={
    "name":"Raj",
    "age" : 25
}
response = requests.get("https://httpbin.org/get", params=params)
print(response.url)
res_json=response.json()
print(res_json)

payload={
    "name":"raj",
    "age":25
}

responsepost=requests.post("https://httpbin.org/post",data=payload)
res_post=responsepost.json()
print(res_post)

payload1={
    "name":"raj",
    "age":25
}
responseput=requests.put("https://httpbin.org/put",data=payload1)
res_put=responseput.json()
print(res_put)
patch_payload = {"age": 26}

res_patch = requests.patch(
    "https://httpbin.org/patch",
    json=patch_payload
)

print(res_patch.json())
res_delete = requests.delete("https://httpbin.org/delete")
print(res_delete.status_code)
print(res_delete.json())
