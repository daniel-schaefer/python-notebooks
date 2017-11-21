import numpy as np
import time
import random
import matplotlib.pyplot as plt
tic   = time.time()

# Physics
xmin    =-1/2;
xmax    = 1/2;
ymin    =-1/2;
ymax    = 1/2;
Tamp    = 100;                               # amplitude
sig     = 0.1;                               # bandwidth
k       = 3;                                 # conductivité
rho     = 3000;                              # densité
c       = 1000;                              # capacité thermique

# Numerics
nx      = 101;                               # nombre de noeuds (espace)
ny      = nx;                                # nombre de noeuds (espace)
nt      = 1000;                              # nombre de pas (temps)
BC      = 2;                                 # 1: Dirichlet / 2: Neumann

# Pre-calculation
dx      = (xmax-xmin)/(nx-1);                # pas d'espace
dy      = (ymax-ymin)/(nx-1);                # pas d'espace
dt      = min(dx,dy)**2/(k/rho/c)/4.2;       # pas de temps
xn      = np.linspace(xmin,xmax,nx);         # coordonnées vertices
xc      = 0.5*(xn[0:-1]+xn[1:]);             # coordonnées centres
yn      = np.linspace(ymin,ymax,ny);         # coordonnées vertices
yc      = 0.5*(yn[0:-1]+yn[1:]);             # coordonnées centres
xc2,yc2 = np.meshgrid(xc,yc);                # maillage 2D - centres
xn2,yn2 = np.meshgrid(xn,yn);                # maillage 2D - noeuds
timep   = 0;                                 # temps initial
kn      = k*np.ones((nx,ny));                # tableau de conductivité

# Initial condition
T             = Tamp*np.exp( -xc2**2/2/sig**2 -yc2**2/2/sig**2 ); # température initiale
locations     = np.logical_and(xn2<0, yn2>0)
kn[locations] = 0.1;                               # variation de la conductivité

# Boundary conditions
Twest   = Tamp*np.exp( -xc2[:, 0]**2/2/sig**2 );   # T(xmin)
Teast   = Tamp*np.exp( -xc2[:,-1]**2/2/sig**2 );   # T(xmax)
Tsouth  = Tamp*np.exp( -yc2[ 0,:]**2/2/sig**2 );   # T(xmin)
Tnorth  = Tamp*np.exp( -yc2[-1,:]**2/2/sig**2 );   # T(xmax)
TEW     = np.zeros((nx+1,ny-1));
TNS     = np.zeros((nx-1,ny+1));

for i in range(nt):

    # Update time
    timep = timep + dt;

    # Horizontal flux
    TEW[1:-1,:] = T[ :,:]
    if BC==1:
        TEW[ 0,:]   = 2*Twest - T[ 0,:]
        TEW[-1,:]   = 2*Teast - T[-1,:]
    elif BC==2:
        TEW[ 0,:]   = T[ 0,:]
        TEW[-1,:]   = T[-1,:]
    kx          =  0.5*(kn[:,1:] + kn[:,:-1]);
    qx          = -kx*np.diff(TEW,axis=0)/dx;

    # Vertical flux
    TNS[:,1:-1] = T[:,:]
    if BC==1:
        TNS[:, 0]   = 2*Tsouth - T[:,0]
        TNS[:, -1]  = 2*Tnorth - T[:,-1]
    elif BC==2:
        TNS[:, 0]   = T[:,0]
        TNS[:, -1]  = T[:,-1]
    ky          =  0.5*(kn[1:,:] + kn[:-1,:]);
    qy          = -ky*np.diff(TNS,axis=1)/dy;

    # Temperature update
    T    = T - dt/rho/c * ( np.diff(qx,axis=0)/dx + np.diff(qy,axis=1)/dy );
    pass

print( "time : {0:.8f}".format( time.time()-tic) )
print( 'Min. temperature %2.2e'%(np.min(T)) )
print( 'Max. temperature %2.2e'%(np.max(T)) )

plt.figure()
plt.title('Temperature at time %2.1f s'%(timep))
plt.contourf(xc2, yc2, T, 256, cmap=plt.cm.jet)
plt.colorbar()
plt.show()
