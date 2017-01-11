from simphony.core import Default  # noqa
from simphony.core.cuba import CUBA
from .physics_equation import PhysicsEquation


class ElectrostaticModel(PhysicsEquation):
    """
    Electrostatic model
    """
    cuba_key = CUBA.ELECTROSTATIC_MODEL

    def __init__(self, description=Default, name=Default):

        super(ElectrostaticModel, self).__init__(
            description=description, name=name)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(ElectrostaticModel, cls).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _default_models(self):
        return []  # noqa

    def _default_definition(self):
        return "Electrostatic model"  # noqa
