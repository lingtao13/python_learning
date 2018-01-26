# -*- coding: UTF-8 -*-

import requests


from collections import  Iterable, Iterator

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities= cities
        self.index = 0

    def getWether(self,city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s:%s,%s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.getWether(city)

class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'北京',u'上海',u'长沙',u'湘潭']):
    print(x)