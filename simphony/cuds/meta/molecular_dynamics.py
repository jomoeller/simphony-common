from simphony.core import Default  # noqa
from simphony.core.cuba import CUBA
from .physics_equation import PhysicsEquation


class MolecularDynamics(PhysicsEquation):
    """
    Classical atomistic molecular dynamics using Newtons
    equations of motion
    """
    cuba_key = CUBA.MOLECULAR_DYNAMICS

    def __init__(self, description=Default, name=Default):

        super(MolecularDynamics, self).__init__(
            description=description, name=name)

    def supported_parameters(self):
        try:
            base_params = super(MolecularDynamics, self).supported_parameters()
        except AttributeError:
            base_params = ()

        return () + base_params

    def _default_models(self):
        return ['CUBA.ATOMISTIC']  # noqa

    def _default_definition(self):
        return "Classical atomistic molecular dynamics using Newtons equations of motion"  # noqa

    def _default_variables(self):
        return [
            'CUBA.POSITION', 'CUBA.VELOCITY', 'CUBA.MOMENTUM',
            'CUBA.ACCELERATION', 'CUBA.FORCE'
        ]  # noqa
