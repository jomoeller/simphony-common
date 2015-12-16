import abc
from simphony.core.data_container import DataContainer

from simphony.testing.utils import create_data_container


class CheckMaterialRelation(object):

    __metaclass__ = abc.ABCMeta

    def setUp(self):
        pass

    @abc.abstractmethod
    def get_name():
        """ Returns the name of the tested relation

        """
        pass

    @abc.abstractmethod
    def get_kind():
        """ Returns the kind of the tested relation

        """
        pass

    @abc.abstractmethod
    def container_factory(self, name=None, materials=None):
        """ Create and return a given number of material relations.

        """
        pass

    def test_material_relation_name(self):
        """ Test that name is set correctly

        """

        relation = self.container_factory('foo_relation')
        original_name = relation.name
        original_name = 'foo_relation_2'

        self.assertEqual(relation.name, 'foo_relation')
        self.assertNotEqual(relation.name, original_name)

    def test_material_relation_name_default(self):
        """ Test that name is set correctly

        """

        relation = self.container_factory()
        original_name = relation.name
        original_name = 'foo_relation_2'

        self.assertEqual(relation.name, self.get_name())
        self.assertNotEqual(relation.name, original_name)

    def test_material_relation_name_update(self):
        """ Test that name is updated correctly

        """

        relation = self.container_factory()
        relation.name = 'foo_relation_2'

        self.assertEqual(relation.name, 'foo_relation_2')

    def test_material_relation_invalid_name_update(self):
        """ Test that name is updated correctly

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(TypeError):
            relation.name = 42

    def test_material_relation_description(self):
        """ Test that description is set correctly

        """

        relation = self.container_factory('foo_relation')

        self.assertNotEqual(relation.description, None)

    def test_material_relation_description_update(self):
        """ Test that description is updated correctly

        """

        relation = self.container_factory()
        extended_desc = relation.descriotion + '_extended'
        relation.descriotion = extended_desc

        self.assertEqual(relation.name, extended_desc)

    def test_material_relation_invalid_description_update(self):
        """ Test that description is updated correctly

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(TypeError):
            relation.name = 42

    def test_material_relation_parameters(self):
        """ Test that material relation parameteres are set correctly

        """

        # when
        relation = self.container_factory('foo_relation')

        # then
        self.assertEqual(relation._parameters, DataContainer())

    def test_material_relation_parameters_update(self):
        """ Test that material relation parameteres are updated correctly

        """

        # given
        relation = self.container_factory('foo_relation')

        parameters = create_data_container(
            restrict=relation.supported_parameters
        )

        # when
        relation.parameters = parameters

        # then
        self.assertEqual(relation.parameters, parameters)
        self.assertIsNot(relation.parameters, parameters)

    def test_material_relation_supported_parameters(self):
        """ Test that name is set correctly

        """
        pass

    def test_material_relation_supported_parameters_update(self):
        """ Test that name is updated correctly

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(AttributeError):
            relation.kind = "invalid attribute"

    def test_material_relation_materials(self):
        """ Test that name is set correctly

        """

    def test_material_relation_materials_update(self):
        """ Test that name is updated correctly

        """
        pass

    def test_material_relation_kind(self):
        """ Test that kind is set correctly

        """
        pass

    def test_material_relation_kind_update(self):
        """ Test that kind can't be accessed

        """

        relation = self.container_factory('foo_relation')

        with self.assertRaises(AttributeError):
            relation.kind = "invalid attribute"
