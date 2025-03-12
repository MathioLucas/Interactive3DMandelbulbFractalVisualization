# Mandelbulb Explorer

An interactive 3D fractal visualization tool for exploring the fascinating Mandelbulb fractal in real-time.


## About the Project

The Mandelbulb Explorer is a Python-based application that allows users to visualize and interact with the Mandelbulb, a three-dimensional analog of the Mandelbrot set. This tool enables real-time manipulation of fractal parameters, providing an intuitive way to explore the complex and beautiful geometry of this mathematical object.

### Features

- **Interactive Visualization**: Rotate, zoom, and explore the 3D fractal in real-time
- **Parameter Adjustment**: Modify power, resolution, and iteration values on-the-fly
- **GPU Acceleration**: Utilizes Numba for high-performance parallel computing
- **Animation Support**: Built-in rotation animation for captivating visualizations

## The Mathematics Behind the Mandelbulb

The Mandelbulb is a three-dimensional fractal, constructed through an iterative formula similar to the Mandelbrot set but extended to three dimensions. For each point (x,y,z) in 3D space, the formula iterates:

```
(x,y,z) → (r^n * sin(n*θ) * cos(n*φ) + x₀, r^n * sin(n*θ) * sin(n*φ) + y₀, r^n * cos(n*θ) + z₀)
```

Where:
- r is the radius in spherical coordinates
- θ (theta) is the polar angle
- φ (phi) is the azimuthal angle
- n is the power parameter (typically 8 for the classic Mandelbulb)

Points that remain bounded after iterations belong to the set and are colored according to how quickly they escape.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mandelbulb-explorer.git
   cd mandelbulb-explorer
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install numpy matplotlib numba
   ```

## Usage

Run the explorer:
```
python mandelbulb_explorer.py
```

### Controls

- **Arrow Up/Down**: Increase/decrease power value
- **+/-**: Increase/decrease resolution
- **[/]**: Increase/decrease maximum iterations
- **Mouse**: Rotate the view (when animation is paused)
- **Spacebar**: Pause/resume animation (not implemented in current version)

## Performance Notes

- Higher resolution values and iteration counts will require more computational resources
- First-time execution includes a JIT compilation step, which may cause a brief delay
- For optimal performance, a computer with a multi-core CPU is recommended

## Customization

You can modify the following parameters in the code:

- Initial power value (default: 8.0)
- Initial resolution (default: 50)
- Initial max iterations (default: 20)
- Color map (default: 'plasma', alternatives: 'viridis', 'inferno', etc.)
- Point size (default: 15)

## Future Enhancements

Potential improvements for future versions:

- Support for different fractal types
- Color customization interface
- Direct export of high-resolution images
- Virtual reality support
- Improved camera controls
- Custom slicing planes

## Acknowledgments

This project was inspired by:
- Daniel White's original Mandelbulb formulation
- Various mathematical visualizations from the fractal community



## Contact

Mathio M.Luca - luca.mathio1@gmail.com
