from correlcalc import *
bins = np.arange(0.002,0.052,0.002)
acorrdr12flcdmcmn2x=atpcf('/usr3/vstr/yrohin/Downloads/galaxy_DR12v5_CMASS_North.fits',bins,bins,randfile='/usr3/vstr/yrohin/randcat_DR12_CMN2x.dat',vtype='sigpi',estimator='ls',weights='eq')
print("---------------------------------------------------------------------------------")
print("Calulating for sflat-mu")
binspar = np.arange(0.002,0.052,0.002)
binsper = np.arange(0.05,1.05,0.05)
acorrdr12flcdmsmucmn=atpcf('/usr3/vstr/yrohin/Downloads/galaxy_DR12v5_CMASS_North.fits',binspar,binsper,randfile='/usr3/vstr/yrohin/randcat_DR12_CMN2x.dat',vtype='smu',estimator='ls',weights='eq')
print("---------------------------------------------------------------------------------")
acorrdr12flcdmcmn2x=atpcf('/usr3/vstr/yrohin/Downloads/galaxy_DR12v5_CMASS_North.fits',bins,bins,randfile='/usr3/vstr/yrohin/randcat_DR12_CMN2x.dat',vtype='sigpi',estimator='ls',weights=True)
print("---------------------------------------------------------------------------------")
acorrdr12flcdmsmucmn=atpcf('/usr3/vstr/yrohin/Downloads/galaxy_DR12v5_CMASS_North.fits',binspar,binsper,randfile='/usr3/vstr/yrohin/randcat_DR12_CMN2x.dat',vtype='smu',estimator='ls',weights=True)