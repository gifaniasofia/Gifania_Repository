from netCDF4 import Dataset
from numpy import dtype
import numpy as np

#-----------------
# read netCDF file
#-----------------

# open a netCDF file to read
filename = "JRA/1973/anl_p125.034_vgrd.1973010100_1973013118.nc"
ncin = Dataset(filename, 'r', format='NETCDF4')
