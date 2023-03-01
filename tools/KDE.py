'''
Kernel density estimation (KDE)
1. scipy.stats.gaussian_kde
2. sklearn.neighbors 
'''

#with scipy=========================
import scipy.stats as st
y_lim = [-1500,1500]; nbiny = 50; #set range and bins
biny = eval('%s' %nbiny+'j')
ymin, ymax = y_lim[0], y_lim[1] 
xx = np.mgrid[ymin:ymax:biny] #set gird map
positions = np.vstack([xx.ravel()])

values = np.vstack([v_los])
kernel = st.gaussian_kde(values)
f = np.reshape(kernel(positions).T, xx.shape)

#with sklearn (can adjust the bandwidth)=========================
from sklearn.neighbors import KernelDensity

# instantiate and fit the KDE model
kde = KernelDensity(bandwidth=60, kernel='gaussian').fit(v_los[:, None])
# score_samples returns the log of the probability density
logprob = kde.score_samples(xx[:, None])
score = np.exp(logprob)
