''' Shading Module '''
import numpy
from LightSource import LightSource
from ColorHelpers import ColorHelpers
from tkinter import Tk, Tcl


class Shading(object):
    ''' Polygon's shading class '''

    def __init__(self, polygon, light_source=LightSource(0, -300, -300)):
        self.polygon = polygon
        self.light_source = light_source
        self._apply_shading()

    def _apply_shading(self):
        # Calc light ray
        light_source_vector = self.light_source.get_vector()
        # Calc face normal
        faces_normal_vectors = self.polygon.get_faces_normal_vectors()

        i = 0
        for normal in faces_normal_vectors:
            # Calc reflextion intensity
            max_value = numpy.linalg.norm(light_source_vector)*numpy.linalg.norm(normal)
            reflection_intensity = numpy.dot(light_source_vector, normal)/max_value

            if reflection_intensity < 0:
                reflection_intensity = 0

            # Calc new rgb
            color = ColorHelpers().get_color(i)
            (r, g, b) = (int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))
            nr = int(reflection_intensity*r)
            ng = int(reflection_intensity*g)
            nb = int(reflection_intensity*b)

            # Apply new rgb
            new_color = "#%0.2x%0.2x%0.2x" % (nr, ng, nb)
            ColorHelpers().update_color(new_color, i)
            i += 1
     
        # self.polygon.draw_polygon()

        return self.polygon

    def get_light_position(self):
        return self.light_source.get_vector()
