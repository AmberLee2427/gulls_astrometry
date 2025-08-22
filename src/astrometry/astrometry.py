"""Astrometric microlensing utilities.

This module provides a thin convenience wrapper around the ``GCMicrolensing``
package for computing photometric–astrometric microlensing trajectories for
single-, binary-, and triple-lens, single-source (1S) configurations.  It
exposes helper methods to (a) sanitize and subset user supplied dictionaries
of physical / model parameters and (b) compute the centroid shift (astrometric
signal) relative to the unmagnified source position.

Notes
-----
The functions here intentionally return both the instantiated model object and
its first (and currently only) *system* entry so that callers can either drill
into the full time series / attributes or just access derived centroid shift
arrays.  No attempt is made (yet) to validate physical ranges of inputs – only
presence / naming – because the canonical validation is delegated to the
``GCMicrolensing`` constructors.

Pending Improvements
--------------------
* Robust error handling & input validation.
* Support for multi-system batches.
* Vectorised interfaces for larger parameter ensembles.
"""

import os, pathlib  # noqa: F401 (kept for potential future file I/O use)
from astropy.io import ascii  # noqa: F401
import matplotlib.pyplot as plt  # noqa: F401
import numpy as np  # noqa: F401
from GCMicrolensing import TwoLens1S
from GCMicrolensing import ThreeLens1S
from GCMicrolensing import OneL1S


class Astrometry:
    """Namespace class with static helpers for microlensing astrometry.

    All methods are ``@staticmethod`` so the class is used purely as a logical
    container (no instance state is stored).  Returned centroid shifts are in
    the same units as provided by the underlying ``GCMicrolensing`` models
    (typically Einstein radii unless the package has been configured
    otherwise).
    """

    @staticmethod
    def read_dic(data, lenses):
        """Extract a subset of model parameters from an input mapping.

        Parameters
        ----------
        data : Mapping[str, Any]
            Dictionary-like object containing candidate model parameters.
        lenses : int
            Number of lens masses in the configuration (1, 2, or 3).

        Returns
        -------
        dict
            A dictionary containing only those keys relevant for the chosen
            lens configuration and present in ``data``.

        Raises
        ------
        ValueError
            If ``lenses`` is not one of {1, 2, 3}.

        Notes
        -----
        The function is intentionally tolerant: it silently skips keys that
        are *expected* but absent from ``data`` rather than raising.  It is
        assumed that downstream constructors will surface any missing required
        parameters.
        """
        if lenses == 1:
            keys = ["t0", "tE", "rho", "u0"]
        elif lenses == 2:
            keys = ["t0", "tE", "rho", "u0", "q", "s", "alpha", "BJD"]
        elif lenses == 3:
            keys = ["t0", "tE", "rho", "u0", "q2", "q3", "s2", "s3", "alpha", "psi"]
        else:
            raise ValueError("lenses must be 1, 2, or 3")

        return {k: data[k] for k in keys if k in data}

    @staticmethod
    def centroid_shift_1l(data):
        """Compute centroid shift for a single-lens single-source (1L1S) model.

        Parameters
        ----------
        data : Mapping[str, Any]
            Parameter dictionary containing at minimum: ``t0``, ``tE``,
            ``rho``, and either ``u0`` or ``u0_list``. ``u0_list`` is passed
            through verbatim if present; otherwise ``u0`` is wrapped / reused.

        Returns
        -------
        single_model : OneL1S
            Instantiated GCMicrolensing single-lens model object.
        one_system : dict-like
            The first (and only) system entry from ``single_model.systems``.
        dx : ndarray
            Centroid shift in x (cent_x_hr - x_src_hr).
        dy : ndarray
            Centroid shift in y (cent_y_hr - y_src_hr).
        """
        args = {
            "t0": data["t0"],
            "tE": data["tE"],
            "rho": data["rho"],
            "u0_list": data.get("u0_list", data["u0"]),
        }

        single_model = OneL1S(**args)
        one_system = single_model.systems[0]
        dx = one_system['cent_x_hr'] - one_system['x_src_hr']
        dy = one_system['cent_y_hr'] - one_system['y_src_hr']
        return single_model, one_system, dx, dy

    @staticmethod
    def centroid_shifts_2l(data):
        """Compute centroid shifts for a binary-lens single-source (2L1S) model.

        Parameters
        ----------
        data : Mapping[str, Any]
            Parameter dictionary. Required keys: ``t0``, ``tE``, ``rho``, and
            either ``u0`` or ``u0_list``. Mass ratio can be given as ``q`` or
            ``q2``; separation as ``s`` or ``s2``. Orientation: ``alpha``.
            A time grid may be supplied via ``BJD`` (preferred) or ``t_lc``.

        Returns
        -------
        double_model : TwoLens1S
            Instantiated GCMicrolensing binary-lens model object.
        two_system : dict-like
            The first system entry from ``double_model.systems``.
        delta_x : ndarray
            Centroid shift in x.
        delta_y : ndarray
            Centroid shift in y.

        Notes
        -----
        This routine performs *minimal* key normalization / aliasing to
        accommodate common naming conventions. Additional preprocessing (e.g.,
        unit conversion) should occur prior to invocation if needed.
        """
        args = {
            "t0": data["t0"],
            "tE": data["tE"],
            "rho": data["rho"],
            "u0_list": data.get("u0_list", data["u0"]),  # accepts either name
            "q": data.get("q", data.get("q2")),           # q or q2
            "s": data.get("s", data.get("s2")),           # s or s2
            "alpha": data["alpha"],                        # position angle
            "t_lc": data.get("BJD", data.get("t_lc")),    # accept BJD or t_lc
        }

        double_model = TwoLens1S(**args)
        two_system = double_model.systems[0]
        delta_x = two_system['cent_x_hr'] - two_system['x_src_hr']
        delta_y = two_system['cent_y_hr'] - two_system['y_src_hr']
        return double_model, two_system, delta_x, delta_y

    @staticmethod
    def centroid_shifts_3l(data):
        """Compute centroid shifts for a triple-lens single-source (3L1S) model.

        Parameters
        ----------
        data : Mapping[str, Any]
            Parameter dictionary with keys: ``t0``, ``tE``, ``rho``, ``u0`` or
            ``u0_list``, secondary and tertiary mass ratios (``q2``, ``q3``),
            projected separations (``s2``, ``s3``), orientation angles
            (``alpha``, optional ``psi``), and optionally an Einstein radius
            scaling ``rs`` plus a time grid ``BJD`` or ``t_lc``.

        Returns
        -------
        triple_model : ThreeLens1S
            Instantiated GCMicrolensing triple-lens model object.
        triple_system : dict-like
            The first system entry from ``triple_model.systems``.
        delta_x_three : ndarray
            Centroid shift in x.
        delta_y_three : ndarray
            Centroid shift in y.

        Notes
        -----
        Fixed values for ``secnum`` and ``basenum`` are currently hard-coded
        (45 and 2 respectively); expose them as parameters if variability is
        required. ``num_points`` is inferred from an available time grid and
        defaults to zero if none is present (the underlying constructor may
        then raise).
        """
        secnum = 45
        basenum = 2

        args = {
            "t0": data["t0"],
            "tE": data["tE"],
            "rho": data["rho"],
            "u0_list": data.get("u0_list", data["u0"]),
            "q2": data["q2"],
            "q3": data["q3"],
            "s2": data["s2"],
            "s3": data["s3"],
            "alpha_deg": data["alpha"],             # position angle primary-secondary
            "psi_deg": data.get("psi"),              # position angle tertiary (optional)
            "rs": data.get("rs"),                   # Einstein radius scaling (optional)
            "secnum": secnum,
            "basenum": basenum,
            "num_points": len(data.get("BJD", data.get("t_lc", []))),
        }

        triple_model = ThreeLens1S(**args)
        triple_system = triple_model.systems[0]
        delta_x_three = triple_system['cent_x_hr'] - triple_system['x_src_hr']
        delta_y_three = triple_system['cent_y_hr'] - triple_system['y_src_hr']
        return triple_model, triple_system, delta_x_three, delta_y_three
