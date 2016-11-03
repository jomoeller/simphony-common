import uuid
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA
from .cuds_component import CUDSComponent
from . import validation


class Node(CUDSComponent):
    '''A node on a structured grid like lattice  # noqa
    '''

    cuba_key = CUBA.NODE

    def __init__(self, index, data=None, description=None, name=None):

        self.index = index
        self.name = name
        self.description = description
        if data:
            internal_data = self.data
            internal_data.update(data)
            self.data = internal_data

        # This is a system-managed, read-only attribute
        self._definition = 'A node on a structured grid like lattice'  # noqa

    @property
    def index(self):
        return self.data[CUBA.INDEX]

    @index.setter
    def index(self, value):
        value = validation.cast_data_type(value, 'index')
        validation.validate_cuba_keyword(value, 'index')
        data = self.data
        data[CUBA.INDEX] = value
        self.data = data

    @property
    def data(self):
        try:
            data_container = self._data
        except AttributeError:
            self._data = DataContainer()
            data_container = self._data

        return DataContainer(data_container)

    @data.setter
    def data(self, new_data):
        self._data = DataContainer(new_data)

    @property
    def definition(self):
        return self._definition

    @property
    def uid(self):
        if not hasattr(self, '_uid') or self._uid is None:
            self._uid = uuid.uuid4()
        return self._uid

    @classmethod
    def supported_parameters(cls):
        return (CUBA.DESCRIPTION, CUBA.INDEX, CUBA.UUID, CUBA.NAME)

    @classmethod
    def parents(cls):
        return (CUBA.CUDS_COMPONENT, CUBA.CUDS_ITEM)