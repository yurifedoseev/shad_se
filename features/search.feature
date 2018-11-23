Feature: пример как работает BDD

  Scenario: Поиск ШАД в Янедксе
     Given yandex main page
     When we search "ШАД"
     Then first result is "yandexdataschool.ru"