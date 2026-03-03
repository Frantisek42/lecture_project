from requests import get
from datetime import datetime

tm = datetime.now()
response = get('https://www.zsnosovice.cz/')
print(response)
print(tm)