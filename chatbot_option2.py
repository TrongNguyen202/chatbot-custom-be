import requests
import json

def processpromt_option(promt):
  url = "https://sider.ai/api/v3/completion/text"
  print("promt22", promt)
  payload = json.dumps({
    "prompt": f"sau đây là dữ liệu được lấy ra từ trong dữ liệu của cửa hàng của tôi để gợi ý sản phẩm cho khách hàng, bạn hãy dựa vào thông tin sau đây tôi đưa và đóng vai là người bán hàng cho cửa hàng Teelover của tôi và gợi ý sản phẩm áo cho khách hàng:' {promt}",
    "stream": True,
    "app_name": "ChitChat_Chrome_Ext",
    "app_version": "4.27.1",
    "tz_name": "Asia/Bangkok",
    "cid": "",
    "model": "sider",
    "search": False,
    "auto_search": False,
    "filter_search_history": False,
    "from": "chat",
    "group_id": "default",
    "chat_models": [],
    "files": [],
    "tools": {
      "auto": []
    },
    "extra_info": {
      "origin_url": "https://sider.ai/setup",
      "origin_title": "Sider: Thanh bên ChatGPT + GPT-4o, Claude 3.5, Gemini 1.5 & Công cụ AI"
    }
  })
  headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTUzMzEzNiwicmVnaXN0ZXJfdHlwZSI6Im9hdXRoMiIsImFwcF9uYW1lIjoiQ2hpdENoYXRfQ2hyb21lX0V4dCIsInRva2VuX2lkIjoiNGFlNjI3NzYtMzJmZS00Zjk5LTk3MDQtZWUwMjA0MzhkYTg2IiwiaXNzIjoic2lkZXIuYWkiLCJhdWQiOlsiIl0sImV4cCI6MTc2MjAxOTIyMywibmJmIjoxNzMwOTE1MjIzLCJpYXQiOjE3MzA5MTUyMjN9.qiFRadhT9pLE8YAiCJB3fAQaqfIXAxxknm4IGXCMqYc',
    'content-type': 'application/json',
    'cookie': 'NEXT_LOCALE=vi; source=gg; p1=ai; p2=display; lang=vi; _ga=GA1.1.27824592.1730745082; _gcl_au=1.1.1641201591.1730745082; _clck=1biq9lf%7C2%7Cfqm%7C0%7C1769; _gcl_aw=GCL.1730819549.Cj0KCQiAoae5BhCNARIsADVLzZfmNJikOlkF_MQunlrqwLundjCXXAVt_-UJZmEqQ2RSlMW_7delh8IaAp-TEALw_wcB; _gcl_gs=2.1.k1$i1730819547$u7016880; __stripe_mid=ecf8ff0f-7706-490a-854a-9cbdfab2e4d5cd33bf; __stripe_sid=a42a1ce7-31b6-4569-ac9a-5b044350232affb335; _fbp=fb.1.1730819594983.350222503897850437; _uetsid=7ada04609b8811ef84eea177d2a35c25; _uetvid=7ada76109b8811efae573f47dc45811d; token=Bearer%20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNTQ4OTQ3OCwicmVnaXN0ZXJfdHlwZSI6Im9hdXRoMiIsImFwcF9uYW1lIjoiQ2hpdENoYXRfQ2hyb21lX0V4dCIsInRva2VuX2lkIjoiNjBkZTI1NzgtNDFkYy00NDE4LTllODEtMTNkNmZiODhmNjc3IiwiaXNzIjoic2lkZXIuYWkiLCJhdWQiOlsiIl0sImV4cCI6MTc2MTkyMzYwMywibmJmIjoxNzMwODE5NjAzLCJpYXQiOjE3MzA4MTk2MDN9.drBjUKHn52_itVFMZQmY0Ciy3XKf8HRSxqWo0yF-OAM; refresh_token=discard; userinfo-avatar=https://chitchat-avatar.s3.amazonaws.com/8ef7b2e26e4a454f9f137882978d872b-1730819603.png; userinfo-name=User_pwgFQU; userinfo-type=oauth2; CloudFront-Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9maWxlLWNkbi5zaWRlci5haS8qL1UwTDVIVk42WTdOLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3MzM0MTE2MDV9fX1dfQ__; CloudFront-Signature=S8cLgz0NnyuYtRra-CIyBpvciAEC4pS15wrgCRepczXMGAkMYV29DzpdRYApyYGWovFEQTafjpGCzlDLdKGFmAIRhQs~4z4Gyaei9SM6uTs99NSC-bZzKSJLmcqmdyAkOfwRDp7utgEDJwWRwf4jdppU7uTf3rgvY7qZyxGDJoOKgpUwFYrwI5FAScp6-ZpqU7kvgaq~JYBfrsamkLMOHh~1SuAK~x63zXUMGeC8sEJndsQUACgT2GLCBwz6Z6Yw0ayfEdxYrrh0-St5Z1iOXopYyPmgo8Kp8uSqoV0n9wSEa-seV1PIvC92eshnEnNSCct-LlCAniwCeYYPXJ0j9g__; CloudFront-Key-Pair-Id=K344F5VVSSM536; _rdt_uuid=1730745081323.27aed353-93e2-4d13-b774-9f4e053ffcb2; _clsk=1qjvdu4%7C1730819606939%7C5%7C0%7Co.clarity.ms%2Fcollect; _ga_0PRFKME4HP=GS1.1.1730819526.2.1.1730819613.42.0.0',
    'origin': 'chrome-extension://difoiogjjojoaoomphldepapgpbgkhkb',
    'priority': 'u=1, i',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'none',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  complete_message = ""

  for line in response.iter_lines():
      if line:
          try:
              # Remove the "data:" prefix, then parse JSON
              data = json.loads(line.decode('utf-8').replace("data:", ""))
              # Extract the "text" field from each message part
              complete_message += data["data"]["text"]
          except json.JSONDecodeError:
              # Handle decoding errors if they arise
              print("Error decoding JSON:", line)

  # print("Complete Message:", complete_message)
  return complete_message



