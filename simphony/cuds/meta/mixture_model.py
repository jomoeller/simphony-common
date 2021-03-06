from simphony.core import Default  # noqa
from simphony.core.cuba import CUBA
from .physics_equation import PhysicsEquation


class MixtureModel(PhysicsEquation):
    """
    Mixture (drift flux) model
    """
    cuba_key = CUBA.MIXTURE_MODEL

    def __init__(self, description=Default, name=Default):
        super(MixtureModel, self).__init__(description=description, name=name)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(MixtureModel, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set(() + base_params))

    def _default_models(self):
        return ['CUBA.CONTINUUM']  # noqa

    def _default_definition(self):
        return "Mixture (drift flux) model"  # noqa
