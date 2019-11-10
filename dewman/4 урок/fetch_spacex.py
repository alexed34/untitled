import requests
import os
import urllib3

urllib3.disable_warnings()


def fetch_spacex_last_launch():
    path = 'images'
    url = 'https://api.spacexdata.com/v3/launches/latest?filter=links/flickr_images'
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    links = response.get('links')
    flickr_images = links.get('flickr_images')
    for number, url in enumerate(flickr_images, 1):
        response = requests.get(url)
        response.raise_for_status()
        filname = f'spacex{number}.jpg'
        with open(os.path.join(path, filname), 'wb') as file:
            file.write(response.content)


def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()