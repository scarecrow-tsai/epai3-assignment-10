from polygon import Polygon


class PolygonSeq:
    def __init__(self, vertices, radius):
        self.vertices = vertices
        self.radius = radius

        if self.vertices < 3:
            raise ValueError(
                "Number of edges/vertices should be equal to or greater than 3"
            )

    def __len__(self):
        return self.vertices

    def __getitem__(self, vertices):
        if isinstance(vertices, int):
            if vertices < 0:
                vertices = self.vertices + vertices
            elif vertices < 0 or vertices >= self.vertices:
                raise IndexError
            else:
                return Polygon(num_vertices=vertices, circum_radius=self.radius)

    def __repr__(self):
        """
        repr method for PolygonSeq class.
        """
        return f"PolygonSeq(1 - {self.vertices}, {self.radius})"

    def __str__(self):
        """
        str method for PolygonSeq class.
        """
        return f"PolygonSeq(vertices: {1, self.vertices},radius={self.radius})"

    def get_maxeff_poly(self):
        """
        Get polygon with max efficiency.
        Efficiency = area:perimeter
        """
        eff_list = []
        for p in self:
            if p.num_vertices >= 3:
                eff_list.append(p.area / p.perimeter)

        return max(eff_list), self[eff_list.index(max(eff_list))]


if __name__ == "__main__":
    ps = PolygonSeq(vertices=5, radius=5)
    print(ps)
    print(list(ps))
    print(ps[1])
    print(ps[2])
    print(ps.get_maxeff_poly())
