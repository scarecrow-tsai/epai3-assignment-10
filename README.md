# Assignment 10

This is the readme for session-10. This file contains information for functions present in `polygon.py` and `polygon_seq.py`.

- Polygon class is in `polygon.py`.
- PolygonSeq class in `polygon_seq.py`.
- Both classses are tested in `main.ipynb`.

## Objectives

### Objective 1

- Create a Polygon Class:

  - where initializer takes in:
    - number of edges/vertices
    - circumradius
  - that can provide these properties:
    - edges
    - vertices
    - interior angle
    - edge length
    - apothem
    - area
    - perimeter
  - that has these functionalities:
    - a proper **repr** function
    - implements equality (==) based on # vertices and circumradius (**eq**)
    - implements > based on number vertices only (**gt**)

### Objective 2

- Implement a Custom Polygon sequence type:
  - where initializer takes in:
    number of vertices for largest polygon in the sequence
    common circumradius for all polygons
  - that can provide these properties:
    max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
  - that has these functionalities:
    functions as a sequence type (**getitem**)
    supports the len() function (**len**)
    has a proper representation (**repr**)
