#!/usr/bin/env python

import argparse

import channels
import config

def parse_args():
	parser = argparse.ArgumentParser()

	args = parser.parse_args()

	return args

def main():
	args = parse_args()

	print('This is srpi v{0}'.format(config.VERSION))

	channels.get_channels(132)

if __name__ == '__main__':
	main()
