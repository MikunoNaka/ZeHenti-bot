from hentai import Hentai
from hentai import Format

class Numbers:
    def title(self):
        title = self.sauce.title(Format.Pretty)
        return title

    def artist(self):
        artist = str(self.sauce.artist).split(', ')[2]
        name = artist[6:-1]  # just the artist's name
        return name

    def Tags(self):
        tags = []
        for tag in self.sauce.tag:
            # get names of tags and put them in a list
            tags.append(tag.name)
        print(tags)






    def __init__(self, number):
        sauce = Hentai(number)
        self.sauce = sauce

        
    
    
#     def info(self): 
        # get hentai title in readable format
#         _title = Numbers.title(self.sauce)
#         _artist = Numbers.artist(self.sauce)
#         _tags = Numbers.tags(self.sauce)
#         sauce = self.sauce
#         r = "{title} ({sauce}) by {artist}\nhttps://nhentai.net/g/{sauce}/"#.format(title=title, artist=artist, sauce=sauce)
#         return r
