# -*- coding: utf-8 -*-

from urllib.request import urlopen
import json
key = '7047852fabf9ea82'

def getCurWeatInfo():
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/UK/London.json'
    f = urlopen(url)
    json_string = f.read()
    parsed_json = json.loads(json_string.decode())
    weatStat = parsed_json['current_observation']['weather']
    temperature = str(parsed_json['current_observation']['temp_c']) + 'Â°C'
    # feelLikeTemp = 'Feels Like %sÂ°C' %(parsed_json['current_observation']['feelslike_c'])
    f.close()
    return weatStat, temperature

def getIcon(weatStat):
    iconPath = 'WeatherIcons/unknown.pgm'
    possibleStat= {
        'drizzle':'drizzle.pgm',
        'rain':'rain.pgm',
        'snow':'snow.pgm',
        'ice':'snow.pgm',
        'hail':'hail.pgm',
        'mist':'mistFog.pgm',
        'fog':'mistFog.pgm',
        'thunderstorm':'thunder.pgm',
        'overcast':'overcast.pgm',
        'clear':'clear.pgm',
        'cloudy':'cloudy.pgm'
    }
    for status in possibleStat:
        if status in weatStat.lower():
            iconPath = 'WeatherIcons/' + possibleStat[status]

    return iconPath

if __name__ == '__main__':
    print(getIcon('Thunderstorm and Rain'))