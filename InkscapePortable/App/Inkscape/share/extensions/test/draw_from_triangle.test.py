#!/usr/bin/env python

# This is only the automatic generated test file for ../draw_from_triangle.py
# This must be filled with real tests and this commentary
# must be cleared.
# If you want to help, read the python unittest documentation:
# http://docs.python.org/library/unittest.html

import sys
sys.path.append('..') # this line allows to import the extension code

import unittest
from draw_from_triangle import *

class Draw_From_TriangleBasicTest(unittest.TestCase):

  #def setUp(self):

  def test_run_without_parameters(self):
    args = [ 'minimal-blank.svg' ]
    e = Draw_From_Triangle()
    e.affect( args, False )
    #self.assertEqual( e.something, 'some value', 'A commentary about that.' )

if __name__ == '__main__':
  unittest.main()
