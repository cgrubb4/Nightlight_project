#part 2 of project
import arcpy  
from arcpy import env  
from arcpy.sa import *  
  
# Set environment settings  
arcpy.env.workspace = r"C:\Data\Out"  
  
# Set local variables  
  
statsList=[] 
  
# Get a list of the rasters in the workspace  
rasters = arcpy.ListRasters("*.tif")
# confirmation step that path is set correctly
statsList=rasters
print statsList

for i in statsList:
    ave=arcpy.GetRasterProperties_management(i, "MEAN")
    std=arcpy.GetRasterProperties_management(i,"STD")
    print "For " +i + " Ave value is %s " %ave + " and STD is %std" %std
