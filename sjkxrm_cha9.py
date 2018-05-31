import requests
import json
from dateutil.parser import parse
from collections import Counter



endpoint = 'https://api.github.com/users/joelgrus/repos'
repos = json.loads(requests.get(endpoint).text)#json.load() takes a file object with a read method and json.loads() takes a strings
dates = [parse(repo['created_at']) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

last_5_repos = sorted(repos, key=lambda r:r['created_at'],
                      reverse=True)[:5]
last_5_languages = [repo['language'] for repo in last_5_repos]

print(last_5_languages)



