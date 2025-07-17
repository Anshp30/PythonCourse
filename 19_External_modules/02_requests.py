import requests

r = requests.get('https://api.github.com/users/codewitharry')

with open("codewithharry","w") as f:
    f.write(r.text)
