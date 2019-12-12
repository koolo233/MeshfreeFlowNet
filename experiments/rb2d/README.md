## Rayleigh-Bernard 2D Experiment

### Dataset Description
Below are some instructions for retrieving the sample data. We can generate more data by varying any of the below parameters:
1. Random seed for the initial perturbation. Set to 42 for the example dataset. At a different random seed the solver will produce results simulated under the same set of physics, but different realisations of the same set of equation given different intial perturbations.
2. Raleigh number. Set to 1e6 for the example dataset. Higher Raleigh number leads to stronger turbulence.
3. Temperature of top and bottom plates. Set to +0.5 and -0.5 for the example dataset.

### Retrieving Sample Data
Download the sample simulation data file (~700 MB) from the server
```bash
wget island.me.berkeley.edu/stsres/rb2d_ra1e6_s42.npz
```
Load and parse the data in python
```python
import numpy as np

filename = 'rb2d_ra1e6_s42.npz'
d = np.load(filename)

print(d.keys())
# >>> ['p', 'b', 'u', 'w', 'bz', 'uz', 'wz', 'write_number', 'sim_time']

print(d['b'].shape)
# >>> (200, 512, 128)
```
Each physical quantity is stored as a (# time steps, # resolution in x, # resolution in z) array.

Below is a description of the variables in this file:
- p: pressure, shape (200, 512, 128)
- b: temperature, shape (200, 512, 128)
- u: velocity in the x direction, shape (200, 512, 128)
- w: velocity in the z direction, shape (200, 512, 128)
- bz: the z derivative of b, shape (200, 512, 128)
- uz: the z derivative of u, shape (200, 512, 128)
- wz: the z derivative of w, shape (200, 512, 128)
- write_number: the sequence index of the simulation frames
- sim_time: simulation time.