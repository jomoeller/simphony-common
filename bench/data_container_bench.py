from __future__ import print_function

import random

from .util import bench
from simphony.core.data_container import DataContainer
from simphony.core.cuba import CUBA

dict_data = {key: 3 for key in CUBA}
data_container = DataContainer(dict_data)
indices = [key for key in CUBA]
random.shuffle(indices)


def data_container_setup():
    return DataContainer(dict_data)


def iteration(container):
    for i in container:
        pass


def getitem_access(data, indices):
    return [data[index] for index in indices]


def setitem_with_CUBA_keys(data):
    for item in CUBA:
        data[item] = str(item)
    return data


def main():
    print("""
    Benchmarking various operations between different data containers

    .. note:

        Only the relative time taken for each type of container within a
        section is comparable.

    """)
    print('Initialization:')
    print("dict:", bench(lambda: dict(dict_data)))
    print("DataContainer:", bench(lambda: DataContainer(dict_data)))
    print("dict == DataContainer", dict(dict_data) == DataContainer(dict_data))
    print()
    print('Iterations:')
    print("dict:", bench(lambda: iteration(dict_data)))
    print("DataContainer:", bench(lambda: iteration(data_container)))
    print()
    print('getitem access:')
    print("dict:", bench(lambda: getitem_access(dict_data, indices)))
    print(
        "DataContainer:",
        bench(lambda: getitem_access(data_container, indices)))
    print(
        "dict == DataContainer",
        getitem_access(dict_data, indices) == getitem_access(data_container, indices))  # noqa
    print()
    print('setitem with CUBA keys:')
    print("dict:", bench(lambda: setitem_with_CUBA_keys(dict_data)))
    print(
        "DataContainer:",
        bench(lambda: setitem_with_CUBA_keys(data_container)))
    print(
        "dict == DataContainer",
        setitem_with_CUBA_keys(dict_data) == setitem_with_CUBA_keys(data_container))  # noqa


if __name__ == '__main__':
    main()
