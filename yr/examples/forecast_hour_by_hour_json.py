#!/usr/bin/env python2

from yr.libyr import Yr

weather = Yr(location_name=u'Norway/Rogaland/Stavanger/Stavanger', forecast_link=u'forecast_hour_by_hour')

for forecast in weather.forecast(as_json=True):
    print forecast
