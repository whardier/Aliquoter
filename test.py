from aliquoter import aliquot, Quad, Point

print aliquot(
            Quad(
                nw=Point(lat=4, long=0),
                sw=Point(lat=0, long=0),
                ne=Point(lat=4, long=4),
                se=Point(lat=0, long=4),
            ),
            ['SW', 'SW', 'E']
        )

