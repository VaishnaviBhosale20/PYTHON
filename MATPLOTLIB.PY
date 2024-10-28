import matplotlib.pyplot as plt
import numpy as np

# Basic Line Plot
print("Basic Line Plot")
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label='Sine Wave', color='blue', linestyle='--')
plt.title('Basic Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
print("Scatter Plot")
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
plt.figure()
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.colorbar()
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Bar Plot
print("Bar Plot")
categories = ['Category A', 'Category B', 'Category C']
values = [5, 7, 3]
plt.figure()
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Horizontal Bar Plot
print("Horizontal Bar Plot")
plt.figure()
plt.barh(categories, values, color=['purple', 'orange', 'cyan'])
plt.title('Horizontal Bar Plot')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()

# Histogram
print("Histogram")
data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30, color='green', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Data values')
plt.ylabel('Frequency')
plt.show()

# Box Plot
print("Box Plot")
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.figure()
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('Box Plot')
plt.xlabel('Dataset')
plt.ylabel('Values')
plt.show()

# Pie Chart
print("Pie Chart")
sizes = [30, 20, 25, 25]
labels = ['Group A', 'Group B', 'Group C', 'Group D']
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, colors=['blue', 'orange', 'green', 'red'])
plt.title('Pie Chart')
plt.show()

# Subplots
print("Subplots")
x = np.linspace(0, 10, 100)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, np.sin(x), 'tab:blue')
axs[0, 0].set_title('Sine')
axs[0, 1].plot(x, np.cos(x), 'tab:orange')
axs[0, 1].set_title('Cosine')
axs[1, 0].plot(x, np.tan(x), 'tab:green')
axs[1, 0].set_title('Tangent')
axs[1, 1].plot(x, -np.sin(x), 'tab:red')
axs[1, 1].set_title('-Sine')
fig.tight_layout(pad=2.0)
plt.show()

# Heatmap
print("Heatmap")
data = np.random.rand(10, 10)
plt.figure()
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()

# Contour Plot
print("Contour Plot")
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.figure()
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar()
plt.title('Contour Plot')
plt.show()

# 3D Plot
from mpl_toolkits.mplot3d import Axes3D
print("3D Plot")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('3D Surface Plot')
plt.show()

# Error Bars
print("Error Bars")
x = np.arange(0, 10, 1)
y = np.exp(-x)
yerr = 0.1 + 0.1 * np.sqrt(x)
plt.figure()
plt.errorbar(x, y, yerr=yerr, fmt='-o')
plt.title('Error Bars')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Filled Area Plot
print("Filled Area Plot")
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure()
plt.fill_between(x, y1, y2, color='gray', alpha=0.5)
plt.title('Filled Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Customizing with Annotations
print("Customizing with Annotations")
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure()
plt.plot(x, y, label='Sine')
plt.annotate('Max Point', xy=(np.pi/2, 1), xytext=(np.pi, 1.5),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.title('Plot with Annotation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Polar Plot
print("Polar Plot")
theta = np.linspace(0, 2 * np.pi, 100)
r = np.abs(np.sin(2 * theta) * np.cos(2 * theta))
plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title('Polar Plot')
plt.show()

# Logarithmic Scale Plot
print("Logarithmic Scale Plot")
x = np.linspace(0.1, 10, 100)
y = np.exp(x)
plt.figure()
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis (Log Scale)')
plt.show()

# OUTPUT:-
#   1. Basic Line Plot
# 	2. Scatter Plot
# 	3. Bar Plot
# 	4. Horizontal Bar Plot
# 	5. Histogram
# 	6. Box Plot
# 	7. Pie Chart
# 	8. Subplots
# 	9. Heatmap
# 	10. Contour Plot
# 	11. 3D Plot
# 	12. Error Bars
# 	13. Filled Area Plot
# 	14. Customizing with Annotations
# 	15. Polar Plot
#   16.Logarithmic Scale Plot