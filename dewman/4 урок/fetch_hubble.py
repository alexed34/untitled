import requests
import os
import urllib3

urllib3.disable_warnings()


def get_response_json(url, name):
    urll = f'{url}{name}'
    response = requests.get(urll)
    response.raise_for_status()
    return response.json()


def get_img_habbl(response_json_photos):
    if not response_json_photos:
        raise ValueError('нет данных в json обьекте')
    return [i['id'] for i in response_json_photos]


def get_photo(photo, response_photos):
    image_files = response_photos.get('image_files')
    url_photo = f"https:{image_files[-1]['file_url']}"
    file_extension = os.path.splitext(url_photo)[1]
    filename = f'{photo}{file_extension}'
    response_photo = requests.get(url_photo, verify=False)
    response_photo.raise_for_status()
    data = {'filname': filename,
            'response_photo': response_photo}
    return data


def write_photo(data, path):
    with open(os.path.join(path, data['filname']), 'wb') as file:
        file.write(data['response_photo'].content)


def main():
    path = 'images'
    os.makedirs(path, exist_ok=True)
    url_images = 'https://hubblesite.org/api/v3/images/'
    name = 'wallpaper'
    response_images = get_response_json(url_images, name)
    photos_name = get_img_habbl(response_images)
    url_image = 'https://hubblesite.org/api/v3/image/'
    for photo in photos_name:
        response_photo = get_response_json(url_image, photo)
        data = get_photo(photo, response_photo)
        write_photo(data, path)


if __name__ == '__main__':
    main()
