# ───────────────────────────────────────────────────────────────
# BASIS: MATERIALKLASSEN
# ───────────────────────────────────────────────────────────────

class Material:
    def __init__(self, name, conductivity, permittivity, density, notes=""):
        self.name = name
        self.conductivity = conductivity
        self.permittivity = permittivity
        self.density = density
        self.notes = notes

    def describe(self):
        return {
            "Material": self.name,
            "Conductivity": self.conductivity,
            "Permittivity": self.permittivity,
            "Density": self.density,
            "Notes": self.notes
        }


# ───────────────────────────────────────────────────────────────
# SCHICHT 1: FARADAY-KÄFIG (EMP-SCHUTZ)
# ───────────────────────────────────────────────────────────────

class FaradayCage:
    def __init__(self, material: Material, thickness_mm, seam_sealing=True, filtered_feeds=True):
        self.material = material
        self.thickness_mm = thickness_mm
        self.seam_sealing = seam_sealing
        self.filtered_feeds = filtered_feeds

    def shielding_effectiveness(self):
        base = self.material.conductivity * self.thickness_mm
        if self.seam_sealing:
            base *= 1.5
        if self.filtered_feeds:
            base *= 1.3
        return base

    def describe(self):
        return {
            "Type": "Faraday Cage",
            "Material": self.material.name,
            "Thickness (mm)": self.thickness_mm,
            "Seam Sealing": self.seam_sealing,
            "Filtered Feeds": self.filtered_feeds,
            "Shielding Score": self.shielding_effectiveness()
        }


# ───────────────────────────────────────────────────────────────
# SCHICHT 2: QUARZ-VERBUNDSTRUKTUR (MECHANIK + THERMIK)
# ───────────────────────────────────────────────────────────────

class QuartzCompositeLayer:
    def __init__(self, quartz_fraction, binder_fraction, density, thermal_stability):
        self.quartz_fraction = quartz_fraction
        self.binder_fraction = binder_fraction
        self.density = density
        self.thermal_stability = thermal_stability

    def mechanical_strength(self):
        return self.quartz_fraction * 0.9 + self.binder_fraction * 0.4

    def describe(self):
        return {
            "Type": "Quartz Composite",
            "Quartz Fraction": self.quartz_fraction,
            "Binder Fraction": self.binder_fraction,
            "Density": self.density,
            "Thermal Stability": self.thermal_stability,
            "Mechanical Strength Score": self.mechanical_strength()
        }


# ───────────────────────────────────────────────────────────────
# SCHICHT 3: QUARZ-VERGUSS (ELEKTRONIK HERMETISCH)
# ───────────────────────────────────────────────────────────────

class QuartzEncapsulation:
    def __init__(self, purity, thickness_mm, thermal_path=True):
        self.purity = purity
        self.thickness_mm = thickness_mm
        self.thermal_path = thermal_path

    def isolation_rating(self):
        base = self.purity * self.thickness_mm
        if self.thermal_path:
            base *= 1.2
        return base

    def describe(self):
        return {
            "Type": "Quartz Encapsulation",
            "Purity": self.purity,
            "Thickness (mm)": self.thickness_mm,
            "Thermal Path": self.thermal_path,
            "Isolation Score": self.isolation_rating()
        }


# ───────────────────────────────────────────────────────────────
# STM32H5-MODUL (EINGEGOSSENE ELEKTRONIK)
# ───────────────────────────────────────────────────────────────

class STM32H5Module:
    def __init__(self, name, encapsulation: QuartzEncapsulation):
        self.name = name
        self.encapsulation = encapsulation

    def protection_score(self):
        return self.encapsulation.isolation_rating()

    def describe(self):
        return {
            "Module": self.name,
            "Encapsulation": self.encapsulation.describe(),
            "Module Protection Score": self.protection_score()
        }


# ───────────────────────────────────────────────────────────────
# KOMPLETTSYSTEM: ALLE 3 SCHICHTEN KOMBINIEREN
# ───────────────────────────────────────────────────────────────

class TripleShieldSystem:
    def __init__(self, cage: FaradayCage, composite: QuartzCompositeLayer, module: STM32H5Module):
        self.cage = cage
        self.composite = composite
        self.module = module

    def total_protection(self):
        return (
            self.cage.shielding_effectiveness() *
            self.composite.mechanical_strength() *
            self.module.protection_score()
        )

    def describe_all(self):
        return {
            "Layer 1 - Faraday Cage": self.cage.describe(),
            "Layer 2 - Quartz Composite": self.composite.describe(),
            "Layer 3 - Quartz Encapsulation": self.module.encapsulation.describe(),
            "Module": self.module.describe(),
            "TOTAL PROTECTION SCORE": self.total_protection()
        }


# ───────────────────────────────────────────────────────────────
# BEISPIELKONFIGURATION
# ───────────────────────────────────────────────────────────────

aluminum = Material("Aluminum", conductivity=3.5e7, permittivity=1.0, density=2.7)
quartz = Material("Quartz", conductivity=1e-17, permittivity=3.8, density=2.65)

cage = FaradayCage(material=aluminum, thickness_mm=2.0)
composite = QuartzCompositeLayer(quartz_fraction=0.85, binder_fraction=0.15, density=2.5, thermal_stability=0.95)
encapsulation = QuartzEncapsulation(purity=0.99, thickness_mm=5.0)

stm_module = STM32H5Module("STM32H563-Sensorboard", encapsulation=encapsulation)

system = TripleShieldSystem(cage, composite, stm_module)

# Einzelne Darstellung:
layer1 = cage.describe()
layer2 = composite.describe()
layer3 = encapsulation.describe()

# Gesamtdarstellung:
full_system = system.describe_all()
