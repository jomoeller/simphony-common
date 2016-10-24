import unittest

from simphony.core.cuba import CUBA
from simphony.core.data_container import DataContainer


class TestDataContainer(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_initialization_with_a_dictionary(self):
        data = {key: key + 3 for key in CUBA}
        container = DataContainer(data)
        self.assertEqual(container, data)
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_initialization_with_a_iterable(self):
        data = [(key,  key + 3) for key in CUBA]
        container = DataContainer(data)
        for key, value in data:
            self.assertEqual(container[key], value)
            self.assertIsInstance(key, CUBA)

    def test_initialization_with_keywords(self):
        data = {key: index + 3 for index, key in enumerate(CUBA.__members__)}
        container = DataContainer(**data)
        self.assertEqual(
            container, {key: index + 3 for index, key in enumerate(CUBA)})
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_initialization_with_keywords_and_iterable(self):
        data = {
            key: index + 3 for index, key in enumerate(CUBA.__members__)
            if key != str(CUBA(10))[5:]}
        container = DataContainer([(CUBA(10), 23)], **data)
        expected = {key: index + 3 for index, key in enumerate(CUBA)}
        expected[CUBA(10)] = 23
        self.assertDictEqual(container, expected)
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_initialization_with_non_cuba_kwards(self):
        with self.assertRaises(ValueError):
            DataContainer(bar=5)

    def test_initialization_with_non_cuba_dict(self):
        with self.assertRaises(ValueError):
            DataContainer({'foo': 5})

    def test_initialization_with_non_cuba_iterable(self):
        with self.assertRaises(ValueError):
            DataContainer([('foo', 5)])

    def test_initialization_with_multiple_arguments(self):
        with self.assertRaises(TypeError):
            DataContainer([('foo', 5)], 45)

    def test_initialization_with_a_dictionary_of_ints(self):
        data = {int(key): key + 3 for key in CUBA}
        with self.assertRaises(ValueError):
            DataContainer(data)

    def test_initialization_with_generator(self):
        generator = ((key, key + 3) for key in CUBA)
        container = DataContainer(generator)
        self.assertEqual(len(container), len(CUBA))

    def test_initialization_with_non_cuba_generator(self):
        generator = (('foo'+str(i), i) for i in range(5))
        with self.assertRaises(ValueError):
            DataContainer(generator)

    def test_update_with_a_dictionary(self):
        container = DataContainer()
        data = {key: key + 3 for key in CUBA}
        container.update(data)
        self.assertEqual(container, data)
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_update_with_a_dictionary_of_ints(self):
        container = DataContainer()
        data = {int(key): key + 3 for key in CUBA}
        with self.assertRaises(ValueError):
            container.update(data)

    def test_update_with_a_iterable(self):
        container = DataContainer()
        data = [(key,  key + 3) for key in CUBA]
        container.update(data)
        # Check that has all the values
        for key, value in data:
            self.assertEqual(container[key], value)
            self.assertIsInstance(key, CUBA)

    def test_update_with_keywords(self):
        container = DataContainer()
        data = {key: index + 3 for index, key in enumerate(CUBA.__members__)}
        container.update(**data)
        self.assertEqual(
            container, {key: index + 3 for index, key in enumerate(CUBA)})
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_update_with_keywords_and_iterable(self):
        container = DataContainer()
        data = {
            key: index + 3 for index, key in enumerate(CUBA.__members__)
            if key != str(CUBA(10))[5:]}
        container.update([(CUBA(10), 23)], **data)
        expected = {key: index + 3 for index, key in enumerate(CUBA)}
        expected[CUBA(10)] = 23
        self.assertDictEqual(container, expected)
        for key in container:
            self.assertIsInstance(key, CUBA)

    def test_update_with_non_cuba_kwards(self):
        container = DataContainer()
        with self.assertRaises(ValueError):
            container.update(bar=5)

    def test_update_with_non_cuba_dict(self):
        container = DataContainer()
        with self.assertRaises(ValueError):
            container.update({'foo': 5})

    def test_update_with_non_cuba_iterable(self):
        container = DataContainer()
        with self.assertRaises(ValueError):
            container.update([('foo', 5)])

    def test_setitem_with_int_key(self):
        container = DataContainer()
        with self.assertRaises(ValueError):
            container[10] = 29

    def test_setitem_with_cuba_key(self):
        container = DataContainer()
        container[CUBA(10)] = 29
        self.assertIsInstance(container.keys()[0], CUBA)
        self.assertEqual(container[CUBA(10)], 29)

    def test_setitem_with_non_cuba_key(self):
        container = DataContainer()
        with self.assertRaises(ValueError):
            container[100] = 29

    def test_new_with_restricted_keys(self):
        restricted_keys = frozenset([CUBA.UUID, CUBA.NAME])
        container = DataContainer.new_with_restricted_keys(restricted_keys)
        self.assertEqual(container.restricted_keys, restricted_keys)

        container[CUBA.NAME] = "foo"

        with self.assertRaises(ValueError):
            container[CUBA.DESCRIPTION] = "hello"


if __name__ == '__main__':
    unittest.main()
