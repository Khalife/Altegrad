from numpy import *
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rc

# Load the "gatlin" image data
X = loadtxt('gatlin.csv', delimiter=',')

#================= ADD YOUR CODE HERE ====================================
# Perform SVD decomposition
## TODO: Perform SVD on the X matrix
# Instructions: Perform SVD decomposition of matrix X. Save the 
#               three factors in variables U, S and V
#
U, s, V = linalg.svd(X)


#=========================================================================

# Plot the original image
plt.figure(1)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (rank 480)')
plt.axis('off')
plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Matrix reconstruction using the top k = [10, 20, 50, 100, 200] singular values
## TODO: Create four matrices X10, X20, X50, X100, X200 for each low rank approximation
## using the top k = [10, 20, 50, 100, 200] singlular values 
#
#transform s into a matrix

S10=diag(s)[:10,:10]
U10=U[:,:10]
V10=V[:10,:]
X10=dot(dot(U10,S10),V10)

U20=U[:,0:20]
V20=V[0:20,:]
S20=diag(s)[:20,:20]
X20=dot(dot(U20,S20),V20)

U50=U[:,0:50]
V50=V[0:50,:]
S50=diag(s)[:50,:50]
X50=dot(dot(U50,S50),V50)

U100=U[:,0:100]
V100=V[0:100,:]
S100=diag(s)[:100,:100]
X100=dot(dot(U100,S100),V100)

U200=U[:,0:200]
V200=V[0:200,:]
S200=diag(s)[:200,:200]
X200=dot(dot(U200,S200),V200)


#=========================================================================



#================= ADD YOUR CODE HERE ====================================
# Error of approximation
## TODO: Compute and print the error of each low rank approximation of the matrix
# The Frobenius error can be computed as |X - X_k| / |X|
#

error10=linalg.norm(X-X10)/linalg.norm(X)
error20=linalg.norm(X-X20)/linalg.norm(X)
error50=linalg.norm(X-X50)/linalg.norm(X)
error100=linalg.norm(X-X100)/linalg.norm(X)
error200=linalg.norm(X-X200)/linalg.norm(X)

print error10
print error20
print error50
print error100
print error200

#=========================================================================



# Plot the optimal rank-k approximation for various values of k)
# Create a figure with 6 subfigures
plt.figure(2)

# Rank 10 approximation
plt.subplot(321)
plt.imshow(X10,cmap = cm.Greys_r)
plt.title('Best rank' + str(5) + ' approximation')
plt.axis('off')

# Rank 20 approximation
plt.subplot(322)
plt.imshow(X20,cmap = cm.Greys_r)
plt.title('Best rank' + str(20) + ' approximation')
plt.axis('off')

# Rank 50 approximation
plt.subplot(323)
plt.imshow(X50,cmap = cm.Greys_r)
plt.title('Best rank' + str(50) + ' approximation')
plt.axis('off')

# Rank 100 approximation
plt.subplot(324)
plt.imshow(X100,cmap = cm.Greys_r)
plt.title('Best rank' + str(100) + ' approximation')
plt.axis('off')

# Rank 200 approximation
plt.subplot(325)
plt.imshow(X200,cmap = cm.Greys_r)
plt.title('Best rank' + str(200) + ' approximation')
plt.axis('off')

# Original
plt.subplot(326)
plt.imshow(X,cmap = cm.Greys_r)
plt.title('Original image (Rank 480)')
plt.axis('off')

plt.draw()


#================= ADD YOUR CODE HERE ====================================
# Plot the singular values of the original matrix
## TODO: Plot the singular values of X versus their rank k

#x=linspace(1,s.size,s.size)
plt.figure(5)
plt.plot(s)
plt.title('Singular values')
#print x


#=========================================================================

plt.show() 

