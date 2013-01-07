Aliquoter
=========

Shapefile Aliqout Mogrifier

Purpose
-------

Given a quad of point pairs (long, lat) return a quad of point pairs for a 
specific aliquot string.

Example
-------

Aliquot string: **E2SW4SW4**

Aliquot meaning: **The East half of the South West quarter of the South West quarter**

This would mean that the quad would be split up into a South West square (SW4) 
and then another South West square (SW4) and then the East half of that square 
would be returned.

<pre>
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
</pre>
