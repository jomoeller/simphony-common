import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .physics_equation import PhysicsEquation


class KsDft(PhysicsEquation):
    '''Kohn-Sham DFT equations  # noqa
    '''

    cuba_key = CUBA.KS_DFT

    def __init__(self, description="", name=""):

        self._data = DataContainer()

        self.name = name
        self.description = description
        # This is a system-managed, read-only attribute
        self._models = [CUBA.ELECTRONIC]
        # This is a system-managed, read-only attribute
        self._definition = 'Kohn-Sham DFT equations'  # noqa
        # This is a system-managed, read-only attribute
        self._variables = [
            CUBA.POSITION, CUBA.CHEMICAL_SPECIE, CUBA.ELECTRON_MASS,
            CUBA.CHARGE_DENSITY, CUBA.ENERGY
        ]

    @property
    def models(self):
        return self._models

    @property
    def definition(self):
        return self._definition

    @property
    def variables(self):
        return self._variables

    @property
    def data(self):
        return DataContainer(self._data)

    @data.setter
    def data(self, new_data):
        self._data = DataContainer(new_data)

    @property
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.DESCRIPTION, CUBA.UUID, CUBA.NAME)

    @classmethod
    def parents(cls):
        return (CUBA.PHYSICS_EQUATION, CUBA.MODEL_EQUATION,
                CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
