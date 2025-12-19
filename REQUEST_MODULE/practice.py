import requests
headers={
    "User-Agent":"Raj Kadkia/22.11",
    "Accept":"image/png"
}
response = requests.get("https://httpbin.org/user-agent",headers=headers)
print(response.text)

response1 = requests.get("https://httpbin.org/headers")
print(response1.text)

response2 = requests.get("https://httpbin.org/image",headers=headers)
with open("image.png","wb")as f:
    f.write(response2.content) 

response3 = requests.get("https://httpbin.org/delay/4")
res_3=response3.json()
print(res_3)

response4= requests.get("https://httpbin.org/delay/4",timeout=3)
res_4=response4.json()
print(res_4)

