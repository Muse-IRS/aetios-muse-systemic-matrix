import sys 
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# test_ssf.py
from ssf import SSFKernel

kernel = SSFKernel()

signals = [0.01, 0.01, 0.5, 0.02, 0.01]

for i, s in enumerate(signals):
    result = kernel.step(s)
    print(f"T{i:02d} | {result}")
