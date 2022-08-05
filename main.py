import tweepy
import random
from PIL import Image, ImageDraw, ImageFont
import time

from tweepy import API

print("Starting...")

# Aquí se deben poner las credenciales de la cuenta
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

myusername = api.me().screen_name
file_name = "last_seen_id.txt"
hour_to_post = int(time.strftime('%H'))

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def crear_imagen():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    width = 1000
    height = 1000
    # creates image
    img = Image.new('RGB', size=(width, height), color=(a, b, c))
    draw = ImageDraw.Draw(img)
    num_figuras = random.randint(4, 10)
    for x in range(num_figuras):
        x0 = random.randint(0, width - 200)
        y0 = random.randint(0, height - 200)
        x1 = random.randint(x0, width)
        y1 = random.randint(y0, height)
        # in case of square or circle:
        aux = random.randint(100, 200)
        x2 = x0 + aux
        y2 = y0 + aux
        polygon = []
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)
        figura = random.randint(0, 4)
        if figura == 0:  # rectangle
            draw.rectangle([x0, y0, x1, y1],
                           fill=(R, G, B))
        elif figura == 1:  # square
            draw.rectangle([x0, y0, x2, y2],
                           fill=(R, G, B))
        elif figura == 2:  # ellipse
            draw.ellipse([x0, y0, x1, y1],
                         fill=(R, G, B))
        elif figura == 3:  # circle
            draw.ellipse([x0, y0, x2, y2],
                         fill=(R, G, B))
        elif figura == 4:  # random polygon
            polygon_vertex = 2 * random.randint(3, 8)
            for vertex in range(polygon_vertex):
                polygon.append(random.randint(0, width))
            draw.polygon(xy=polygon, fill=(R, G, B))
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text([30, 960], text='@' + myusername, fill=(0, 0, 0), font=font)

    del draw
    img.save('cuadro.png')


def crear_respuesta(r1, r2, g1, g2, b1, b2, color, mention_username):
    a = random.randint(r1, r2)
    b = random.randint(g1, g2)
    c = random.randint(b1, b2)
    if color == 'red':
        b = c
    elif color == 'yellow':
        a = b
    elif color == 'green':
        a = c
    elif color == 'bw':
        a = b = c
    width = 1000
    height = 1000
    # creates image
    img = Image.new('RGB', size=(width, height), color=(a, b, c))
    draw = ImageDraw.Draw(img)
    num_figuras = random.randint(4, 10)
    for x in range(num_figuras):
        x0 = random.randint(0, width - 200)
        y0 = random.randint(0, height - 200)
        x1 = random.randint(x0, width)
        y1 = random.randint(y0, height)
        # in case of square or circle:
        aux = random.randint(100, 200)
        x2 = x0 + aux
        y2 = y0 + aux
        polygon = []
        R = random.randint(r1, r2)
        G = random.randint(g1, g2)
        B = random.randint(b1, b2)
        if color == 'red':
            G = B
        elif color == 'yellow':
            R = G
        elif color == 'green':
            R = B
        elif color == 'bw':
            R = G = B
        figura = random.randint(0, 4)
        if figura == 0:  # rectangle
            draw.rectangle([x0, y0, x1, y1],
                           fill=(R, G, B))
        elif figura == 1:  # square
            draw.rectangle([x0, y0, x2, y2],
                           fill=(R, G, B))
        elif figura == 2:  # ellipse
            draw.ellipse([x0, y0, x1, y1],
                         fill=(R, G, B))
        elif figura == 3:  # circle
            draw.ellipse([x0, y0, x2, y2],
                         fill=(R, G, B))
        elif figura == 4:  # random polygon
            polygon_vertex = 2 * random.randint(3, 8)
            for vertex in range(polygon_vertex):
                polygon.append(random.randint(0, width))
            draw.polygon(xy=polygon, fill=(R, G, B))
        font = ImageFont.truetype("arial.ttf", 20)
        draw.text([30, 960], text='@' + myusername + ' painted this for @' + mention_username, fill=(0, 0, 0), font=font)

    del draw
    img.save('respuesta.png')



def reply_to_tweets():
    print("retrieving and replying to tweets...")
    last_seen_id = retrieve_last_seen_id(file_name)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")

    for mention in reversed(mentions):
        print(str(mention.id) + " - " + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, file_name)

        if ("#red" in mention.full_text.lower()):
            crear_respuesta(102, 255, 0, 102, 0, 102, 'red', mention.user.screen_name)
            print("responding back with a red painting...")
            img = ('respuesta.png')
            status = ("@" + mention.user.screen_name + " Here's your red painting :D " + 'https://twitter.com/' +
                      mention.user.screen_name + '/status/' + str(mention.id))
            api.update_with_media(img, status)
            print('Tweet posted!')

        elif ("#yellow" in mention.full_text.lower()):
            crear_respuesta(153, 255, 153, 255, 0, 153, 'yellow', mention.user.screen_name)
            print("responding back with a yellow painting...")
            img = ('respuesta.png')
            status = ("@" + mention.user.screen_name + " Here's your yellow painting :D " + 'https://twitter.com/' +
                      mention.user.screen_name + '/status/' + str(mention.id))
            api.update_with_media(img, status)
            print('Tweet posted!')

        elif ("#green" in mention.full_text.lower()):
            crear_respuesta(0, 102, 153, 255, 0, 178, 'green', mention.user.screen_name)
            print("responding back with a green painting...")
            img = ('respuesta.png')
            status = ("@" + mention.user.screen_name + " Here's your green painting :D " + 'https://twitter.com/' +
                      mention.user.screen_name + '/status/' + str(mention.id))
            api.update_with_media(img, status)
            print('Tweet posted!')

        elif ("#blue" in mention.full_text.lower()):
            crear_respuesta(0, 153, 0, 153, 153, 255, 'blue', mention.user.screen_name)
            print("responding back with a blue painting...")
            img = ('respuesta.png')
            status = ("@" + mention.user.screen_name + " Here's your blue painting :D " + 'https://twitter.com/' +
                      mention.user.screen_name + '/status/' + str(mention.id))
            api.update_with_media(img, status)
            print('Tweet posted!')

        elif ("#blackandwhite" in mention.full_text.lower()):
            crear_respuesta(20, 255, 20, 255, 20, 255, 'bw', mention.user.screen_name)
            print("responding back with a black and white painting...")
            img = ('respuesta.png')
            status = ("@" + mention.user.screen_name + " Here's your black and white painting :D " + 'https://twitter.com/' +
                      mention.user.screen_name + '/status/' + str(mention.id))
            api.update_with_media(img, status)
            print('Tweet posted!')


while True:
    try:
        crear_imagen()
        hora = int(time.strftime('%H'))
        if hora == hour_to_post:
            api.update_with_media('cuadro.png')
            print('Posted a painting!')
            hour_to_post += 4
            if hour_to_post > 23:
                hour_to_post = 0
        reply_to_tweets()
        time.sleep(30)

    except tweepy.TweepError as e:
        print(e.reason)