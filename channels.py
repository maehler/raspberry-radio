import json
from urllib.request import urlopen

import utils

def get_channels(chid=None):
	if chid is None:
		url = utils.get_url('channels', {'format': 'json'})
	else:
		url = utils.get_url('channels/' + str(chid), {'format': 'json'})
	print(url)
	res = urlopen(url)
	print(json.loads(res.read().decode('utf-8')))
