# Package Classification System

## Project Objective
This project implements a package classification system that sorts packages into different handling categories based on their physical properties (dimensions and mass). The system helps logistics operations by automatically determining how packages should be handled in the sorting process.

## Classification Categories
- **STANDARD**: Normal packages that can be handled automatically
- **SPECIAL**: Packages that require special handling (either bulky or heavy)
- **REJECTED**: Packages that cannot be processed (both bulky and heavy, or invalid dimensions/mass)

## Package Class Overview
The `Package` class is the core component of this system:
- **Properties**: width, height, length, and mass
- **Key Methods**:
  - `is_valid()`: Validates package dimensions and mass
  - `get_volume()`: Calculates package volume
  - `is_bulky()`: Checks if package exceeds volume or dimension thresholds
  - `is_heavy()`: Checks if package exceeds mass threshold
  - `designate_stack_label()`: Assigns handling category based on package properties

## Usage Example
```python
from package_handler import sort

# Create and classify a standard package
result = sort(100, 50, 30, 15)  # width, height, length, mass
print(result)  # Output: "STANDARD"

# Create and classify a special package (heavy)
result = sort(100, 50, 30, 25)  # mass > 20kg
print(result)  # Output: "SPECIAL"
```

## Thresholds
- Bulky Volume: 1,000,000 cm³
- Bulky Dimension: 150 cm (any single dimension)
- Heavy Mass: 20 kg