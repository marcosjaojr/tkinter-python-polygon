from tkinter import Tk

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
    '#8BC34A',
    '#03A9F4',
    '#795548',
    '#BBDEFB',
    '#66BB6A',
    '#9E9E9E',
    '#90A4AE',
    '#3F51B5'
]

class ColorHelpers():

    def __init__(self, colors=COLORS):
        self.colors = colors

    def get_color(self, i):
        return self.colors[i]

    def update_color(self, new_color, position):
        self.colors[position] = new_color
