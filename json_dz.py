import json

citi =\
    {
  "cities": [
    {
      "name": "Москва",
      "population": 13149803,
      "child_cities": [
        {
          "name": "Зеленоград"
        }
      ]
    },
    {
      "name": "Санкт-Петербург",
      "population": 5597763
    },
    {
      "name": "Кемпендяй",
      "population": 357
    },
    {
      "name": "Пеледуй",
      "population": 3578
    },
    {
      "name": "Чаплыгин"
    }
  ]
}

menu_json = json.dumps(citi)

