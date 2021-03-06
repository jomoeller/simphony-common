from simphony.core import Default  # noqa
from .cuds_component import CUDSComponent
from simphony.core.cuba import CUBA
from simphony.cuds import meta_validation


class Origin(CUDSComponent):
    """
    The origin of a space system
    """
    cuba_key = CUBA.ORIGIN

    def __init__(self, position=Default, description=Default, name=Default):
        super(Origin, self).__init__(description=description, name=name)
        self._init_position(position)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Origin, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set((CUBA.POSITION, ) + base_params))

    def _default_definition(self):
        return "The origin of a space system"  # noqa

    def _init_position(self, value):
        if value is Default:
            value = self._default_position()

        self.position = value

    @property
    def position(self):
        return self.data[CUBA.POSITION]

    @position.setter
    def position(self, value):
        value = self._validate_position(value)
        self.data[CUBA.POSITION] = value

    def _validate_position(self, value):
        value = meta_validation.cast_data_type(value, 'POSITION')
        meta_validation.check_valid_shape(value, [1], 'POSITION')
        meta_validation.validate_cuba_keyword(value, 'POSITION')
        return value

    def _default_position(self):
        return [0, 0, 0]
