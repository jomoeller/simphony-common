from simphony.material_relations.material_relation import (
    MaterialRelation)
from simphony.core.cuba import CUBA
from simphony.core.data_container import DataContainer


class LennardJones(MaterialRelation):

    """ Automatically generated implementation of the
    LennardJones material-relation

    Attributes
    ----------

    cutoffdistance : <type 'numpy.float64'>
        Cutoff Distance
    energywelldepth : <type 'numpy.float64'>
        Energy Well Depth
    vanderwaalsradius : <type 'numpy.float64'>
        Van Der Waals Radius

    """

    def __init__(
        self,
        name="LennardJones",
        materials=None,
        cutoff_distance=1.0,
        energy_well_depth=1.0,
        van_der_waals_radius=1.0
    ):
        super(LennardJones, self).__init__(
            name=name,
            description="Lennard Jones material relation",  # noqa
            parameters=DataContainer({
                CUBA.CUTOFF_DISTANCE: cutoff_distance,
                CUBA.ENERGY_WELL_DEPTH: energy_well_depth,
                CUBA.VAN_DER_WAALS_RADIUS: van_der_waals_radius,
            }),
            supported_parameters=[
                CUBA.CUTOFF_DISTANCE,
                CUBA.ENERGY_WELL_DEPTH,
                CUBA.VAN_DER_WAALS_RADIUS,
            ],
            materials=materials,
            num_materials=[1, 2],
            kind=CUBA.LENNARD_JONES
        )

    @property
    def cutoff_distance(self):
        return self._parameters[CUBA.CUTOFF_DISTANCE]

    @cutoff_distance.setter
    def cutoff_distance(self, value):
        updated_parameters = self._parameters
        updated_parameters[CUBA.CUTOFF_DISTANCE] = value
        self._parameters = updated_parameters

    @property
    def energy_well_depth(self):
        return self._parameters[CUBA.ENERGY_WELL_DEPTH]

    @energy_well_depth.setter
    def energy_well_depth(self, value):
        updated_parameters = self._parameters
        updated_parameters[CUBA.ENERGY_WELL_DEPTH] = value
        self._parameters = updated_parameters

    @property
    def van_der_waals_radius(self):
        return self._parameters[CUBA.VAN_DER_WAALS_RADIUS]

    @van_der_waals_radius.setter
    def van_der_waals_radius(self, value):
        updated_parameters = self._parameters
        updated_parameters[CUBA.VAN_DER_WAALS_RADIUS] = value
        self._parameters = updated_parameters
