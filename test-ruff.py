import os  # F401: Unused import
import sys

def My_Function(n): # N802: Function name should be lowercase
    X = 10          # F841: Local variable 'X' is assigned but never used
    print(f"Result: {n}")
    return result   # F821: Undefined name 'result' (should be 'n')

if __name__ == "__main__":
    My_Function(5)
