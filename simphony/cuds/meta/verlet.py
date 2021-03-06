from simphony.core import Default  # noqa
from .computational_method import ComputationalMethod
from simphony.core.cuba import CUBA


class Verlet(ComputationalMethod):
    """
    Newtonian dynamics integration using verlet algorithm
    """
    cuba_key = CUBA.VERLET

    def __init__(self, description=Default, name=Default):
        super(Verlet, self).__init__(description=description, name=name)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(Verlet, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(set(() + base_params))

    def _default_definition(self):
        return "Newtonian dynamics integration using verlet algorithm"  # noqa

    def _default_physics_equations(self):
        return ['CUBA.MOLECULAR_DYNAMICS']  # noqa
