''' Light Source Module '''


class LightSource(object):

    def __init__(self, light_position_x, light_position_y, light_position_z):
        self.light_position_x = light_position_x
        self.light_position_y = light_position_y
        self.light_position_z = light_position_z

    def get_module(self):
        ''' Calc light source vector's module '''
        return (self.light_position_x**2
                + self.light_position_y**2
                + self.light_position_z**2)**(1 / 2)

    def get_vector(self):
        ''' Returns light source coodinates '''
        return (self.light_position_x, self.light_position_y, self.light_position_z)
