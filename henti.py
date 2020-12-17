from hentai import Hentai
from hentai import Format

class Numbers:
    def __init__(self, number):
        self.sauce = Hentai(number)

    def title(self):
        title = self.sauce.title(Format.Pretty)
        return title
"""
    def artist(self):
        artist = str(Hentai(sauce).artist).split(', ')[2]  # name='artist'
        name = artist[6:-1]  # just the artist's name
        return name

    def tags():
        # get a henti's tags
        pass
    
    def get_title(sauce): 
        # get hentai title in readable format
        title = str(Hentai(sauce).title(Format.Pretty))
        artist = get_artist(sauce)
        r = "{title} ({sauce}) by {artist}\nhttps://nhentai.net/g/{sauce}/".format(title=title, artist=artist, sauce=sauce)
        return r
"""
# print(Numbers(177013).title())
# print(Numbers.title(177013))
# print(Numbers.title(177013))
# print(x.title())
