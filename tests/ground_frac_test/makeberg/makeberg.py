#!/usr/bin/env python

from netCDF4 import Dataset  
import numpy as np 
import math
#import os
from pylab import *
#import pdb
import netCDF4 as nc

nx = 30
ny = 30
New_ice_thickness_filename='testberg.nc'
grid_res = 1.e3 #1 km 
grid_area = grid_res * grid_res
h_ice = 300.0

New_ice_thickness_filename='testtabularberg.nc'
g=Dataset(New_ice_thickness_filename,'w') # w if for creating a file

g.createDimension('nx',nx)
g.createDimension('ny',ny)
thick_h=g.createVariable('thick','f8',('ny','nx'))
area_h=g.createVariable('area','f8',('ny','nx'))
lat_h=g.createVariable('lat','f8','ny')
lon_h=g.createVariable('lon','f8','nx')
#lat_h=g.createVariable('lat','f8',('ny','nx'))
#lon_h=g.createVariable('lon','f8',('ny','nx'))

thick_h.units = 'm'
thick_h.standard_name = 'ice shelf thickness'
area_h.units = 'm2'
area_h.standard_name = 'ice shelf area'
lon_h.unit = 'm'
lon_h.standard_name = 'longitude'
lat_h.unit = 'm'
lat_h.standard_name = 'latitude'



#g.variables['thick'][:]=h_ice
g.variables['area'][:,:]=grid_area

#create a circular tabular berg centered on the following coords (km)
cy = 3.5e3
cx = 15.0e3
xl = 8.e3 #7.0e3 #5.0e3
yl = 4.e3 #5.0e3
xmin=cx-xl/2
xmax=cx+xl/2
ymin=cy-yl/2
ymax=cy+yl/2
maxh=h_ice
minh=300 #100
slopedist=sqrt((xl/2)**2 + (yl/2)**2)
slope=(minh-h_ice)/slopedist

#cx2 = 15.5e3

for i in range(nx):

        tx = float(i) * grid_res 
        g.variables['lon'][i] = tx
        
        for j in range(ny):
               
                ty = float(j) * grid_res

                # dist = sqrt((tx-cx)*(tx-cx) + (ty-cy)*(ty-cy))
                # if (dist <1.e3): #or dist2<1.e3):
                #         g.variables['thick'][i,j]=h_ice
                if (tx>=xmin and tx<=xmax and ty>=ymin and ty<=ymax):
                        dist = sqrt((tx-cx)*(tx-cx) + (ty-cy)*(ty-cy))                         
                        g.variables['thick'][i,j]=slope*dist+h_ice
                                               
                else:
                        g.variables['thick'][i,j]=0.0

                        

for j in range(ny):
        g.variables['lat'][j] = float(j) * grid_res 

print('Creating file: ' , New_ice_thickness_filename)

g.sync()
g.close()

        