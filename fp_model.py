class WeatherReport():
    def __init__(self, max_temp,
                min_temp, summary, raining_prob,
                icon):
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.summary = summary
        self.raining_prob = raining_prob
        self.icon = icon