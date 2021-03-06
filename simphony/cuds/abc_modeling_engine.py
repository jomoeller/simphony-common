"""This module is part of simphony-common package. It contains
wrappers base class.
"""
from abc import ABCMeta, abstractmethod


class ABCModelingEngine(object):  # pragma: no cover
    """Abstract base class for modeling engines in SimPhoNy.

    Through this interface, the user controls and interacts with the
    simulation/calculation (which is being performed by the modeling
    engine).
    """
    __metaclass__ = ABCMeta

    def __init__(self, *args, **kwargs):
        """Initialize the engine.

        Parameters
        ----------
        cuds:
            The CUDS computational model object

        Returns
        -------

        """
        self._cuds = kwargs.get('cuds')
        self._load_cuds()

    # This class is supposed to be overridden, however it is not labeled
    # abstract, in order to be backward-compatible.
    def _load_cuds(self):
        """Load information from CUDS into the engine."""
        pass

    def get_cuds(self):
        """Get current CUDS instance."""
        return self._cuds

    @abstractmethod
    def run(self):
        """ Run the modeling engine

        Run the modeling engine using the configured settings (e.g. CM, BC,
        and SP) and the configured state data (e.g. particle, mesh and
        lattice data).
        """

    @abstractmethod
    def add_dataset(self, container):
        """Add a CUDS container

        Parameters
        ----------
        container : {ABCMesh, ABCParticles, ABCLattice}
            The CUDS container to add to the engine.

        Raises
        ------
        TypeError:
            If the container type is not supported by the engine.
        ValueError:
            If there is already a dataset with the given name.

        """

    @abstractmethod
    def remove_dataset(self, name):
        """ Remove a dataset from the engine

        Parameters
        ----------
        name: str
            name of CUDS container to be deleted

        Raises
        ------
        ValueError:
            If there is no dataset with the given name

        """

    @abstractmethod
    def get_dataset(self, name):
        """ Get the dataset

        Parameters
        ----------
        name: str
            name of CUDS container to be retrieved.

        Returns
        -------
        container :
            A proxy of the dataset named ``name`` that is stored
            internally in the Engine.

        Raises
        ------
        ValueError:
            If there is no dataset with the given name

        """

    @abstractmethod
    def get_dataset_names(self):  # pragma: no cover
        """ Returns a list of the datasets' names in the engine workspace.

        """

    @abstractmethod
    def iter_datasets(self, names=None):  # pragma: no cover
        """ Returns an iterator over a subset or all of the containers.

        Parameters
        ----------
        names : sequence of str, optional
            names of specific containers to be iterated over. If names is not
            given, then all containers will be iterated over.

        """
