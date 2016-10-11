import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .material_relation import MaterialRelation
from . import validation


class SjkrCohesionForce(MaterialRelation):

    '''Additional normal force tending to maintain the contact  # noqa
    '''

    cuba_key = CUBA.SJKR_COHESION_FORCE

    def __init__(self, material, description=None, name=None, data=None, cohesion_energy_density=0.0):

        self.material = material
        self.description = description
        self.name = name
        if data:
            self.data = data
        self.cohesion_energy_density = cohesion_energy_density
        # This is a system-managed, read-only attribute
        self._models = [CUBA.ATOMISTIC]
        # This is a system-managed, read-only attribute
        self._definition = 'Additional normal force tending to maintain the contact'  # noqa
        # This is a system-managed, read-only attribute
        self._variables = []

    @property
    def data(self):
        try:
            data_container = self._data
        except AttributeError:
            self._data = DataContainer()
            return self._data
        else:
            # One more check in case the
            # property setter is by-passed
            if not isinstance(data_container, DataContainer):
                raise TypeError("data is not a DataContainer. "
                                "data.setter is by-passed.")
            return data_container

    @data.setter
    def data(self, new_data):
        if isinstance(new_data, DataContainer):
            self._data = new_data
        else:
            self._data = DataContainer(new_data)

    @property
    def cohesion_energy_density(self):
        return self.data[CUBA.COHESION_ENERGY_DENSITY]

    @cohesion_energy_density.setter
    def cohesion_energy_density(self, value):
        value = validation.cast_data_type(value, 'cohesion_energy_density')
        validation.validate_cuba_keyword(value, 'cohesion_energy_density')
        self.data[CUBA.COHESION_ENERGY_DENSITY] = value

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
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.DESCRIPTION, CUBA.COHESION_ENERGY_DENSITY, CUBA.MATERIAL, CUBA.UUID, CUBA.NAME)

    @classmethod
    def parents(cls):
        return (CUBA.MATERIAL_RELATION, CUBA.MODEL_EQUATION, CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
