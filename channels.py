import json
import re
from urllib.request import urlopen

import config
import utils

def get_channel(chid, audio_template_id=config.DEFAULT_LIVE_AUDIO_TEMPLATE_ID,
		qual=config.QUALITY):
	url = utils.get_url('channels/' + str(chid),
		{'format': 'json',
		 'liveaudiotemplateid': audio_template_id,
		 'audioquality': qual})
	print(url)
	res = urlopen(url)
	return json.loads(res.read().decode('utf-8'))

def get_live_audio_url(chid, audio_template_id=config.DEFAULT_LIVE_AUDIO_TEMPLATE_ID,
		qual=config.QUALITY):
	channel = get_channel(chid, audio_template_id, qual)
	return channel['channel']['liveaudio']['url']
