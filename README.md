Aliquoter
=========

Aliquot mogrifier utilizing the BLM PLSS method of quartering/halving sections.

Purpose
-------

Given a quad of point pairs (long, lat) return a quad of point pairs for a 
specific aliquot string.

This code should work on any quad in any orientation as long as north, south, 
east, west can be defined appropriately.

This code uses specific points rather than a bounding box set to 0 degrees.

Example
-------

Aliquot string: **E2SW4SW4**

Aliquot meaning: **The East half of the South West quarter of the South West quarter**

This would mean that the quad would be split up into a South West square (SW4) 
and then another South West square (SW4) and then the East half of that square 
would be returned.

<pre>
4,0                                           4,4
+-----------------------+-----------------------+
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|                       |                       |
|          S-W          |                       |
|          \ /          |                       |
+-----------+-----------+-----------------------+
|           |           |                       |
|           |           |                       |
|           |           |                       |
|    S-W    |           |                       |
|    \ /    |           |                       |
+-----*******-----------+-----------------------+
|     *     *           |                       |
|     *     *           |                       |
|     *  E  *           |                       |
|     *     *           |                       |
|     *     *           |                       |
+-----*******-----------+-----------------------+
0,0                                           0,4
</pre>

Usage
-----

Check out 'test.py'.  It represents the above example and outputs the following.

Code:

```python
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
```

In the above code the list of aliquot quarters/halves is reversed to make 
processing more straight forward.

Result:

```
Quad(
    nw=Point(lat=1.0, long=0.5),
    sw=Point(lat=0.0, long=0.5),
    ne=Point(lat=1.0, long=1.0),
    se=Point(lat=0.0, long=1.0)
)
```

