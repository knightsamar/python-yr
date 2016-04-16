#!/usr/bin/env python2

from yr.libyr import Yr

weather = Yr(location_name=u'Norge/Telemark/Skien/Skien')
now = weather.now(as_json=True)

print now
