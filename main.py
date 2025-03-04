import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from numba import jit, prange
import time

@jit(nopython=True, parallel=True)
def calculate_mandelbulb(width, height, depth, max_iterations, power, threshold=2.0):
    """Calculate a 3D Mandelbulb fractal using parallel processing."""
    result = np.zeros((width, height, depth), dtype=np.uint8)
    
    for i in prange(width):
        x = (i - width/2) * 2.0 / width
        for j in range(height):
            y = (j - height/2) * 2.0 / height
            for k in range(depth):
                z = (k - depth/2) * 2.0 / depth
                
                x0, y0, z0 = x, y, z
                iteration = 0
                
                while x*x + y*y + z*z < threshold and iteration < max_iterations:
                    r = np.sqrt(x*x + y*y + z*z)
                    theta = np.arctan2(np.sqrt(x*x + y*y), z)
                    phi = np.arctan2(y, x)
                    
                    r = r**power
                    x = r * np.sin(theta * power) * np.cos(phi * power) + x0
                    y = r * np.sin(theta * power) * np.sin(phi * power) + y0
                    z = r * np.cos(theta * power) + z0
                    
                    iteration += 1
                
                if iteration < max_iterations:
                    result[i, j, k] = iteration
    
    return result

class MandelbulbExplorer:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 10))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_facecolor('black')
        self.fig.patch.set_facecolor('black')
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])
        self.ax.set_title('Interactive Mandelbulb Fractal Explorer', color='white', fontsize=16)
        
        self.power = 8.0
        self.resolution = 50
        self.max_iterations = 20
        self.angle = 0
        
        print("Calculating initial Mandelbulb fractal...")
        start_time = time.time()
        self.update_mandelbulb()
        print(f"Initial calculation took {time.time() - start_time:.2f} seconds")
        
        self.animation = FuncAnimation(self.fig, self.update, frames=72, interval=100)
        
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        print("\nControls:")
        print("- Arrow Up/Down: Increase/decrease power")
        print("- +/-: Increase/decrease resolution")
        print("- [/]: Increase/decrease max iterations")
        
    def update_mandelbulb(self):
        """Recalculate the Mandelbulb with current parameters"""
        self.mandelbulb = calculate_mandelbulb(
            self.resolution, self.resolution, self.resolution, 
            self.max_iterations, self.power
        )
        
        x, y, z = [], [], []
        colors = []
        
        for i in range(self.resolution):
            for j in range(self.resolution):
                for k in range(self.resolution):
                    if self.mandelbulb[i, j, k] > 0:
                        x.append(i)
                        y.append(j)
                        z.append(k)
                        colors.append(self.mandelbulb[i, j, k])
        
        self.points = (np.array(x), np.array(y), np.array(z))
        self.point_colors = np.array(colors)
        
    def update(self, frame):
        """Update function for animation"""
        self.angle = frame * 5
        self.ax.clear()
        self.ax.set_facecolor('black')
        self.ax.grid(False)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_zticks([])
        
        self.ax.set_title(f'Power: {self.power:.1f}, Resolution: {self.resolution}, Iterations: {self.max_iterations}', 
                         color='white', fontsize=12)
        
        if len(self.points[0]) > 0:
            scatter = self.ax.scatter(
                self.points[0], self.points[1], self.points[2],
                c=self.point_colors, 
                cmap='plasma',
                s=15,
                alpha=0.7
            )
        
        self.ax.view_init(30, self.angle)
        return scatter,
    
    def on_key(self, event):
        """Handle keyboard interactions"""
        if event.key == 'up':
            self.power += 0.5
            self.update_mandelbulb()
        elif event.key == 'down':
            self.power = max(1.0, self.power - 0.5)
            self.update_mandelbulb()
        elif event.key == '+':
            self.resolution = min(80, self.resolution + 5)
            self.update_mandelbulb()
        elif event.key == '-':
            self.resolution = max(20, self.resolution - 5)
            self.update_mandelbulb()
        elif event.key == ']':
            self.max_iterations += 5
            self.update_mandelbulb()
        elif event.key == '[':
            self.max_iterations = max(5, self.max_iterations - 5)
            self.update_mandelbulb()

if __name__ == "__main__":
    print("Starting Mandelbulb Explorer...")
    explorer = MandelbulbExplorer()
    plt.show()
