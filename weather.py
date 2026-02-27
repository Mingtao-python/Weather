import requests

icons = {
    0: "☀️ Clear sky",
    1: "🌤️ Mainly clear",
    2: "⛅ Partly cloudy",
    3: "☁️ Overcast",
    45: "🌫️ Fog",
    48: "🌫️ Depositing rime fog",
    51: "🌦️ Light drizzle",
    53: "🌦️ Moderate drizzle",
    55: "🌧️ Dense drizzle",
    56: "🌧️ Freezing drizzle",
    57: "🌧️ Freezing drizzle (dense)",
    61: "🌧️ Light rain",
    63: "🌧️ Moderate rain",
    65: "🌧️ Heavy rain",
    66: "🌧️ Freezing rain",
    67: "🌧️ Freezing rain (heavy)",
    71: "🌨️ Light snow",
    73: "🌨️ Moderate snow",
    75: "❄️ Heavy snow",
    77: "❄️ Snow grains",
    80: "🌧️ Rain showers",
    81: "🌧️ Rain showers (moderate)",
    82: "🌧️ Rain showers (violent)",
    85: "🌨️ Snow showers",
    86: "🌨️ Snow showers (heavy)",
    95: "⛈️ Thunderstorm",
    96: "⛈️ Thunderstorm with hail",
    99: "⛈️ Thunderstorm with heavy hail"
}

def location():
    global lat
    global lon
    global timezone
    global country
    while True:
        try:
            city = input("city name> ").strip()
            city = "".join(city.split())
            data = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}', timeout = 6)

            if data.status_code != 200:
                print('Bad API responce.\nPlease try again in a moment.')

            data = data.json()

            if "results" not in data or data["results"] is None:
                print('❌ City not found. Check spelling and try again.')
                continue

            else:
                data = data['results'][0]
                if "latitude" not in data or "longitude" not in data or "timezone" not in data or "country" not in data:
                    print("❌ This location is too vague or incomplete. Try a specific city name instead of a region or country.")
                    continue
                lat = data['latitude']
                lon = data['longitude']
                timezone = data['timezone']
                country = data['country']
                break

        except requests.exceptions.Timeout:
            print('Time out. Please try again')
        except Exception as e:
            print(f'Unexpected error: {e}\nPlease try again!')
while True:
    location()
    try:
        _3 = requests.get("https://api.open-meteo.com/v1/forecast" f"?latitude={lat}&longitude={lon}" "&hourly=temperature_2m" "&timezone=auto" '&current_weather=true').json().get('current_weather')
        if not _3:
            print("Weather data unavailable.")
            continue
        wc = _3.get('weathercode')

        print('temperature: ' + str(_3['temperature']))
        print('wind speed: ' + str(_3['windspeed']))
        print(f'timezone: {timezone}')
        print(f'country: {country}')
        print(f"weather: {icons.get(wc, f'Unknown ({wc})')}")

        direction = ['↗north to east ', '↘east to south ', '↙south to west ', '↖west to north ', 'north  ⬆', 'east ➡', 'south ⬇', 'west ⬅']

        wd = _3['winddirection']

        if 0 < wd < 90:
            print(direction[0], wd, '°')
        elif 90 < wd < 180:
            print(direction[1], wd - 90, '°')
        elif 180 < wd < 270:
            print(direction[2], wd - 180, '°')
        elif 270 < wd < 360:
            print(direction[3], wd - 270, '°')
        elif wd in [0, 360]:
            print(direction[4])
        elif wd == 90:
            print(direction[5])
        elif wd == 180:
            print(direction[6])
        elif wd == 270:
            print(direction[7])
        else:
            print('''Winddirection service was failed to acess!---------
Please try again!---------
''')
        
    except Exception as e:
        print(f'something went wrong-- Please check the internet or any typo\nError: {e}')
