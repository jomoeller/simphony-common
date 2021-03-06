from simphony.core import Default  # noqa
from .lattice import Lattice
from simphony.core.cuba import CUBA
from simphony.cuds import meta_validation


class BravaisLattice(Lattice):
    """
    A Bravais lattice
    """
    cuba_key = CUBA.BRAVAIS_LATTICE

    def __init__(self,
                 origin,
                 primitive_cell,
                 lattice_parameter=Default,
                 size=Default,
                 description=Default,
                 name=Default):
        super(BravaisLattice, self).__init__(
            description=description, name=name)
        self._init_origin(origin)
        self._init_lattice_parameter(lattice_parameter)
        self._init_primitive_cell(primitive_cell)
        self._init_size(size)

    @classmethod
    def supported_parameters(cls):
        try:
            base_params = super(BravaisLattice, cls).supported_parameters()
        except AttributeError:
            base_params = ()
        return tuple(
            set((
                CUBA.ORIGIN,
                CUBA.LATTICE_PARAMETER,
                CUBA.PRIMITIVE_CELL,
                CUBA.SIZE, ) + base_params))

    def _default_definition(self):
        return "A Bravais lattice"  # noqa

    def _init_origin(self, value):
        if value is Default:
            value = self._default_origin()

        self.origin = value

    @property
    def origin(self):
        return self.data[CUBA.ORIGIN]

    @origin.setter
    def origin(self, value):
        value = self._validate_origin(value)
        self.data[CUBA.ORIGIN] = value

    def _validate_origin(self, value):
        value = meta_validation.cast_data_type(value, 'ORIGIN')
        meta_validation.check_valid_shape(value, [1], 'ORIGIN')
        meta_validation.validate_cuba_keyword(value, 'ORIGIN')
        return value

    def _default_origin(self):
        raise TypeError("No default for origin")

    def _init_lattice_parameter(self, value):
        if value is Default:
            value = self._default_lattice_parameter()

        self.lattice_parameter = value

    @property
    def lattice_parameter(self):
        return self.data[CUBA.LATTICE_PARAMETER]

    @lattice_parameter.setter
    def lattice_parameter(self, value):
        value = self._validate_lattice_parameter(value)
        self.data[CUBA.LATTICE_PARAMETER] = value

    def _validate_lattice_parameter(self, value):
        value = meta_validation.cast_data_type(value, 'LATTICE_PARAMETER')
        meta_validation.check_valid_shape(value, [3], 'LATTICE_PARAMETER')
        meta_validation.check_elements(value, [3], 'LATTICE_PARAMETER')

        return value

    def _default_lattice_parameter(self):
        return [1.0, 1.0, 1.0]

    def _init_primitive_cell(self, value):
        if value is Default:
            value = self._default_primitive_cell()

        self.primitive_cell = value

    @property
    def primitive_cell(self):
        return self.data[CUBA.PRIMITIVE_CELL]

    @primitive_cell.setter
    def primitive_cell(self, value):
        value = self._validate_primitive_cell(value)
        self.data[CUBA.PRIMITIVE_CELL] = value

    def _validate_primitive_cell(self, value):
        value = meta_validation.cast_data_type(value, 'PRIMITIVE_CELL')
        meta_validation.check_valid_shape(value, [1], 'PRIMITIVE_CELL')
        meta_validation.validate_cuba_keyword(value, 'PRIMITIVE_CELL')
        return value

    def _default_primitive_cell(self):
        raise TypeError("No default for primitive_cell")

    def _init_size(self, value):
        if value is Default:
            value = self._default_size()

        self.size = value

    @property
    def size(self):
        return self.data[CUBA.SIZE]

    @size.setter
    def size(self, value):
        value = self._validate_size(value)
        self.data[CUBA.SIZE] = value

    def _validate_size(self, value):
        value = meta_validation.cast_data_type(value, 'SIZE')
        meta_validation.check_valid_shape(value, [3], 'SIZE')
        meta_validation.check_elements(value, [3], 'SIZE')

        return value

    def _default_size(self):
        return [1, 1, 1]
