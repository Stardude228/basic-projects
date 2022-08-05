import requests

url = 'https://cdns-images.dzcdn.net/images/cover/a26e476def6a65078e518e95a961fd7f/500x500.jpg'

res = requests.get(url)

name = 'photos/dancin.jpg'

with open(name, 'wb')as file:
    file.write(res.content)