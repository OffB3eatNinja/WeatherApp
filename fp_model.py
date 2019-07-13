class WeatherReport():
    def __init__(self, max_temperature,
                 min_temperature, summary, raining_prob,
                icon):
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.summary = summary
        self.raining_prob = raining_prob
        self.icon = icon