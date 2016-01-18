# code auto-generated by the cuba-generate.py script.
from collections import namedtuple

import numpy
import uuid


ATTRIBUTES = [
    "name", "description", "domain", "key", "number", "shape", "dtype"]
Keyword = namedtuple("Keyword", ATTRIBUTES)


KEYWORDS = {
    'ID': Keyword(
        name='Id',
        description='Universal unique id represented as a hex string size 32',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'SPH', 'VIS'],
        key='ID',
        number=0,
        shape=[32],
        dtype=numpy.str),
    'NAME': Keyword(
        name='Name',
        description='Naming of high-level objects (e.g. solver models)',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'SPH', 'VIS'],
        key='NAME',
        number=1,
        shape=[20],
        dtype=numpy.str),
    'POSITION': Keyword(
        name='Position',
        description='Position of a point or node or atom',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'SPH', 'VIS'],
        key='POSITION',
        number=2,
        shape=[3],
        dtype=numpy.float64),
    'DIRECTION': Keyword(
        name='Direction',
        description='Geometric (more general than, e.g., velocity) could be used for spin',  # noqa
        domain=['ATM', 'FEM', 'FVM', 'LBM', 'VIS'],
        key='DIRECTION',
        number=3,
        shape=[3],
        dtype=numpy.float64),
    'STATUS': Keyword(
        name='Status',
        description='Status of a point or node',  # noqa
        domain=['DEM', 'LBM'],
        key='STATUS',
        number=4,
        shape=[1],
        dtype=numpy.int32),
    'LABEL': Keyword(
        name='Label',
        description='Label for a point or node',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'VIS'],
        key='LABEL',
        number=5,
        shape=[1],
        dtype=numpy.int32),
    'MATERIAL_ID': Keyword(
        name='MaterialId',
        description='Material identification number',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='MATERIAL_ID',
        number=6,
        shape=[1],
        dtype=numpy.int32),
    'CHEMICAL_SPECIE': Keyword(
        name='ChemicalSpecie',
        description='Chemical Specie',  # noqa
        domain=['ATM', 'VIS'],
        key='CHEMICAL_SPECIE',
        number=7,
        shape=[20],
        dtype=numpy.str),
    'MATERIAL_TYPE': Keyword(
        name='MaterialType',
        description='Material dimension and type',  # noqa
        domain=['VIS'],
        key='MATERIAL_TYPE',
        number=8,
        shape=[1],
        dtype=numpy.int32),
    'SHAPE_CENTER': Keyword(
        name='ShapeCenter',
        description='Geometrical center of the shape of the material',  # noqa
        domain=['VIS'],
        key='SHAPE_CENTER',
        number=9,
        shape=[3],
        dtype=numpy.float64),
    'SHAPE_LENGTH_UC': Keyword(
        name='ShapeLengthUC',
        description='Length in units cells of the shape of the material',  # noqa
        domain=['VIS'],
        key='SHAPE_LENGTH_UC',
        number=10,
        shape=[3],
        dtype=numpy.float64),
    'SHAPE_LENGTH': Keyword(
        name='ShapeLength',
        description='Length in angstroms of the shape of the materials',  # noqa
        domain=['VIS'],
        key='SHAPE_LENGTH',
        number=11,
        shape=[3],
        dtype=numpy.float64),
    'SHAPE_RADIUS': Keyword(
        name='ShapeRadius',
        description='Radius for a spherical material',  # noqa
        domain=['VIS'],
        key='SHAPE_RADIUS',
        number=12,
        shape=[3],
        dtype=numpy.float64),
    'SHAPE_SIDE': Keyword(
        name='ShapeSide',
        description='Side length for a hexagonal material',  # noqa
        domain=['VIS'],
        key='SHAPE_SIDE',
        number=13,
        shape=[3],
        dtype=numpy.float64),
    'CRYSTAL_STORAGE': Keyword(
        name='CrystalStorage',
        description='Additional information for visualization',  # noqa
        domain=['VIS'],
        key='CRYSTAL_STORAGE',
        number=14,
        shape=[20],
        dtype=numpy.str),
    'NAME_UC': Keyword(
        name='NameUC',
        description='Name of the unit cell of the component',  # noqa
        domain=['ATM', 'VIS'],
        key='NAME_UC',
        number=15,
        shape=[20],
        dtype=numpy.str),
    'LATTICE_VECTORS': Keyword(
        name='LatticeVectors',
        description='Lattice vectors of unit cell of the component',  # noqa
        domain=['ATM', 'VIS'],
        key='LATTICE_VECTORS',
        number=16,
        shape=[3, 3],
        dtype=numpy.float64),
    'SYMMETRY_LATTICE_VECTORS': Keyword(
        name='SymmetryLatticeVectors',
        description='Symmetry Group',  # noqa
        domain=['ATM', 'VIS'],
        key='SYMMETRY_LATTICE_VECTORS',
        number=17,
        shape=[1],
        dtype=numpy.int32),
    'OCCUPANCY': Keyword(
        name='Occupancy',
        description='Occupancy of an atomic position',  # noqa
        domain=['ATM', 'VIS'],
        key='OCCUPANCY',
        number=18,
        shape=[1],
        dtype=numpy.float64),
    'BOND_LABEL': Keyword(
        name='BondLabel',
        description='Unique ID of atoms',  # noqa
        domain=['ATM', 'VIS'],
        key='BOND_LABEL',
        number=19,
        shape=[20],
        dtype=numpy.str),
    'BOND_TYPE': Keyword(
        name='BondType',
        description='Type of label',  # noqa
        domain=['ATM', 'VIS'],
        key='BOND_TYPE',
        number=20,
        shape=[1],
        dtype=numpy.int32),
    'VELOCITY': Keyword(
        name='Velocity',
        description='Velocity of a point or node',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='VELOCITY',
        number=21,
        shape=[3],
        dtype=numpy.float64),
    'ACCELERATION': Keyword(
        name='Acceleration',
        description='Acceleration of a point or node',  # noqa
        domain=['ATM', 'DEM', 'LBM', 'SPH'],
        key='ACCELERATION',
        number=22,
        shape=[3],
        dtype=numpy.float64),
    'NUMBER_OF_POINTS': Keyword(
        name='NumberOfPoints',
        description='Number of points or nodes',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='NUMBER_OF_POINTS',
        number=23,
        shape=[1],
        dtype=numpy.int32),
    'RADIUS': Keyword(
        name='Radius',
        description='Particle radius',  # noqa
        domain=['DEM', 'SPH'],
        key='RADIUS',
        number=24,
        shape=[1],
        dtype=numpy.float64),
    'SIZE': Keyword(
        name='Size',
        description='For non-spherical particles',  # noqa
        domain=['DEM', 'SPH'],
        key='SIZE',
        number=25,
        shape=[1],
        dtype=numpy.float64),
    'MASS': Keyword(
        name='Mass',
        description='Particle mass',  # noqa
        domain=['ATM', 'DEM'],
        key='MASS',
        number=26,
        shape=[1],
        dtype=numpy.float64),
    'VOLUME': Keyword(
        name='Volume',
        description='Volume of a particle, cell, etc.',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH', 'VIS'],
        key='VOLUME',
        number=27,
        shape=[1],
        dtype=numpy.float64),
    'ANGULAR_VELOCITY': Keyword(
        name='AngularVelocity',
        description='Angular velocity of a point or node',  # noqa
        domain=['DEM'],
        key='ANGULAR_VELOCITY',
        number=28,
        shape=[3],
        dtype=numpy.float64),
    'ANGULAR_ACCELERATION': Keyword(
        name='AngularAcceleration',
        description='Angular acceleration of a point or node',  # noqa
        domain=['DEM'],
        key='ANGULAR_ACCELERATION',
        number=29,
        shape=[3],
        dtype=numpy.float64),
    'SIMULATION_DOMAIN_DIMENSIONS': Keyword(
        name='SimulationDomainDimensions',
        description='Size of the simulation domain',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='SIMULATION_DOMAIN_DIMENSIONS',
        number=30,
        shape=[3],
        dtype=numpy.float64),
    'SIMULATION_DOMAIN_ORIGIN': Keyword(
        name='SimulationDomainOrigin',
        description='Offset for the simulation domain',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='SIMULATION_DOMAIN_ORIGIN',
        number=31,
        shape=[3],
        dtype=numpy.float64),
    'DYNAMIC_VISCOSITY': Keyword(
        name='DynamicViscosity',
        description='Dynamic viscosity of fluid',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='DYNAMIC_VISCOSITY',
        number=32,
        shape=[1],
        dtype=numpy.float64),
    'KINEMATIC_VISCOSITY': Keyword(
        name='KinematicViscosity',
        description='Kinematic viscosity of fluid',  # noqa
        domain=['FEM', 'FVM', 'LBM'],
        key='KINEMATIC_VISCOSITY',
        number=33,
        shape=[1],
        dtype=numpy.float64),
    'DIFFUSION_COEFFICIENT': Keyword(
        name='DiffusionCoefficient',
        description='Diffusion coefficient',  # noqa
        domain=['FEM', 'FVM', 'LBM'],
        key='DIFFUSION_COEFFICIENT',
        number=34,
        shape=[1],
        dtype=numpy.float64),
    'PROBABILITY_COEFFICIENT': Keyword(
        name='ProbabilityCoefficient',
        description='For stochastic processes (e.g. sorption)',  # noqa
        domain=['DEM', 'LBM'],
        key='PROBABILITY_COEFFICIENT',
        number=35,
        shape=[1],
        dtype=numpy.float64),
    'FRICTION_COEFFICIENT': Keyword(
        name='FrictionCoefficient',
        description='Control particle friction',  # noqa
        domain=['DEM', 'LBM'],
        key='FRICTION_COEFFICIENT',
        number=36,
        shape=[1],
        dtype=numpy.float64),
    'SCALING_COEFFICIENT': Keyword(
        name='ScalingCoefficient',
        description='Coarsening or time-scale bridging',  # noqa
        domain=['DEM', 'LBM'],
        key='SCALING_COEFFICIENT',
        number=37,
        shape=[1],
        dtype=numpy.float64),
    'EQUATION_OF_STATE_COEFFICIENT': Keyword(
        name='EquationOfStateCoefficient',
        description='Equation of state for multiphase fluids',  # noqa
        domain=['FEM', 'FVM', 'LBM', 'SPH'],
        key='EQUATION_OF_STATE_COEFFICIENT',
        number=38,
        shape=[1],
        dtype=numpy.float64),
    'CONTANCT_ANGLE': Keyword(
        name='ContanctAngle',
        description='Wettability in multiphase flows',  # noqa
        domain=['LBM'],
        key='CONTANCT_ANGLE',
        number=39,
        shape=[1],
        dtype=numpy.float64),
    'AMPHIPHILICITY': Keyword(
        name='Amphiphilicity',
        description='Hydrophilic/-phile behaviour of a particle',  # noqa
        domain=['DEM'],
        key='AMPHIPHILICITY',
        number=40,
        shape=[1],
        dtype=numpy.float64),
    'PHASE_INTERACTION_STRENGTH': Keyword(
        name='PhaseInteractionStrength',
        description='Strength of phase interactions on a particle',  # noqa
        domain=['DEM'],
        key='PHASE_INTERACTION_STRENGTH',
        number=41,
        shape=[1],
        dtype=numpy.float64),
    'HAMAKER_CONSTANT': Keyword(
        name='HamakerConstant',
        description='Van der Waals body-body interaction',  # noqa
        domain=['DEM'],
        key='HAMAKER_CONSTANT',
        number=42,
        shape=[1],
        dtype=numpy.float64),
    'ZETA_POTENTIAL': Keyword(
        name='ZetaPotential',
        description='Coulomb interaction between particles',  # noqa
        domain=['DEM'],
        key='ZETA_POTENTIAL',
        number=43,
        shape=[1],
        dtype=numpy.float64),
    'ION_VALENCE_EFFECT': Keyword(
        name='IonValenceEffect',
        description='Coulomb interaction between particles',  # noqa
        domain=['DEM'],
        key='ION_VALENCE_EFFECT',
        number=44,
        shape=[1],
        dtype=numpy.float64),
    'DEBYE_LENGTH': Keyword(
        name='DebyeLength',
        description='Electrostatic effects of particles in solution',  # noqa
        domain=['DEM'],
        key='DEBYE_LENGTH',
        number=45,
        shape=[1],
        dtype=numpy.float64),
    'SMOOTHING_LENGTH': Keyword(
        name='SmoothingLength',
        description='Half of kernel cut-off for all splines',  # noqa
        domain=['SPH'],
        key='SMOOTHING_LENGTH',
        number=46,
        shape=[1],
        dtype=numpy.float64),
    'LATTICE_SPACING': Keyword(
        name='LatticeSpacing',
        description='Distance between adjacent lattice nodes',  # noqa
        domain=['LBM'],
        key='LATTICE_SPACING',
        number=47,
        shape=[1],
        dtype=numpy.float64),
    'TIME_STEP': Keyword(
        name='TimeStep',
        description='Length of a discrete time step',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM'],
        key='TIME_STEP',
        number=48,
        shape=[1],
        dtype=numpy.float64),
    'NUMBER_OF_TIME_STEPS': Keyword(
        name='NumberOfTimeSteps',
        description='Number of discrete time steps',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM'],
        key='NUMBER_OF_TIME_STEPS',
        number=49,
        shape=[1],
        dtype=numpy.float64),
    'FORCE': Keyword(
        name='Force',
        description='Force',  # noqa
        domain=['DEM', 'LBM', 'SPH'],
        key='FORCE',
        number=50,
        shape=[3],
        dtype=numpy.float64),
    'TORQUE': Keyword(
        name='Torque',
        description='Torque',  # noqa
        domain=['DEM'],
        key='TORQUE',
        number=51,
        shape=[3],
        dtype=numpy.float64),
    'DENSITY': Keyword(
        name='Density',
        description='Density',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='DENSITY',
        number=52,
        shape=[1],
        dtype=numpy.float64),
    'CONCENTRATION': Keyword(
        name='Concentration',
        description='Concentration of a substance',  # noqa
        domain=['ATM', 'FEM', 'FVM', 'LBM', 'VIS'],
        key='CONCENTRATION',
        number=53,
        shape=[1],
        dtype=numpy.float64),
    'PRESSURE': Keyword(
        name='Pressure',
        description='Pressure',  # noqa
        domain=['FEM', 'FVM', 'LBM', 'SPH'],
        key='PRESSURE',
        number=54,
        shape=[1],
        dtype=numpy.float64),
    'TEMPERATURE': Keyword(
        name='Temperature',
        description='Temperature',  # noqa
        domain=['DEM', 'FEM', 'FVM', 'LBM', 'SPH'],
        key='TEMPERATURE',
        number=55,
        shape=[1],
        dtype=numpy.float64),
    'DISTRIBUTION': Keyword(
        name='Distribution',
        description='Single-particle distribution function',  # noqa
        domain=['ATM', 'LBM', 'VIS'],
        key='DISTRIBUTION',
        number=56,
        shape=[1],
        dtype=numpy.float64),
    'ORDER_PARAMETER': Keyword(
        name='OrderParameter',
        description='Phase field in multiphase flows',  # noqa
        domain=['LBM'],
        key='ORDER_PARAMETER',
        number=57,
        shape=[1],
        dtype=numpy.float64),
    'ORIGINAL_POSITION': Keyword(
        name='OriginalPosition',
        description='Position at the beginning of the calculation',  # noqa
        domain=['DEM'],
        key='ORIGINAL_POSITION',
        number=58,
        shape=[3],
        dtype=numpy.float64),
    'DELTA_DISPLACEMENT': Keyword(
        name='DeltaDisplacement',
        description='Displacement during the last time step',  # noqa
        domain=['DEM'],
        key='DELTA_DISPLACEMENT',
        number=59,
        shape=[3],
        dtype=numpy.float64),
    'EXTERNAL_APPLIED_FORCE': Keyword(
        name='ExternalAppliedForce',
        description='Externally applied force (force fields, interactions, etc)',  # noqa
        domain=['DEM'],
        key='EXTERNAL_APPLIED_FORCE',
        number=60,
        shape=[3],
        dtype=numpy.float64),
    'EULER_ANGLES': Keyword(
        name='EulerAngles',
        description='Euler Angles',  # noqa
        domain=['DEM'],
        key='EULER_ANGLES',
        number=61,
        shape=[3],
        dtype=numpy.float64),
    'SPHERICITY': Keyword(
        name='Sphericity',
        description='Sphericity of the particle',  # noqa
        domain=['DEM'],
        key='SPHERICITY',
        number=62,
        shape=[1],
        dtype=numpy.float64),
    'YOUNG_MODULUS': Keyword(
        name='YoungModulus',
        description='Young Modulus',  # noqa
        domain=['DEM'],
        key='YOUNG_MODULUS',
        number=63,
        shape=[1],
        dtype=numpy.float64),
    'POISSON_RATIO': Keyword(
        name='PoissonRatio',
        description='Poisson Ratio',  # noqa
        domain=['DEM'],
        key='POISSON_RATIO',
        number=64,
        shape=[1],
        dtype=numpy.float64),
    'RESTITUTION_COEFFICIENT': Keyword(
        name='RestitutionCoefficient',
        description='Restitution Coefficient',  # noqa
        domain=['DEM'],
        key='RESTITUTION_COEFFICIENT',
        number=65,
        shape=[1],
        dtype=numpy.float64),
    'ROLLING_FRICTION': Keyword(
        name='RollingFriction',
        description='Rolling Friction coefficient',  # noqa
        domain=['DEM'],
        key='ROLLING_FRICTION',
        number=66,
        shape=[1],
        dtype=numpy.float64),
    'VOLUME_FRACTION': Keyword(
        name='VolumeFraction',
        description='Volume fraction',  # noqa
        domain=['FEM', 'FVM'],
        key='VOLUME_FRACTION',
        number=67,
        shape=[1],
        dtype=numpy.float64),
    'MATERIAL': Keyword(
        name='Material',
        description='Material',  # noqa
        domain=['ATM', 'DEM', 'FEM', 'FVM', 'LBM', 'SPH', 'VIS'],
        key='MATERIAL',
        number=68,
        shape=[1],
        dtype=uuid.UUID),
    'CUTOFF_DISTANCE': Keyword(
        name='CutoffDistance',
        description='Distance where force is no longer taken into account.',  # noqa
        domain=[],
        key='CUTOFF_DISTANCE',
        number=69,
        shape=[1],
        dtype=numpy.float64),
    'ENERGY_WELL_DEPTH': Keyword(
        name='EnergyWellDepth',
        description='Measurement of how strongly the two particles attract each other.',  # noqa
        domain=[],
        key='ENERGY_WELL_DEPTH',
        number=70,
        shape=[1],
        dtype=numpy.float64),
    'VAN_DER_WAALS_RADIUS': Keyword(
        name='VanDerWaalsRadius',
        description='Distance at which the intermolecular potential between the two particles is zero.',  # noqa
        domain=[],
        key='VAN_DER_WAALS_RADIUS',
        number=71,
        shape=[1],
        dtype=numpy.float64),
    'DIELECTRIC_CONSTANT': Keyword(
        name='DielectricConstant',
        description='Ratio of the permittivity of a substance to the permittivity of free space or vacuum',  # noqa
        domain=[],
        key='DIELECTRIC_CONSTANT',
        number=72,
        shape=[1],
        dtype=numpy.float64),
    'DYNAMIC_PRESSURE': Keyword(
        name='DynamicPressure',
        description='Dynamic pressure',  # noqa
        domain=['FEM', 'FVM'],
        key='DYNAMIC_PRESSURE',
        number=73,
        shape=[1],
        dtype=numpy.float64),
    'FLUX': Keyword(
        name='Flux',
        description='Flux',  # noqa
        domain=['FEM', 'FVM'],
        key='FLUX',
        number=74,
        shape=[1],
        dtype=numpy.float64),
    'HOMOGENIZED_STRESS_TENSOR': Keyword(
        name='HomogenizedStressTensor',
        description='Homogenized stress tensor',  # noqa
        domain=['FEM', 'FVM'],
        key='HOMOGENIZED_STRESS_TENSOR',
        number=75,
        shape=[9],
        dtype=numpy.float64),
    'STRAIN_TENSOR': Keyword(
        name='StrainTensor',
        description='Strain tensor',  # noqa
        domain=['FEM', 'FVM'],
        key='STRAIN_TENSOR',
        number=76,
        shape=[9],
        dtype=numpy.float64),
    'RELATIVE_VELOCITY': Keyword(
        name='RelativeVelocity',
        description='Relative velocity',  # noqa
        domain=['FEM', 'FVM'],
        key='RELATIVE_VELOCITY',
        number=77,
        shape=[3],
        dtype=numpy.float64),
    'DIFFUSION_VELOCITY': Keyword(
        name='DiffusionVelocity',
        description='Diffusion velocity',  # noqa
        domain=['FEM', 'FVM'],
        key='DIFFUSION_VELOCITY',
        number=78,
        shape=[3],
        dtype=numpy.float64),
    'STRESS_TENSOR': Keyword(
        name='StressTensor',
        description='Stress tensor',  # noqa
        domain=['FEM', 'FVM'],
        key='STRESS_TENSOR',
        number=79,
        shape=[9],
        dtype=numpy.float64),
    'VOLUME_FRACTION_GRADIENT': Keyword(
        name='VolumeFractionGradient',
        description='Volume fraction gradient',  # noqa
        domain=['FEM', 'FVM'],
        key='VOLUME_FRACTION_GRADIENT',
        number=80,
        shape=[3],
        dtype=numpy.float64),
    'COHESION_ENERGY_DENSITY': Keyword(
        name='Cohesion_Energy_Density',
        description='Work of adhesion per unit contact area',  # noqa
        domain=['DEM'],
        key='COHESION_ENERGY_DENSITY',
        number=81,
        shape=[1],
        dtype=numpy.float64),
}
