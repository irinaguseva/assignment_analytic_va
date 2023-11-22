import requests

api_key = "НАШ_API_KEY"
# А вот мой рабочий ключ 2d9f52c92f884811bb74626a06fd5df5

base_url = "https://api.weatherbit.io/v2.0/current"

city = input("Введите название города: ")
params = {"city": city, "key": api_key}
response = requests.get(base_url, params=params)

if response.status_code == 200:
    data = response.json()
    if data["count"] != 0:
        weather_data = data["data"][0]
        print("Погода в городе", city)
        print("Температура:", weather_data["temp"], "°C")
        print("Ощущается как:", weather_data["app_temp"], "°C")
        print("Скорость ветра:", weather_data["wind_spd"], "м/с")
        print("Направление ветра:", weather_data["wind_cdir_full"])
        print("Давление:", weather_data["pres"], "мм рт. ст.")
        print("Влажность:", weather_data["rh"], "%")
        print("Облачность:", weather_data["clouds"], "%")
        print("Время обновления данных:", weather_data["ob_time"])
    else:
        print("Данные о погоде для города", city, "не найдены")
else:
    print("Ошибка при получении данных о погоде")
