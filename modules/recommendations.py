def get_recommendation(temp, weather):

    weather = weather.lower()

    if temp > 35:
        return "🥤 High temperature detected. Stay hydrated and avoid prolonged exposure to sunlight."

    elif temp < 10:
        return "🧥 Cold weather expected. Wear warm clothing before going outside."

    elif "rain" in weather:
        return "☔ Rain expected. Carry an umbrella or raincoat."

    elif "cloud" in weather:
        return "🌥 Cloudy conditions. Pleasant weather for outdoor activities."

    elif "clear" in weather:
        return "😎 Clear skies ahead. Perfect day for outdoor plans."

    return "✅ Weather conditions appear comfortable."