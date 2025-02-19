from enum import Enum


BULKY_VOLUME_THRESHOLD = 1_000_000  # units in cm^3
BULKY_DIMENSION_THRESHOLD = 150  # unit in cm
HEAVY_MASS_THRESHOLD = 20  # unit in kg


class PackageStackLabel(Enum):
    # standard packages (those that are not bulky or heavy) can be handled normally
    STANDARD = 1
    # packages that are either heavy or bulky can't be handled automatically
    SPECIAL = 2
    # packages that are both heavy and bulky are rejected
    REJECTED = 3


class Package:
    def __init__(self, width: float, height: float, length: float, mass: float):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

        self.label = None
        self.designate_stack_label()

    def is_valid(self):
        return all([
            self._is_valid_dimension(self.width),
            self._is_valid_dimension(self.height),
            self._is_valid_dimension(self.length),
            self._is_valid_mass()
        ])

    def _is_number(self, value: any):
        return type(value) in [float, int]

    def _is_valid_dimension(self, dimension):
        return self._is_number(dimension) and dimension > 0
    
    def _is_valid_mass(self):
        return self._is_number(self.mass) and self.mass > 0

    def set_label(self, label: str):
        self.label = label

    def get_volume(self):
        return self.width * self.height * self.length
    
    def is_bulky(self):
        if self.get_volume() >= BULKY_VOLUME_THRESHOLD or (
            self.width >= BULKY_DIMENSION_THRESHOLD or
            self.height >= BULKY_DIMENSION_THRESHOLD or
            self.length >= BULKY_DIMENSION_THRESHOLD
        ):
            return True
        return False
    
    def is_heavy(self):
        return self.mass >= HEAVY_MASS_THRESHOLD
    
    def designate_stack_label(self):
        if self.is_valid():
            _is_bulky = self.is_bulky()
            _is_heavy = self.is_heavy()

            if _is_bulky and _is_heavy:
                self.set_label(PackageStackLabel.REJECTED.name)
            elif _is_bulky or _is_heavy:
                self.set_label(PackageStackLabel.SPECIAL.name)
            else:
                self.set_label(PackageStackLabel.STANDARD.name)
        else:
            # assuming that packages cannot be created with invalid mass/dimension
            # (i.e. at less than or equal to 0), so we reject those
            self.set_label(PackageStackLabel.REJECTED.name)


def sort(width, height, length, mass):
    package = Package(width, height, length, mass)
    return package.label
