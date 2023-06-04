def nearest_neighbor(neighbors, you):
    def calculate_distance(c1,c2):
        return ((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)**0.5

    distance = []

    for i in neighbors:
        distance.append(calculate_distance(you,i))

    neighbors_index,distance_value = sorted(list(enumerate(distance)),key=lambda x:x[1])[0]

    print("Nearest neighbor is ", neighbors_index, "at distance", distance_value )


neighbors = [
   [62,76],
    [45,78],
    [67,90],
    [2,4]
]

you = [-9,7]

nearest_neighbor(neighbors, you)