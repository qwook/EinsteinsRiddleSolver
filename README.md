
Einstein's Riddle Solver
========================
Solves Einsten's Riddle  

Useage
------
You must have python installed.  
Run this command in the terminal to start the riddle solver:  
`python einstein.py`  
The script will then print the output to the terminal.


Methodology:
------------
An `attribute` can be `House #1's Color` or `House #2's Drink`.  
An `attribute value` can be `Drinks Tea` or `Keeps Dogs`.  
  
I first assume that every house contains every single `possible`  
attribute value.  
  
When a house is conclusive with an attribute, or there is only 1  
`possible` attribute for that house, then that attribute is marked  
as `determined`.  
  
The possibilities of the house `evolve` over time,  
as the rules and process of elimination are iteratively applied  
to each house.  
The process of elimination sees if a house has an attribute that  
none of the other houses have, then marks the attribute as  
`determined`.  
  
This loops until each house has a possibility of only  
1 attribute, and thus `determined`.  


Post Mortem:
------------
This would have been better if I made the attributes an array  
instead of defining them as instance variables.  
  
That way the code would be much shorter  
and I can just iterate through the array,  
rather than repeating the same lines of code over and over.  
  
Perhaps I'll remake this script to use attributes array,  
but that will be another day.  
  
License
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