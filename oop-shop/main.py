from urls import urlpatterns
from pprint import pprint

while True:
    try:
        url, arg = input('Type an address: ').split('/')
    except ValueError:
        print('You printed not valid url')
        continue
    
    found = False
    for uri, view in urlpatterns:
        if uri.split('/')[0] == url:
            found = True
            try:
                if arg:
                    pprint(view(arg))
                else:
                    print(view())
            except Exception as e:
                print(e)
    if not found:
        print('404 url not found')