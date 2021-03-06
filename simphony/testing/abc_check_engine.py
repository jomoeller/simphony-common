import abc
import uuid

from .utils import (
    compare_particles_datasets, compare_mesh_datasets,
    compare_lattice_datasets)

from ..core import CUBA
from ..cuds.particles import Particles
from ..cuds.particles_items import Particle
from ..cuds.mesh import Mesh
from ..cuds.mesh_items import Edge, Face, Cell, Point
from ..cuds.lattice import make_cubic_lattice


def grouper(iterable, group_size):
    """Given an iterable, returns groups of size group_size.
    Excess entries are not included.

    >>> grouper('abcdefg', 3)
    [('a', 'b', 'c'), ('d', 'e', 'f')]
    """
    iters = [iter(iterable)]*group_size
    return zip(*iters)


class CheckEngine(object):

    __metaclass__ = abc.ABCMeta

    def setUp(self, number_datasets_used_in_testing):
        self.maxDiff = None
        self.items = self.create_dataset_items()
        self.number_datasets_used_in_testing = number_datasets_used_in_testing

    @abc.abstractmethod
    def engine_factory(self):
        """ Create and return the container object
        """

    @abc.abstractmethod
    def create_dataset(self, name):
        """ Create and return a cuds object
        """

    @abc.abstractmethod
    def create_dataset_items(self):
        """ Create and return a list of items
        """

    @abc.abstractmethod
    def check_instance_of_dataset(self, ds):
        """ Check if a dataset is instance of a class
        """

    @abc.abstractmethod
    def compare_dataset(self, dataset, reference):
        """ compare a dataset to a reference

        """

    def test_get_missing_dataset(self):
        engine = self.engine_factory()
        with self.assertRaises(ValueError):
            engine.get_dataset('foo')

    def test_add_dataset(self):
        engine = self.engine_factory()
        reference = self.create_dataset(name='test')
        engine.add_dataset(reference)
        ds = engine.get_dataset("test")
        self.compare_dataset(ds, reference)

    def test_add_dataset_invalid(self):
        engine = self.engine_factory()

        class Invalid(object):

            def __init__(self):
                self.name = 'invalid'

        with self.assertRaises(TypeError):
            engine.add_dataset(Invalid())

    def test_add_dataset_data_copy(self):
        engine = self.engine_factory()

        reference = self.create_dataset(name='test')

        reference_data = reference.data
        reference_data[CUBA.NAME] = 'foo_name'
        reference.data = reference_data

        engine.add_dataset(reference)

        ds = engine.get_dataset('test')

        data = ds.data
        data[CUBA.NAME] = 'somename'

        # Since the returned data is always a copy,
        #  therefore the ds.data should not have changed
        self.assertNotEqual(data[CUBA.NAME], ds.data[CUBA.NAME])

        # if
        ds.data = data

        # then
        self.assertEqual(data[CUBA.NAME], ds.data[CUBA.NAME])

    def test_add_get_dataset(self):
        engine = self.engine_factory()
        reference = self.create_dataset(name='test')

        # Store dataset along with its data
        engine.add_dataset(reference)
        ds = engine.get_dataset('test')
        self.compare_dataset(ds, reference)

    def test_add_get_dataset_data(self):
        engine = self.engine_factory()

        reference = self.create_dataset(name='test')
        # Change data
        data = reference.data
        data[CUBA.NAME] = 'somename'
        reference.data = data

        # Store dataset along with its data
        engine.add_dataset(reference)
        ds = engine.get_dataset('test')
        self.compare_dataset(ds, reference)

    def test_add_dataset_with_same_name(self):
        engine = self.engine_factory()
        engine.add_dataset(self.create_dataset(name='test'))
        with self.assertRaises(ValueError):
            engine.add_dataset(
                self.create_dataset(name='test'))

    def test_get_dataset_names(self):
        engine = self.engine_factory()
        # add a few empty datasets
        ds_names = []

        for i in xrange(self.number_datasets_used_in_testing):
            name = "test_{}".format(i)
            ds_names.append(name)
            engine.add_dataset(self.create_dataset(name=name))

        # test that we are getting all the names
        names = engine.get_dataset_names()
        self.assertItemsEqual(names, ds_names)

    def test_iter_dataset(self):
        engine = self.engine_factory()
        # add a few empty datasets
        ds_names = []

        for i in xrange(self.number_datasets_used_in_testing):
            name = "test_{}".format(i)
            ds_names.append(name)
            engine.add_dataset(self.create_dataset(name=name))

        # test iterating over all
        names = [
            ds.name for ds in engine.iter_datasets()]
        self.assertItemsEqual(names, ds_names)

        # test iterating over a specific subset
        subset_index = 3 if self.number_datasets_used_in_testing > 3 \
            else self.number_datasets_used_in_testing
        subset = ds_names[:subset_index]
        names = [
            ds.name for ds in engine.iter_datasets(subset)]
        self.assertEqual(names, subset)

        for ds in engine.iter_datasets(ds_names):
            self.check_instance_of_dataset(ds)

    def test_iter_dataset_wrong(self):
        engine = self.engine_factory()
        ds_names = ["wrong1", "wrong"]

        with self.assertRaises(ValueError):
            [ds for ds in engine.iter_datasets(ds_names)]

    def test_delete_dataset(self):
        engine = self.engine_factory()
        # add a few empty datasets
        for i in xrange(self.number_datasets_used_in_testing):
            name = "test_" + str(i)
            engine.add_dataset(self.create_dataset(name=name))

        datasets_and_names = [(ds, ds.name) for ds in engine.iter_datasets()]

        # delete each of the datasets
        for (dataset, name) in datasets_and_names:
            engine.remove_dataset(name)
            # test that we can't get deleted datasets
            with self.assertRaises(ValueError):
                engine.get_dataset(name)
            # test that we can't use the deleted datasets
            with self.assertRaises(Exception):
                self.compare_dataset(dataset, dataset)

    def test_delete_non_existing_dataset(self):
        engine = self.engine_factory()
        with self.assertRaises(ValueError):
            engine.remove_dataset("foo")

    def test_dataset_rename(self):
        engine = self.engine_factory()
        engine.add_dataset(self.create_dataset(name='foo'))
        ds = engine.get_dataset("foo")
        ds.name = "bar"
        self.assertEqual(ds.name, "bar")

        # we should not be able to use the old name "foo"
        with self.assertRaises(ValueError):
            engine.get_dataset("foo")
        with self.assertRaises(ValueError):
            engine.remove_dataset("foo")
        with self.assertRaises(ValueError):
            [_ for _ in engine.iter_datasets(names=["foo"])]

        # we should be able to access using the new "bar" name
        ds_bar = engine.get_dataset("bar")
        self.assertEqual(ds_bar.name, "bar")

        # and we should be able to use the no-longer used
        # "foo" name when adding another dataset
        if self.number_datasets_used_in_testing > 1:
            ds = engine.add_dataset(self.create_dataset(name='foo'))


class ParticlesEngineCheck(CheckEngine):

    def setUp(self, number_datasets_used_in_testing=5):
        CheckEngine.setUp(self, number_datasets_used_in_testing)

    def compare_dataset(self, dataset, reference):
        compare_particles_datasets(dataset, reference, self)

    def create_dataset(self, name):
        """ Create and return a cuds object

        """
        return Particles(name=name)

    def create_dataset_items(self):
        """ Create and return a list of items
        """
        items = []
        for i in xrange(10):
            items.append(
                Particle((1.1*i, 2.2*i, 3.3*i), uid=uuid.uuid4()))
        return items


class MeshEngineCheck(CheckEngine):

    def setUp(self, number_datasets_used_in_testing=5):
        CheckEngine.setUp(self, number_datasets_used_in_testing)

    def compare_dataset(self, dataset, reference):
        compare_mesh_datasets(dataset, reference, self)

    def create_dataset(self, name):
        """ Create and return a cuds object

        """
        return Mesh(name=name)

    def create_dataset_items(self):
        """ Create and return a list of items
        """
        items = []
        point_uids = []
        for i in xrange(10):
            point = Point((1.1*i, 2.2*i, 3.3*i), uid=uuid.uuid4())
            items.append(point)
            point_uids.append(point.uid)

        for edge_points in grouper(point_uids, 2):
            edge = Edge(edge_points, uid=uuid.uuid4())
            items.append(edge)

        for face_points in grouper(point_uids, 4):
            face = Face(face_points, uid=uuid.uuid4())
            items.append(face)

        for cell_points in grouper(point_uids, 8):
            cell = Cell(cell_points, uid=uuid.uuid4())
            items.append(cell)

        return items


class LatticeEngineCheck(CheckEngine):

    def setUp(self, number_datasets_used_in_testing=5):
        CheckEngine.setUp(self, number_datasets_used_in_testing)

    def compare_dataset(self, dataset, reference):
        compare_lattice_datasets(dataset, reference, self)

    def create_dataset(self, name):
        """ Create and return a cuds object

        """
        return make_cubic_lattice(name, 1.0, (2, 3, 4))

    def create_dataset_items(self):
        """ Create and return a list of items
        """
        items = []
        for i in xrange(10):
            items.append(
                Point((1.1*i, 2.2*i, 3.3*i), uid=uuid.uuid4()))
        return items
