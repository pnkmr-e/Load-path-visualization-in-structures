#-------------------------------------------------------------------------------------
# INPUT TO BE MODIFIED FOR EVERY PROBLEM
num_streamlines = 10
ParentFolder = 'P:/nobackup/KBEIMP/Ram_Santhosh/Plate_With_Hole/VTK_trials/Trial10_1/'
VTKFileName  = 'Plate_with_hole.vtk'
#-------------------------------------------------------------------------------------
# DIRECTIONS:
#
# Change streamTracer1.SeedType.Point1 to change the streamTracer Line Source
# The streamline files are named 'streamline_<I>.csv', I in range(num_streamlines) COMMENTED OUT
# The file 'streamline_i.csv' is used to temporarily store cell data for finding the largest streamline
# The file 'largest_streamline.csv' has the point data for the longest streamline
#-------------------------------------------------------------------------------------

#### import csv reader
import csv

#### import numerical library
#import numpy as np

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
plate_with_holevtk = LegacyVTKReader(FileNames=[ParentFolder+VTKFileName])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1233, 807]

# show data in view
plate_with_holevtkDisplay = Show(plate_with_holevtk, renderView1)
# trace defaults for the display properties.
plate_with_holevtkDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

#changing interaction mode based on data extents
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [1.0, 0.5, 10000.0]
renderView1.CameraFocalPoint = [1.0, 0.5, 0.0]

# show color bar/color legend
plate_with_holevtkDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'U_star'
u_starLUT = GetColorTransferFunction('U_star')
u_starLUT.ScalarRangeInitialized = 1.0

# Properties modified on u_starLUT
u_starLUT.NumberOfTableValues = 10

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=plate_with_holevtk)

# show data in view
gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet1Display.Representation = 'Surface'

# hide data in view
Hide(plate_with_holevtk, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(gradientOfUnstructuredDataSet1Display, ('POINTS', 'Gradients', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(u_starLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
gradientOfUnstructuredDataSet1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
gradientOfUnstructuredDataSet1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Gradients'
gradientsLUT = GetColorTransferFunction('Gradients')
gradientsLUT.RGBPoints = [0.0037388897989653245, 0.231373, 0.298039, 0.752941, 1.5768434242596319, 0.865003, 0.865003, 0.865003, 3.1499479587202983, 0.705882, 0.0156863, 0.14902]
gradientsLUT.ScalarRangeInitialized = 1.0

# hide data in view
Hide(gradientOfUnstructuredDataSet1, renderView1)

# set active source
SetActiveSource(plate_with_holevtk)

# show data in view
plate_with_holevtkDisplay = Show(plate_with_holevtk, renderView1)

# show color bar/color legend
plate_with_holevtkDisplay.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(gradientOfUnstructuredDataSet1)

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=gradientOfUnstructuredDataSet1,
    SeedType='High Resolution Line Source')

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point1 = [0.0, 0.0, 0.0]

# Properties modified on streamTracer1.SeedType
streamTracer1.SeedType.Point2 = [0.0, 1.0, 0.0]
streamTracer1.SeedType.Resolution = num_streamlines-1

# Properties modified on streamTracer1
streamTracer1.InitialStepLength = 0.01
streamTracer1.MaximumStepLength = 0.02
streamTracer1.MaximumSteps = 20000
streamTracer1.MaximumStreamlineLength = 200.0

# show data in view
streamTracer1Display = Show(streamTracer1, renderView1)
# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'

# hide data in view
Hide(gradientOfUnstructuredDataSet1, renderView1)

# show color bar/color legend
streamTracer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(u_starLUT, renderView1)

# create a new 'Threshold'
threshold1 = Threshold(Input=streamTracer1)

# Properties modified on threshold1
threshold1.Scalars = ['CELLS', 'SeedIds']
threshold1.ThresholdRange = [0.0, 0.0]

# show data in view
threshold1Display = Show(threshold1, renderView1)
# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(streamTracer1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# destroy renderView1
Delete(renderView1)
del renderView1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# get layout
layout1 = GetLayout()

# place view in the layout
layout1.AssignView(0, spreadSheetView1)

# show data in view
threshold1Display = Show(threshold1, spreadSheetView1)

# Looping through seed points
FileName     = 'streamline_'
Extension    = '.csv'
#for i in range(num_streamlines):
#
#    # Properties modified on threshold1
#    threshold1.ThresholdRange = [i, i]
#
#    # update the view to ensure updated data information
#    spreadSheetView1.Update()
#
#    # export view
#    ExportView(ParentFolder+FileName+str(i)+Extension, view=spreadSheetView1)


# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(Input=threshold1)

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1)

# Properties modified on integrateVariables1Display
integrateVariables1Display.FieldAssociation = 'Cell Data'

# Initializing streamline length vector
streamlineLength = []

for i in range(num_streamlines):
    
    # Properties modified on threshold1
    threshold1.ThresholdRange = [i, i]
    
    # update the view to ensure updated data information
    spreadSheetView1.Update()
    
    # export view
    ExportView(ParentFolder+'streamline_i.csv', view=spreadSheetView1)
    
    # reading csv data
    with open(ParentFolder+'streamline_i.csv','r') as file:
        csv_data = csv.reader(file)
        csv_list = list(csv_data)
    
    # storing streamline lengths
    streamlineLength.append(float(csv_list[1][2]))

longestStreamline = streamlineLength.index(max(streamlineLength))

# Properties modified on threshold1
threshold1.ThresholdRange = [longestStreamline, longestStreamline]

# Properties modified on integrateVariables1Display
integrateVariables1Display.FieldAssociation = 'Point Data'

# show data in view
threshold1Display = Show(threshold1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# export view
ExportView(ParentFolder+'longest_streamline.csv', view=spreadSheetView1)