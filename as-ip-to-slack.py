import requests, json

hook = 'https://hooks.slack.com/services/...incoming.hook.data...'

response = requests.get('https://api.ipify.org')

payload = json.dumps({'username': 'as-ip', 'text': '/as-ip ' + response.text, 'icon_emoji': ':dark_sunglasses:'})

response = requests.post(hook, data=payload)

print(response.text)
