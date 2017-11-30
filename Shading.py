''' Shading Module '''
import numpy
from LightSource import LightSource


class Shading(object):
    ''' Polygon's shading class '''

    def __init__(self, polygon, light_source=LightSource(300, 0, 0)):
        self.polygon = polygon
        self.light_source = light_source
        self._apply_shading()

    def _apply_shading(self):
        # Calc light ray
        # Calc face normal
        # Calc reflextion intensity
        # Calc new rgb
        # Apply new rgb
        light_source_vector = self.light_source.get_vector()
        faces_normal_vectors = self.polygon.geo_structure.get_faces_normal_vectors()

        for normal in faces_normal_vectors:
            dot_product = numpy.dot(light_source_vector, normal)

        return self.polygon

    def get_light_position(self):
        return self.light_source.get_vector()
