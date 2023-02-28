'''
Functions and examples for free parameters fitting:
1. Minuit
2. curve_fit
'''

#Use Minuit to fit=============================
from iminuit import Minuit

#define Chi square function 
def minichi2(M,c):
  chi2 = 0
  halofit = Halo(halotype = HaloTypes.TMPMC, TMPid = nclu)
  m0 = 10**M/1e10
  c0 = 10**c
  halofit.set_param([m0,c0])
  modelM = halofit.mass(rlin)/1e5  
  for ii in range(nbin):
    for jj in range(nbin):
      chi2 += (modelM[ii] - pdata[ii]) * matrix_c[ii,jj] * (modelM[jj] - pdata[jj])
  return chi2

fitmc = Minuit(minichi2, M = Mtrue, c = ctrue)
fitmc.limits["M"]=(14,17)
fitmc.limits["c"]=(-1.,2.)
fitmc.errors["M"]=1
fitmc.errors["c"]=1
fitmc.errordef = Minuit.LEAST_SQUARES

fitmc.migrad()
fitmc.hesse()

if fitmc.valid == False:
  return 0,0,0

fit_M = fitmc.values['M'] #best fit
fit_C = fitmc.values['c'] #best fit


# Use curve_fit==========================================
from scipy.optimize import curve_fit
def func1(x,a,b,c):
  return np.log10(a / (1 + (x/b)**2)**(3*c/2))
coeffs, matcov = curve_fit(func1, x0, y0, p0 = (1e6,1,1))




