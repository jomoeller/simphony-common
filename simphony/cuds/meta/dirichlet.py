import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .condition import Condition
from . import validation


class Dirichlet(Condition):
    '''Dirichlet boundary condition, specify the value the solutions takes on the boundary of the domain  # noqa
    '''

    cuba_key = CUBA.DIRICHLET

    def __init__(self, description="", name="", variable=None, material=None):

        self._data = DataContainer()

        if material is None:
            self.material = []
        if variable is None:
            self.variable = []
        self.name = name
        self.description = description
        # This is a system-managed, read-only attribute
        self._models = [CUBA.CONTINUUM]
        # This is a system-managed, read-only attribute
        self._definition = 'Dirichlet boundary condition, specify the value the solutions takes on the boundary of the domain'  # noqa

    @property
    def material(self):
        return self.data[CUBA.MATERIAL]

    @material.setter
    def material(self, value):
        value = validation.cast_data_type(value, 'material')
        validation.check_shape(value, '(:)')
        for item in value:
            validation.validate_cuba_keyword(item, 'material')
        data = self.data
        data[CUBA.MATERIAL] = value
        self.data = data

    @property
    def variable(self):
        return self.data[CUBA.VARIABLE]

    @variable.setter
    def variable(self, value):
        value = validation.cast_data_type(value, 'variable')
        validation.check_shape(value, '(:)')
        for item in value:
            validation.validate_cuba_keyword(item, 'variable')
        data = self.data
        data[CUBA.VARIABLE] = value
        self.data = data

    @property
    def models(self):
        return self._models

    @property
    def definition(self):
        return self._definition

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
        return (CUBA.DESCRIPTION, CUBA.MATERIAL, CUBA.NAME, CUBA.UUID,
                CUBA.VARIABLE)

    @classmethod
    def parents(cls):
        return (CUBA.CONDITION, CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)
