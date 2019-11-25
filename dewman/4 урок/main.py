from PIL import Image
import os
from instabot import Bot
from dotenv import load_dotenv


def list_img():
    imgs = os.listdir('images')
    if not os.path.exists('image2'):
        os.makedirs('image2')
    for img in imgs:
        image = Image.open(f'images/{img}')
        width = image.width
        height = image.height
        cordionate1 = (width - height) / 2
        cordionate2 = cordionate1 + height
        coordinates = (cordionate1, 0, cordionate2, height)
        cropped = image.crop(coordinates)
        cropped.save(f"image2/n{img}")


def load_img_insta(user_name, pass_word):
    imgs = os.listdir('image2')
    bot = Bot()
    bot.login(username=user_name, password=pass_word)
    for img in imgs:
        bot.upload_photo(f'image2/{img}')


def main():
    load_dotenv()
    user_name = os.environ['USERNAME_INSTAG']
    pass_word = os.environ['PASSWORD_INSTAG']
    load_img_insta(user_name, pass_word)


if __name__ == '__main__':
    main()
