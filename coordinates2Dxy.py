# class Point:
#     def __init__(self,x,y):
#         self.x_cod = x
#         self.y_cod = y
#     def __str__(self):
#         return '<{},{}>'.format(self.x_cod,self.y_cod)
#
#     def euchidean_distance(self, other):
#         return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5
#
#     def distance_from_origin(self):
#         # return (self.x_cod**2+self.y_cod**2)**0.5
#         return self.euchidean_distance(Point(0, 0))
#
# class Line:
#     def __init__(self,A,B,C):
#         self.A =A
#         self.B =B
#         self.C=C
#     def __str__(self):
#         return '{}x+{}y+{}=0'.format(self.A,self.B, self.C)
#
#     def point_on_Line(self, point):
#         if self.A*point.x_cod + self.B*point.y_cod +self.C == 0:
#             return "Line and point same"
#         else:
#             return "not same"
#
#
#
#
#
# p1 = Point(1, 1)
# p2 = Point(5, 6)
#
# print(p1.euchidean_distance(p2))
# print(p1.distance_from_origin())
#
# l1= Line(1,1,-2)
# print(l1.point_on_Line(p1))
# print(l1)



# TODO: Practice
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line/short path bola diba

class Point:
    def __init__(self, x,y):
        self.x_cod = x
        self.y_cod = y
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def distance_between_2_point(self,other):
        return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)*0.5

    def distance_from_origin(self):
        return self.distance_between_2_point(Point(0,0)) #self means = p1 obj , obj ka Bollam (0,0) origin thaka tomar distance


class Line:
    def __init__(self,A,B,C):
        self.A_line = A
        self.B_line = B
        self.C_line = C

    def __str__(self):
        return "{}x+{}y+{}=0".format(self.A_line,self.B_line,self.C_line)

    def point_on_line(self , point):
        if self.A_line*point.x_cod + self.B_line*point.y_cod + self.C_line ==0:
            return "same line on Point"
        else:
            return "not same point"

    def shortest_path_line_point(self, point):
        return abs(self.A_line*point.x_cod+self.B_line*point.y_cod+self.C_line)/((self.A_line)**2+(self.B_line)**2)**0.5


    def twoline_intersention(self,point, point2):
        if self.A_line*point.x_cod + self.B_line*point.y_cod + self.C_line ==self.A_line*point2.x_cod + self.B_line*point2.y_cod + self.C_line:
            return "same line"
        else:
            return "not same 2 line"


# TODO: p1 obj
p1 = Point(1,4)
p2 = Point(1,4)
print(p1)
print(p2)
print(p1.distance_between_2_point(p2))
print(p1.distance_from_origin())
# TODO: p1 obj

l1 = Line(3,4,5)
print(l1)
print(l1.point_on_line(p1))
print(l1.shortest_path_line_point(p1))

print(l1.twoline_intersention(p1,p2))