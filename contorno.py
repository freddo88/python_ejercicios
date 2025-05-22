import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z, levels=10, cmap='plasma')
plt.colorbar(label='height')
plt.title('Contour Plot ')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
# This code generates a contour plot of the function Z = sin(sqrt(X^2 + Y^2)) using numpy and matplotlib.
# The contour plot visualizes the function's height at different points in the X-Y plane.
# The levels parameter specifies the number of contour lines to draw, and cmap specifies the color map used for the plot.
# The color bar indicates the height corresponding to each contour line.
