#!/usr/bin/env python

import argparse

import channels
import config
import player

def parse_args():
	parser = argparse.ArgumentParser()

	args = parser.parse_args()

	return args

def main():
	args = parse_args()

	print('This is srpi v{0}'.format(config.VERSION))

	live_audio_url = channels.get_live_audio_url(132)

	player.play(live_audio_url)

if __name__ == '__main__':
	main()
