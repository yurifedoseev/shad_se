from unittest.mock import MagicMock, patch
import unittest
from shad.weather import current_weather


class TestWeather(unittest.TestCase):
    def test_weather(self):
        with patch('shad.weather.fetch_weather') as mock:
            result = mock.return_value
            result.status_code = 200
            result.json = MagicMock()
            result.json.return_value = {
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
                                    "temp": "0",
                                    "text": "Clear"
                                }
                            }
                        }
                    }
                }
            }

            weather = current_weather()
            mock.assert_called_once_with('Moscow')
            assert 'Today is -15.0°C in Moscow, Clear. Winter has come' == weather


if __name__ == '__main__':
    unittest.main()
