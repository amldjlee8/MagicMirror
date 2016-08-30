# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json
key = '7047852fabf9ea82'

def getCurWeatInfo():
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/UK/London.json'
    f = urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string.decode())
    weather = parsed_json['current_observation']['weather']
    temperature = str(parsed_json['current_observation']['temp_c']) + '°C'
    # feelLikeTemp = 'Feels Like %s°C' %(parsed_json['current_observation']['feelslike_c'])
    f.close()
    return weather, temperature