''' Polygon Module '''
from tkinter import Canvas, BOTH, YES, ALL
import numpy
from MatrixHelpers import MatrixHelpers
from ColorHelpers import ColorHelpers
from GeometryStructure import GeometryStructure


class Polygon(MatrixHelpers):
    ''' Generic Polygon Class '''

    def __init__(self, root, bg_color='LightGoldenrod1'):
        self.root = root
        self.bg_color = bg_color
        self.init_data()
        self.create_canvas()
        self.polygon = self.rotate_along_x(0.5, self.polygon)
        self.polygon = self.rotate_along_y(0.7, self.polygon)
        self.polygon = self.rotate_along_z(1.5, self.polygon)
        self.draw_polygon()
        self.continually_rotate()

    def init_data(self):
        self.geo_structure = GeometryStructure()
        self.polygon = self.transpose_matrix(
            self.geo_structure.vertices)

    def create_canvas(self):
        ''' Create a canvas where de polygon will be draw '''
        self.canvas = Canvas(self.root, width=400, height=400,
                             background=self.bg_color)
        self.canvas.pack(fill=BOTH, expand=YES)

    def draw_polygon(self):
        ''' Draw the polygon based on a geometry structure '''
        polygon_points_to_draw_face = self.geo_structure.faces
        half_width = self.canvas.winfo_width()/2
        half_height = self.canvas.winfo_height()/2
        self.canvas.delete(ALL)
        count = 0
        for i in polygon_points_to_draw_face:
            face = []
            for j in range(len(i)-1):
                face.append(
                    self.translate_vector(self.polygon[0][i[j]-1], self.polygon[1][i[j]-1],
                                          half_width, half_height))
                face.append(
                    self.translate_vector(self.polygon[0][i[j+1]-1], self.polygon[1][i[j+1]-1],
                                          half_width, half_height))
            self.canvas.create_polygon(*face, fill=ColorHelpers().get_color(count))

            count += 1

    def continually_rotate(self):
        # self.polygon = self.rotate_along_x(0.01, self.polygon)
        # self.polygon = self.rotate_along_y(0.01, self.polygon)
        # self.polygon = self.rotate_along_z(0.01, self.polygon)
        self.draw_polygon()
        self.root.after(15, self.continually_rotate)

    def get_faces_normal_vectors(self):
        ''' Calc normal vector for each face '''
        normal_vectors = []

        for face in self.geo_structure.faces:
            a_vertice = (self.polygon[0][face[0] - 1],
                         self.polygon[1][face[0] - 1],
                         self.polygon[2][face[0] - 1])
            b_vertice = (self.polygon[0][face[1] - 1],
                         self.polygon[1][face[1] - 1],
                         self.polygon[2][face[1] - 1])
            c_vertice = (self.polygon[0][face[2] - 1],
                         self.polygon[1][face[2] - 1],
                         self.polygon[2][face[2] - 1])

            first_vector = [b_vertice[i] - a_vertice[i]
                            for i in range(len(b_vertice))]
            second_vector = [c_vertice[i] - a_vertice[i]
                             for i in range(len(c_vertice))]

            normal_vectors.append(
                list(numpy.cross(first_vector, second_vector)))

        return normal_vectors
