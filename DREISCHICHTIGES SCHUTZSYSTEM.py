class Material:
    def __init__(self, name, conductivity, permittivity, density, notes=""):
        self.name = name
        self.conductivity = conductivity      # S/m
        self.permittivity = permittivity      # relative εr
        self.density = density                # g/cm³
        self.notes = notes

    def __repr__(self):
        return f"<Material {self.name}: σ={self.conductivity}, εr={self.permittivity}>"

# ───────────────────────────────────────────────────────────────
# 1) ÄUSSERE SCHICHT: METALLISCHER FARADAY-KÄFIG
# ───────────────────────────────────────────────────────────────

class FaradayCage:
    def __init__(self, material: Material, thickness_mm, seam_sealing=True, filtered_feeds=True):
        self.material = material
        self.thickness_mm = thickness_mm
        self.seam_sealing = seam_sealing
        self.filtered_feeds = filtered_feeds

    def shielding_effectiveness(self):
        # stark vereinfachtes Modell
        base = self.material.conductivity * self.thickness_mm
        if self.seam_sealing:
            base *= 1.5
        if self.filtered_feeds:
            base *= 1.3
        return base

# ───────────────────────────────────────────────────────────────
# 2) MITTLERE SCHICHT: QUARZ-VERBUNDSTRUKTUR
# ───────────────────────────────────────────────────────────────

class QuartzCompositeLayer:
    def __init__(self, quartz_fraction, binder_fraction, density, thermal_stability):
        self.quartz_fraction = quartz_fraction
        self.binder_fraction = binder_fraction
        self.density = density
        self.thermal_stability = thermal_stability

    def mechanical_strength(self):
        return self.quartz_fraction * 0.9 + self.binder_fraction * 0.4

# ───────────────────────────────────────────────────────────────
# 3) INNERE SCHICHT: QUARZ-VERGUSS DER ELEKTRONIK
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

# ───────────────────────────────────────────────────────────────
# STM32H5-MODUL ALS EINGEGOSSENE EINHEIT
# ───────────────────────────────────────────────────────────────

class STM32H5Module:
    def __init__(self, name, quartz_encapsulation: QuartzEncapsulation):
        self.name = name
        self.encapsulation = quartz_encapsulation

    def protection_score(self):
        return self.encapsulation.isolation_rating()

# ───────────────────────────────────────────────────────────────
# GESAMTSYSTEM: ALLE 3 SCHICHTEN KOMBINIEREN
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

    def describe(self):
        return {
            "Faraday_Cage": self.cage.material.name,
            "Composite": f"Quartz {self.composite.quartz_fraction*100}%",
            "Encapsulation": f"Purity {self.module.encapsulation.purity}",
            "Total_Protection_Score": self.total_protection()
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

print(system.describe())
