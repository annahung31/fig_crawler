
import requests


url = 'https://cdn.pixabay.com/photo/2016/07/11/15/43/pretty-woman-1509956__340.jpg'
filename = '../output/test.jpg'
cover_path = filename
with open( cover_path , 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)

