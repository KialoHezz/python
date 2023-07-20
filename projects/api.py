import sys
from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://itunes.apple.com/search?entity=song&limit=5&term" + sys.argv[1]

printer = PrettyPrinter()

data =  get(BASE_URL).json()  
printer.pprint(data)