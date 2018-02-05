import webbrowser
from random import randint
random_page_generator = ['http://www.google.com',
                         'http://www.twitter.com','http://www.facebook.com']
y=random_page_generator[randint(0,2)]
webbrowser.open(y, new=2)
