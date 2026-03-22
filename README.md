# Weather Application

A simple command-line weather application that fetches and displays current weather information for any city in the world.

## Features

- 🌍 **City Search**: Enter any city name to get weather information
- 🌡️ **Current Weather Data**: Temperature, wind speed, and weather conditions
- 🧭 **Wind Direction**: Visual representation of wind direction with compass indicators
- 🎨 **Weather Icons**: Emoji-based weather icons for intuitive visualization
- ⏰ **Timezone Information**: Displays the timezone of the searched location
- 🌐 **Country Information**: Shows which country the city is located in

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download this repository
2. Install the required dependencies:
```bash
pip install requests
```

## Usage

Run the script:
```bash
python weather.py
```

The program will prompt you to enter a city name:
```
city name> London
```

The application will then display:
- Current temperature
- Wind speed
- Weather condition with emoji
- Wind direction with compass direction
- Timezone
- Country

### Example Output
```
temperature: 15.2
wind speed: 12.5
timezone: Europe/London
country: United Kingdom
weather: ⛅ Partly cloudy
↗north to east  45 °
```

## How It Works

1. **Geocoding**: The app uses the [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) to convert city names into geographic coordinates
2. **Weather Data**: Current weather information is retrieved from the [Open-Meteo Weather API](https://open-meteo.com/en/docs)
3. **Display**: Results are formatted with emojis and compass directions for easy reading

## Weather Code Reference

The application supports comprehensive weather codes:
- **Clear**: ☀️ Clear sky, 🌤️ Mainly clear
- **Cloudy**: ⛅ Partly cloudy, ☁️ Overcast
- **Precipitation**: 🌧️ Rain, 🌨️ Snow, 🌦️ Drizzle
- **Extreme**: ⛈️ Thunderstorm, 🌫️ Fog

## Error Handling

The application handles various error scenarios:
- **City not found**: Suggests checking spelling
- **Invalid location**: Prompts for more specific city name
- **API timeout**: Allows retry after timeout
- **Network errors**: Displays error message with connection troubleshooting

## API Services Used

- **Geocoding API**: https://geocoding-api.open-meteo.com/v1/search
- **Weather API**: https://api.open-meteo.com/v1/forecast

These are free, open-source APIs with no API key required.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests with improvements.

## Troubleshooting

**"City not found"**
- Double-check the spelling of the city name
- Try using a more specific city name (e.g., "New York" instead of just "York")

**"Bad API response"**
- Check your internet connection
- Try again after a moment (the API might be temporarily unavailable)

**"Time out"**
- This usually indicates a network connectivity issue
- Check your internet connection and try again

---

**Note**: This application requires an active internet connection to fetch weather data.
