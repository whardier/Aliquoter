#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""Aliquoter"""

__name__ = "aliquoter"
__author__ = 'Shane R. Spencer'
__email__ = "shane@bogomip.com"
__license__ = 'None'
__copyright__ = '2012 Shane R. Spencer'
__version__ = '0.0.1'
__status__ = "Prototype"
__description__ = "Aliquot Mogrifier"

from collections import namedtuple

class Point(namedtuple('Point', ['lat', 'long'])):
    __slots__ = ()

class Quad(namedtuple('Quad', ['nw', 'sw', 'ne', 'se'])):
    __slots__ = ()

def average_points_together(point1, point2):
    _lat = (point1.lat + point2.lat) / 2.0
    _long = (point1.long + point2.long) / 2.0
    return Point(lat=_lat, long=_long)

def aliquot(quad, aliquots):
    """Return a quad based on a list of aliquot references.

    Ex: aliquot(
            Quad(
                nw=Point(lat=61, long=-12),
                ne=Point(lat=61, long=-11),
                se=Point(lat=60, long=-11),
                sw=Point(lat=60, long=-12),
            ),
            ['E2'], #Or just E.
        )
    """

    #Define these now
    _quad = quad
    _nw = quad.nw
    _ne = quad.ne
    _sw = quad.sw
    _se = quad.se    

    for aliquot in aliquots:
        _aliquot = aliquot.upper()
        for d in _aliquot: #'SW'
            if not d in ['N', 'S', 'E', 'W']:
                continue
            if d == 'N':
                _sw = average_points_together(quad.nw, quad.sw)
                _se = average_points_together(quad.ne, quad.se)
            elif d == 'S':
                _nw = average_points_together(quad.nw, quad.sw)
                _ne = average_points_together(quad.ne, quad.se)
            elif d == 'E':
                _nw = average_points_together(quad.nw, quad.ne)
                _sw = average_points_together(quad.sw, quad.se)
            elif d == 'W':
                _ne = average_points_together(quad.nw, quad.ne)
                _se = average_points_together(quad.sw, quad.se)

            quad = Quad(nw=_nw, ne=_ne, sw=_sw, se=_se)

    return quad
