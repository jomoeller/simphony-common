from simphony.core import Default  # noqa
from simphony.cuds import meta_validation
from simphony.core.cuba import CUBA
from .physics_equation import PhysicsEquation


class GravityModel(PhysicsEquation):
    """
    A simple gravity model
    """
    cuba_key = CUBA.GRAVITY_MODEL

    def __init__(self, acceleration=Default, description=Default,
                 name=Default):
        super(GravityModel, self).__init__(description=description, name=name)
        self._init_acceleration(acceleration)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(GravityModel, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set((CUBA.ACCELERATION, ) + base_params))

    def _default_models(self):
        return ['CUBA.MESOSCOPIC', 'CUBA.CONTINUUM']  # noqa

    def _default_definition(self):
        return "A simple gravity model"  # noqa

    def _default_variables(self):
        return ['CUBA.ACCELERATION']  # noqa

    def _init_acceleration(self, value):
        if value is Default:
            value = self._default_acceleration()

        self.acceleration = value

    @property
    def acceleration(self):
        return self.data[CUBA.ACCELERATION]

    @acceleration.setter
    def acceleration(self, value):
        value = self._validate_acceleration(value)
        self.data[CUBA.ACCELERATION] = value

    def _validate_acceleration(self, value):
        value = meta_validation.cast_data_type(value, 'ACCELERATION')
        meta_validation.check_valid_shape(value, [1], 'ACCELERATION')
        meta_validation.validate_cuba_keyword(value, 'ACCELERATION')
        return value

    def _default_acceleration(self):
        return [0.0, 0.0, 0.0]
