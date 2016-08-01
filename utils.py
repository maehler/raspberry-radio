from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urljoin, urlencode

import config

'''
Get a api.sr.se URL
'''
def get_url(func, args=None):
	if args is None:
		argtuple = ()
	elif type(args) is tuple or type(args) is list:
		argtuple = tuple(args)
	elif type(args) is dict:
		argtuple = tuple(args.items())
	else:
		raise TypeError('args needs to be a sequence of two-tuples or a dict')

	url = urljoin(config.BASE_URL, func) + '?' + urlencode(argtuple)

	try:
		statuscode = urlopen(url).getcode()
	except HTTPError:
		raise

	return url
