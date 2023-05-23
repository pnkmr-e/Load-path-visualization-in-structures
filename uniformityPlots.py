import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('P:\\nobackup\\KBEIMP\\Ram_Santhosh\\Plate_With_Hole\\VTK_trials\\Trial10_1')
os.listdir()

csv_data = np.array(pd.read_csv('principal_streamline_85.csv'))

XYZ = csv_data[:,9:12]
Ustar = csv_data[:,13]

LengthInc = np.zeros(len(csv_data))
LengthInc[1:] = np.sqrt( np.sum((XYZ[1:] - XYZ[:-1])**2 , 1) )
streamlineCoord = np.array( [ np.sum(LengthInc[:i+1]) for i in range(len(LengthInc)) ] )

s = streamlineCoord/streamlineCoord[-1]  # normalised streamline coordinate

###     Polynomial fitting      ###
# Making a sufficient order polynomial fit for curvature values

p = np.polyfit(s,Ustar,12)
sfit = np.linspace(0,1,101)
Ustarfit = np.polyval(p,sfit)

###     Uniformity plot     ###
fig,ax1 = plt.subplots(figsize=(12,8))

color = 'tab:blue'
ax1.plot(sfit,Ustarfit, color=color, linewidth=1.4)
ax1.set_xlabel('s', fontsize=14)
ax1.set_ylabel('U*', color=color, fontsize=14)
ax1.set_title('Uniformity & Continuity plots', fontsize=16)
ax1.set_xlim([0,1])
ax1.set_ylim([0,1])
ax1.tick_params(axis ='y', labelcolor = color)

ax1.plot([0,1],[0,1],'-k',linewidth=0.1)

#plt.show()

###     Continuity plot     ###
ds  = np.gradient(sfit)
dds = np.gradient(ds)
dy  = np.gradient(Ustarfit)
ddy = np.gradient(dy)
num   = ds * ddy - dds * dy
denom = ds * ds  + dy  * dy
denom = denom**(3/2)
curvUstar = num / denom

color = 'tab:red'
ax2 = ax1.twinx()
ax2.plot(sfit,curvUstar,'-r', color=color, linewidth=1.4)
ax2.set_ylabel('Curvature', color=color, fontsize=14)
ax2.set_ylim([-10,10])
ax2.tick_params(axis ='y', labelcolor = color)

ax2.plot([0,1],[0,0],'k',linewidth=0.1)


plt.show()
