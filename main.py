''' Main Module '''
import time
from tkinter import Tk
from Polygon import Polygon
from Shading import Shading


def apply_shading(polygon):
    return Shading(polygon)

def main():
    ''' Main function '''
    root = Tk()
    apply_shading(Polygon(root))
    root.mainloop()

if __name__ == '__main__':
    main()
