COLORS = [
    '#00BCD4',
    '#263238',
    '#BCAAA4',
    '#ff8a80',
    '#827717',
    '#8D6E63',
    '#64DD17',
    '#C5CAE9',
    '#00796B',
    '#FF6D00',
    '#4527A0',
    '#304FFE',
    '#795548',
    '#03A9F4',
    '#8BC34A',
    '#BBDEFB',
    '#66BB6A',
    '#9E9E9E',
    '#90A4AE',
    '#3F51B5'
]

class ColorHelpers():

    def __init__(self):
        self.colors = COLORS

    def get_random_color(self):
        color = self.colors.pop(0)
        self.colors.append(color)
        return color
