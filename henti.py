from hentai import Hentai
from hentai import Format

def find_title(sauce): 
    # get hentai title in readable format
    henti_title = str(Hentai(sauce).title(Format.Pretty))
    return henti_title
