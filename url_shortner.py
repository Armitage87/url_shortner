import random
from urllib.parse import urlparse
import json
import string


def check_availability(url):
    with open('urls_db.json', 'r') as main_db:
        db = json.load(main_db)
    try:
        result = db['urls'][0].get(url, None)
    except IndexError:
        return False
    if result:
        return True
    else:
        return False


def generate_shortened_url(url, no_char):
    string_colection = string.ascii_letters
    try:    
        parsed_uri = urlparse(url)
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    except Exception:
        return 'Please provide valid URL'
    check_available = True
    while check_available:
        generated_short_url = result + ''.join(random.choice(string_colection) for x in range(no_char))
        check_available = check_availability(generated_short_url)
        if not check_available:
            with open("urls_db.json") as feedsjson:
                feeds = json.load(feedsjson)
            feeds['urls'][0][generated_short_url] = url
            with open("urls_db.json", 'w') as save_feed:
                json.dump(feeds, save_feed)
            return generated_short_url


print(generate_shortened_url('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CC4QFjAA&url=http%3A%2F%2Fthelongestlistofthelongeststuffatthelongestdomainnameatlonglast.com%2Fwearejustdoingthistobestupidnowsincethiscangoonforeverandeverandeverbutitstilllookskindaneatinthebrowsereventhoughitsabigwasteoftimeandenergyandhasnorealpointbutwehadtodoitanyways.html&ei=40egUo2MGI3xoATQtIKwDQ&usg=AFQjCNHbBa5Fk4YutdUOj_D8IwpJLu7hGw&sig2=8P4ew1Yie72Ps_OQ-L5cXw&bvm=bv.57155469,d.cGU', 2))