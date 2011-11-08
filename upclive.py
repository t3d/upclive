#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

__license__ = 'GPL 3'
__copyright__ = '2011, Tomasz Długosz <tomek3d@gmail.com>'

vlc_opts = '--rtsp-tcp --rtsp-wmserver --rtsp-caching=5000 --clock-synchro=0'

vlc_bin = 'vlc'

channels = [
  ('Animal Planet', 'rtsp://stream.livetv.chello.pl/Animal'),
  ('Discovery', 'rtsp://stream.livetv.chello.pl/Discovery'),
  ('CNN', 'rtsp://stream.livetv.chello.pl/CNN'),
  ('TVN 24', 'rtsp://stream.livetv.chello.pl/TVN24'),
  ('Mini Mini', 'rtsp://stream.livetv.chello.pl/MiniMini'),
  ('teletoon+', 'rtsp://stream.livetv.chello.pl/ZigZap'),
  ('National Geographic', 'rtsp://stream.livetv.chello.pl/NATGEO')
  ]

for channel_name, channel_url in channels:
	print channel_name, channel_url
	os.system( vlc_bin + ' ' + vlc_opts + ' ' + channel_url)
