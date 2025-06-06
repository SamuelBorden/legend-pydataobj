"""Routines from reading and writing LEGEND Data Objects in HDF5 files.
Currently the primary on-disk format for LGDO object is LEGEND HDF5 (LH5) files. IO
is done via the class :class:`.store.LH5Store`. LH5 files can also be
browsed easily in python like any `HDF5 <https://www.hdfgroup.org>`_ file using
`h5py <https://www.h5py.org>`_.
"""

from __future__ import annotations

from .core import read, read_as, write
from .iterator import LH5Iterator
from .store import LH5Store
from .tools import ls, show
from .utils import read_n_rows

__all__ = [
    "LH5Iterator",
    "LH5Store",
    "concat",
    "default_hdf5_settings",
    "ls",
    "read",
    "read_as",
    "read_n_rows",
    "reset_default_hdf5_settings",
    "show",
    "write",
]
