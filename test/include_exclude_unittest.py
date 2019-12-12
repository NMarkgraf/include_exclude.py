#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
  Quick-Pandoc-Filter unit test: include_exclude_unittest.py

  (C)opyleft in 2019 by Norman Markgraf (nmarkgraf@hotmail.com)

  Release:
  ========
  0.1   - 04.01.2019 (nm) - Erste Version


  WICHTIG:
  ========
    Benoetigt python3 !
    -> https://www.howtogeek.com/197947/how-to-install-python-on-windows/
    oder
    -> https://www.youtube.com/watch?v=dX2-V2BocqQ

  RUN THE TESTS:
  ==============
  Um die unit tests auszuführen kann man im Terminal den Befehl

    > python3 -m unittest discover -s test/ -p *_unittest.py

  im Hauptverzeichnis des Projektes eingeben!

  Lizenz:
  =======
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

  
  "Errare (Errasse) humanum est, sed in errare (errore) perseverare diabolicum."

    -- Cicero

'''

# import sys
import unittest
import io

# sys.path.append('..')
from include_exclude import *
 

class IncludeExcludeTest(unittest.TestCase):

    def test_intersection1(self):
        lst1 = []
        lst2 = []
        self.assertFalse(intersection_not_empty(lst1, lst2))


    def test_intersection2(self):
        lst1 = ["*"]
        lst2 = []
        self.assertFalse(intersection_not_empty(lst1, lst2))


    def test_intersection3(self):
        lst1 = []
        lst2 = ["*"]
        self.assertFalse(intersection_not_empty(lst1, lst2))


    def test_intersection4(self):
        lst1 = ["*"]
        lst2 = ["*"]
        self.assertTrue(intersection_not_empty(lst1, lst2))

 
if __name__ == "__main__":
    unittest.main()
