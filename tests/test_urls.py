from nose.tools import raises

from urllib.error import HTTPError

import utils

class TestValidURLs:

	def test_channels(self):
		assert type(utils.get_url('channels')) is str

class TestInvalidURLs:

	@raises(HTTPError)
	def test_nonexistent_subapi(self):
		utils.get_url('notafunction')
