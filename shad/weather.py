import requests


def fetch_weather(city):
    """
    Json format:
    {
        "query": {
            "count": 1,
            "created": "2018-11-23T06:21:48Z",
            "lang": "en-us",
            "results": {
                "channel": {
                    "item": {
                        "condition": {
                            "code": "31",
                            "date": "Fri, 23 Nov 2018 08:00 AM MSK",
                            "temp": "25",
                            "text": "Clear"
                        }
                    }
                }
            }
        }
    }
    :return:
    """
    query = 'select item.condition from weather.forecast ' \
            'where woeid in (select woeid from geo.places(1) ' \
            'where text="{}")'.format(city)

    params = dict(q=query, format='json', env='store://datatables.org/alltableswithkeys')
    rsp = requests.get('https://query.yahooapis.com/v1/public/yql', params=params)
    return rsp


def current_weather():
    city = 'Moscow'
    rsp = fetch_weather(city)
    data = rsp.json()
    current = data['query']['results']['channel']['item']['condition']
    temp = (int(current['temp']) - 30) / 2
    result = 'Today is {t}°C in {city}, {summary}. '.format(t=temp, city=city, summary=current['text'])

    if temp < - 100:
        result += 'You are dead, sorry'
    elif temp < -20:
        result += 'Brrr, so cold - be carefault'
    elif temp < 0:
        result += 'Winter has come'
    elif temp > 30:
        result += 'So hot! Take a hat!'
    else:
        result += 'What a lovely day!'

    return result


if __name__ == '__main__':
    print(current_weather())
