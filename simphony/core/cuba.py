# code auto-generated by the
# simphony-metadata/scripts/generate.py script.
# cuba.yml
from enum import Enum, unique


@unique
class CUBA(Enum):
    ACCELERATION = "ACCELERATION"
    AMPHIPHILICITY = "AMPHIPHILICITY"
    ANGULAR_ACCELERATION = "ANGULAR_ACCELERATION"
    ANGULAR_VELOCITY = "ANGULAR_VELOCITY"
    ATOM = "ATOM"
    ATOMISTIC = "ATOMISTIC"
    BASE_CENTERED_MONOCLINIC_LATTICE = "BASE_CENTERED_MONOCLINIC_LATTICE"
    BASE_CENTERED_ORTHORHOMBIC_LATTICE = "BASE_CENTERED_ORTHORHOMBIC_LATTICE"
    BASIS = "BASIS"
    BERENDSEN = "BERENDSEN"
    BIRD_CARREAU_MODEL = "BIRD_CARREAU_MODEL"
    BODY_CENTERED_CUBIC_LATTICE = "BODY_CENTERED_CUBIC_LATTICE"
    BODY_CENTERED_ORTHORHOMBIC_LATTICE = "BODY_CENTERED_ORTHORHOMBIC_LATTICE"
    BODY_CENTERED_TETRAGONAL_LATTICE = "BODY_CENTERED_TETRAGONAL_LATTICE"
    BOND = "BOND"
    BOND_LABEL = "BOND_LABEL"
    BOND_TYPE = "BOND_TYPE"
    BOUNDARY = "BOUNDARY"
    BOX = "BOX"
    BRAVAIS_LATTICE = "BRAVAIS_LATTICE"
    CELL = "CELL"
    CFD = "CFD"
    CHARGE = "CHARGE"
    CHARGE_DENSITY = "CHARGE_DENSITY"
    CHEMICAL_SPECIE = "CHEMICAL_SPECIE"
    COHESION_ENERGY_DENSITY = "COHESION_ENERGY_DENSITY"
    COLLISION_OPERATOR = "COLLISION_OPERATOR"
    COMPRESSIBILITY_MODEL = "COMPRESSIBILITY_MODEL"
    COMPUTATIONAL_METHOD = "COMPUTATIONAL_METHOD"
    COMPUTATIONAL_MODEL = "COMPUTATIONAL_MODEL"
    CONCENTRATION = "CONCENTRATION"
    CONDITION = "CONDITION"
    CONSTANT_ELECTROSTATIC_FIELD_MODEL = "CONSTANT_ELECTROSTATIC_FIELD_MODEL"
    CONTACT_ANGLE = "CONTACT_ANGLE"
    CONTINUUM = "CONTINUUM"
    COULOMB = "COULOMB"
    COULOMB_FRICTION_FORCE = "COULOMB_FRICTION_FORCE"
    COUPLING_TIME = "COUPLING_TIME"
    CROSS_POWER_LAW_MODEL = "CROSS_POWER_LAW_MODEL"
    CRYSTAL_STORAGE = "CRYSTAL_STORAGE"
    CUBIC_LATTICE = "CUBIC_LATTICE"
    CUDS = "CUDS"
    CUDS_COMPONENT = "CUDS_COMPONENT"
    CUDS_ITEM = "CUDS_ITEM"
    CURRENT = "CURRENT"
    CUTOFF_DISTANCE = "CUTOFF_DISTANCE"
    DATA_SET = "DATA_SET"
    DEBYE_LENGTH = "DEBYE_LENGTH"
    DELTA_DISPLACEMENT = "DELTA_DISPLACEMENT"
    DEM = "DEM"
    DENSITY = "DENSITY"
    DESCRIPTION = "DESCRIPTION"
    DIELECTRIC_CONSTANT = "DIELECTRIC_CONSTANT"
    DIFFUSION_COEFFICIENT = "DIFFUSION_COEFFICIENT"
    DIFFUSION_VELOCITY = "DIFFUSION_VELOCITY"
    DIRECTION = "DIRECTION"
    DIRICHLET = "DIRICHLET"
    DISSIPATION_FORCE = "DISSIPATION_FORCE"
    DISTRIBUTION = "DISTRIBUTION"
    DYNAMIC_PRESSURE = "DYNAMIC_PRESSURE"
    DYNAMIC_VISCOSITY = "DYNAMIC_VISCOSITY"
    EDGE = "EDGE"
    ELECTRIC_FIELD = "ELECTRIC_FIELD"
    ELECTRONIC = "ELECTRONIC"
    ELECTRON_MASS = "ELECTRON_MASS"
    ELECTROSTATIC_FIELD = "ELECTROSTATIC_FIELD"
    ELECTROSTATIC_MODEL = "ELECTROSTATIC_MODEL"
    EMPTY = "EMPTY"
    ENERGY = "ENERGY"
    ENERGY_WELL_DEPTH = "ENERGY_WELL_DEPTH"
    ENGINE = "ENGINE"
    ENGINE_FEATURE = "ENGINE_FEATURE"
    EQUATION_OF_STATE_COEFFICIENT = "EQUATION_OF_STATE_COEFFICIENT"
    EULER_ANGLES = "EULER_ANGLES"
    EXTERNAL_APPLIED_FORCE = "EXTERNAL_APPLIED_FORCE"
    EXTERNAL_FORCING = "EXTERNAL_FORCING"
    FACE = "FACE"
    FACE_CENTERED_CUBIC_LATTICE = "FACE_CENTERED_CUBIC_LATTICE"
    FACE_CENTERED_ORTHORHOMBIC_LATTICE = "FACE_CENTERED_ORTHORHOMBIC_LATTICE"
    FEM = "FEM"
    FINAL = "FINAL"
    FLOW_TYPE = "FLOW_TYPE"
    FLUX = "FLUX"
    FORCE = "FORCE"
    FREE = "FREE"
    FREE_SURFACE_MODEL = "FREE_SURFACE_MODEL"
    FRICTION_COEFFICIENT = "FRICTION_COEFFICIENT"
    FULL = "FULL"
    FVM = "FVM"
    GRANULAR_DYNAMICS = "GRANULAR_DYNAMICS"
    GRAVITY_MODEL = "GRAVITY_MODEL"
    HAMAKER_CONSTANT = "HAMAKER_CONSTANT"
    HEAT_CONDUCTIVITY = "HEAT_CONDUCTIVITY"
    HERSCHEL_BULKLEY_MODEL = "HERSCHEL_BULKLEY_MODEL"
    HEXAGONAL_LATTICE = "HEXAGONAL_LATTICE"
    HOMOGENIZED_STRESS_TENSOR = "HOMOGENIZED_STRESS_TENSOR"
    INCOMPRESSIBLE_FLUID_MODEL = "INCOMPRESSIBLE_FLUID_MODEL"
    INDEX = "INDEX"
    INITIAL_VISCOSITY = "INITIAL_VISCOSITY"
    INTEGRATION_STEP = "INTEGRATION_STEP"
    INTEGRATION_TIME = "INTEGRATION_TIME"
    INTERATOMIC_POTENTIAL = "INTERATOMIC_POTENTIAL"
    ION_VALENCE_EFFECT = "ION_VALENCE_EFFECT"
    ISOTHERMAL_MODEL = "ISOTHERMAL_MODEL"
    KINEMATIC_VISCOSITY = "KINEMATIC_VISCOSITY"
    KS_DFT = "KS_DFT"
    LABEL = "LABEL"
    LAMINAR_FLOW_MODEL = "LAMINAR_FLOW_MODEL"
    LATTICE = "LATTICE"
    LATTICE_PARAMETER = "LATTICE_PARAMETER"
    LATTICE_SPACING = "LATTICE_SPACING"
    LATTICE_VECTORS = "LATTICE_VECTORS"
    LENNARD_JONES_6_12 = "LENNARD_JONES_6_12"
    LINEAR_CONSTANT = "LINEAR_CONSTANT"
    MAJOR = "MAJOR"
    MASS = "MASS"
    MATERIAL = "MATERIAL"
    MATERIAL_RELATION = "MATERIAL_RELATION"
    MATERIAL_TYPE = "MATERIAL_TYPE"
    MAXIMUM_VISCOSITY = "MAXIMUM_VISCOSITY"
    MESH = "MESH"
    MESH_ELEMENT = "MESH_ELEMENT"
    MESOSCOPIC = "MESOSCOPIC"
    MINIMUM_VISCOSITY = "MINIMUM_VISCOSITY"
    MINOR = "MINOR"
    MIXTURE_MODEL = "MIXTURE_MODEL"
    MODEL_EQUATION = "MODEL_EQUATION"
    MOLECULAR_DYNAMICS = "MOLECULAR_DYNAMICS"
    MOLECULAR_STATICS = "MOLECULAR_STATICS"
    MOMENTUM = "MOMENTUM"
    MOMENT_INERTIA = "MOMENT_INERTIA"
    MONOCLINIC_LATTICE = "MONOCLINIC_LATTICE"
    MULTIPHASE_MODEL = "MULTIPHASE_MODEL"
    NAME = "NAME"
    NAME_UC = "NAME_UC"
    NEUMANN = "NEUMANN"
    NEWTONIAN_FLUID_MODEL = "NEWTONIAN_FLUID_MODEL"
    NODE = "NODE"
    NONE = "NONE"
    NOSE_HOOVER = "NOSE_HOOVER"
    NUMBER_OF_POINTS = "NUMBER_OF_POINTS"
    NUMBER_OF_TIME_STEPS = "NUMBER_OF_TIME_STEPS"
    OCCUPANCY = "OCCUPANCY"
    ORDER_PARAMETER = "ORDER_PARAMETER"
    ORIGIN = "ORIGIN"
    ORIGINAL_POSITION = "ORIGINAL_POSITION"
    ORTHORHOMBIC_LATTICE = "ORTHORHOMBIC_LATTICE"
    PAIR_POTENTIAL = "PAIR_POTENTIAL"
    PARTICLE = "PARTICLE"
    PARTICLES = "PARTICLES"
    PATCH = "PATCH"
    PERIODIC = "PERIODIC"
    PHASE_INTERACTION_STRENGTH = "PHASE_INTERACTION_STRENGTH"
    PHYSICS_EQUATION = "PHYSICS_EQUATION"
    POINT = "POINT"
    POISSON_RATIO = "POISSON_RATIO"
    POSITION = "POSITION"
    POTENTIAL_ENERGY = "POTENTIAL_ENERGY"
    POWER_LAW_INDEX = "POWER_LAW_INDEX"
    POWER_LAW_VISCOSITY_MODEL = "POWER_LAW_VISCOSITY_MODEL"
    PRESSURE = "PRESSURE"
    PRIMITIVE_CELL = "PRIMITIVE_CELL"
    PROBABILITY_COEFFICIENT = "PROBABILITY_COEFFICIENT"
    RADIUS = "RADIUS"
    REFERENCE_DENSITY = "REFERENCE_DENSITY"
    RELATIVE_VELOCITY = "RELATIVE_VELOCITY"
    RELAXATION_TIME = "RELAXATION_TIME"
    RESTITUTION_COEFFICIENT = "RESTITUTION_COEFFICIENT"
    RHEOLOGY_MODEL = "RHEOLOGY_MODEL"
    RHOMBOHEDRAL_LATTICE = "RHOMBOHEDRAL_LATTICE"
    ROLLING_FRICTION = "ROLLING_FRICTION"
    SCALING_COEFFICIENT = "SCALING_COEFFICIENT"
    SHAPE_CENTER = "SHAPE_CENTER"
    SHAPE_LENGTH = "SHAPE_LENGTH"
    SHAPE_LENGTH_UC = "SHAPE_LENGTH_UC"
    SHAPE_RADIUS = "SHAPE_RADIUS"
    SHAPE_SIDE = "SHAPE_SIDE"
    SIMULATION_DOMAIN_DIMENSIONS = "SIMULATION_DOMAIN_DIMENSIONS"
    SIMULATION_DOMAIN_ORIGIN = "SIMULATION_DOMAIN_ORIGIN"
    SINGLE_PHASE_MODEL = "SINGLE_PHASE_MODEL"
    SIZE = "SIZE"
    SJKR_COHESION_FORCE = "SJKR_COHESION_FORCE"
    SMOOTHING_LENGTH = "SMOOTHING_LENGTH"
    SOFTWARE_TOOL = "SOFTWARE_TOOL"
    SOLVER_PARAMETER = "SOLVER_PARAMETER"
    SPH = "SPH"
    SPHERICITY = "SPHERICITY"
    STATUS = "STATUS"
    STRAIN_TENSOR = "STRAIN_TENSOR"
    STRESS_TENSOR = "STRESS_TENSOR"
    SURFACE_TENSION = "SURFACE_TENSION"
    SURFACE_TENSION_RELATION = "SURFACE_TENSION_RELATION"
    SYMMETRY_LATTICE_VECTORS = "SYMMETRY_LATTICE_VECTORS"
    TEMPERATURE = "TEMPERATURE"
    TEMPERATURE_RESCALING = "TEMPERATURE_RESCALING"
    TETRAGONAL_LATTICE = "TETRAGONAL_LATTICE"
    THERMAL_MODEL = "THERMAL_MODEL"
    THERMODYNAMIC_ENSEMBLE = "THERMODYNAMIC_ENSEMBLE"
    THERMOSTAT = "THERMOSTAT"
    TIME = "TIME"
    TIME_STEP = "TIME_STEP"
    TORQUE = "TORQUE"
    TRICLINIC_LATTICE = "TRICLINIC_LATTICE"
    TURBULENCE_MODEL = "TURBULENCE_MODEL"
    UID = "UID"
    VAN_DER_WAALS_RADIUS = "VAN_DER_WAALS_RADIUS"
    VARIABLE = "VARIABLE"
    VECTOR = "VECTOR"
    VELOCITY = "VELOCITY"
    VERLET = "VERLET"
    VERSION = "VERSION"
    VISCOSITY = "VISCOSITY"
    VOLUME = "VOLUME"
    VOLUME_FRACTION = "VOLUME_FRACTION"
    VOLUME_FRACTION_GRADIENT = "VOLUME_FRACTION_GRADIENT"
    YOUNG_MODULUS = "YOUNG_MODULUS"
    ZETA_POTENTIAL = "ZETA_POTENTIAL"
