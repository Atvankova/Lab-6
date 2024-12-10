class Firearms:
    def __init__(self, number_of_cartridges, rate_of_fire, shooting_range):
        self.number_of_cartridges = number_of_cartridges
        self.rate_of_fire = rate_of_fire
        self.shooting_range = shooting_range

    def empty_magazine_time(self):
        if self.rate_of_fire <= 0:
            return "Скорострельность должна быть больше 0."
        time_to_empty = self.number_of_cartridges / self.rate_of_fire
        return f"Магазин опустеет за {time_to_empty:.2f} секунды."

    def fire_rate_to_range_ratio(self):
        if self.shooting_range <= 0:
            return "Дальность должна быть больше 0."
        ratio = self.rate_of_fire / self.shooting_range
        return f"Соотношение скорострельности к дальности: {ratio:.2f}."


class AssaultRifle(Firearms):
    def __init__(self, number_of_cartridges, rate_of_fire, shooting_range, automatic_mode):
        super().__init__(number_of_cartridges, rate_of_fire, shooting_range)
        self.automatic_mode = automatic_mode

    def describe(self):
        mode = "автоматический" if self.automatic_mode else "полуавтоматический"
        return f"Режим стрельбы: {mode}."


class SniperRifle(Firearms):
    def __init__(self, number_of_cartridges, rate_of_fire, shooting_range, scope_magnification):
        super().__init__(number_of_cartridges, rate_of_fire, shooting_range)
        self.scope_magnification = scope_magnification

    def describe(self):
        return f"Кратность увеличения прицела: {self.scope_magnification}x."


ak47 = AssaultRifle(number_of_cartridges=30, rate_of_fire=600, shooting_range=300, automatic_mode=True)
print(ak47.empty_magazine_time())
print(ak47.fire_rate_to_range_ratio())
print(ak47.describe())


m24 = SniperRifle(number_of_cartridges=5, rate_of_fire=60, shooting_range=1000, scope_magnification=10)
print(m24.empty_magazine_time())
print(m24.fire_rate_to_range_ratio())
print(m24.describe())