class car(object):
    def __init__(self, color, manufacturer, model, doors):
        self.color = color;
        self.manufacturer = manufacturer;
        self.model = model;
        self.doors = doors;
    def __str__(self):
        return car(self.color, self.manufacturer, self.model, self.doors)
