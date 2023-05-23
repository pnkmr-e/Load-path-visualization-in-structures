# Load-path-visualization-in-structures
This depository contains the scripts and supporting files developed as part of my master thesis project titled "Load Path Visualization in Engine Structures". The current work utilizes the U* index to determine load paths in structures.

## Background
The pursuit of lightweight and cost-effective components, without compromising the strength and safety, has always been a challenge for engineers. This is true especially in the Aerospace industry. It is crucial to identify how the loads imposed on the structure are transferred from the point of application to the support. The conventional stress-based methods are often prone to incorrect prediction of load paths due to the presence of stress concentrations. In order to circumvent this problem, the present work aims to implement the concept of U*, a stiffness based index, for the identification of load paths.

The description for the Mechanical APDL input files, MATLAB and Python scripts are provided below in this table. Sample mesh files for a simple plate with hole structure are also provided to run the input files.

| Sl.No. |     FileName     |  Language | Description |
| :----: | ---------------- | :-------: | ----------- |
| 1 | U_str_Pnt_Direct.inp  |    APDL   |   Computes U* values for a structure using Direct Method, Works only for point load   |
| 2 | U_str_Dst_Direct.inp  |    APDL   |   Uses Direct Method, Allows distributed load on a single interface   |
| 3 | U_str_Dst_Inspect.inp |    APDL   |   Uses Inspection Load Method, Allows distributed load on a single interface   |
| 4 | U_str_MDL_Inspect.inp |    APDL   |   Uses Inspection Load Method, Allows distributed loads on multiple interfaces   |
| 5 | PWH_Pnt_4npe_216.cdb  |    APDL   |   Mesh file for Point Loading case. To be used for U_str_Pnt_Direct.inp|
| 6 | PWH_Dst_4npe_478.cdb  |    APDL   |   Mesh file for Single Interface Distributed Loadng case. To be used for U_str_Dst_Direct.inp & U_str_Dst_Inspect.inp|
| 7 | PWH_MDL_4npe_478.cdb  |    APDL   |   Mesh file for Multiple Interface Distributed Loading case. To be used for U_str_MDL_Inspect.inp|
| 8 | create_vtk.m          |   MATLAB  |   Uses APDL mesh data & U* data to generate VTK file for postprocessing in Paraview   |
| 9 | Paraview_automate.py  |   Python  |   Macro in Paraview that generates desired series of streamlines, Extracts and writes data for individual streamlines into separate CSV files, Finds the longest streamline |

Please note that all the files only work with 2D elements. The code will be updated in the future.
