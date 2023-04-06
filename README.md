# Load-path-visualization-in-structures
This depository contains the scripts developed as part of my master thesis project titled "Load Path Visualization in Engine Structures". The current work utilizes the U* index to determine load paths in structures.

The description for the Mechanical APDL input files, MATLAB and Python scripts are provided below in this table.

| Sl.No. |     FileName     |  Language | Description |
| :----: | ---------------- | :-------: | ----------- |
| 1 | U_str_Pnt_Direct.inp  |    APDL   |   Computes U* values for a structure using Direct Method. Works only for point load.   |
| 2 | U_str_Dst_Direct.inp  |    APDL   |   Uses Direct Method. Allows distributed load on a single interface.   |
| 3 | U_str_Dst_Inspect.inp |    APDL   |   Uses Inspection Load Method. Allows distributed load on a single interface.   |
| 4 | U_str_MDL_Inspect.inp |    APDL   |   Uses Inspection Load Method. Allows distributed loads on multiple interfaces.   |
| 5 | create_vtk.m          |   MATLAB  |   Uses APDL mesh data and U* data to generate a .vtk file for postprocessing in Paraview.   |
| 6 | Paraview_automate.py  |   Python  |   Takes input from .vtk file to generate desired series of streamlines. Extracts streamline-wise data for all the streamlines and computes the longest streamline. |

Please note that all the files only work with 2D elements. The code will be updated in the future.
