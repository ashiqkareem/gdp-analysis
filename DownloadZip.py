import requests

url = 'https://raw.github.com/ashiqkareem/gdp-analysis/master/files.zip'

r = requests.get(url)
with open("files.zip", "wb") as code:
    code.write(r.content)
