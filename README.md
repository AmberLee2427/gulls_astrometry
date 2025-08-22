# GULLS Astrometry Bolt‑On

Augment simulated microlensing light curves (generated with **GULLS**) with predicted astrometric (centroid) shifts for single, binary, and triple lens single–source (1L/2L/3L 1S) configurations.

Current focus: lightweight wrappers around `GCMicrolensing` plus centroid combination utilities that can be layered onto existing photometric simulations without modifying the original pipeline output.

## Features (Current)

- Parse GULLS-produced light curve `.lc` files (work in progress in `gulls_parser`).
- Compute model centroid trajectories for:
  - 1L1S (`Astrometry.centroid_shift_1l`)
  - 2L1S (`Astrometry.centroid_shifts_2l`)
  - 3L1S (`Astrometry.centroid_shifts_3l`)
- Flux‑weighted centroid combination (`CentroidAddition.add_centroids`).
- Simulate per‑epoch astrometric shifts by blending source + lens flux components (`CentroidAddition.simulate_astrometric_shift`).
- Quiver plot visualization prototype (`CentroidAddition.plot_astrometric_shifts`).

## Project Structure

```
src/
  astrometry/            # Wrappers around GCMicrolensing models
  centroid_addition/     # Centroid algebra & shift simulation
  gulls_parser/          # (WIP) Parsing of master + light curve files
input/                   # Sample / placeholder GULLS outputs
output/                  # Generated augmented light curves
validation/              # Notebooks for exploratory validation
tests/                   # Pytest-based unit tests
```

## Installation

(Assumes Python ≥3.11.)

```bash
pip install -e .[dev]
```

If `GCMicrolensing` or science dependencies are not on PyPI, install them per their instructions before running.

## Quick Start

```python
from astrometry.astrometry import Astrometry
from centroid_addition.centroid_addition import CentroidAddition

# Minimal 1L1S example (parameter dict mimicking GULLS output subset)
params = {"t0": 0.0, "tE": 20.0, "rho": 0.001, "u0": 0.1}
model, system, dx, dy = Astrometry.centroid_shift_1l(params)

# Flux-weighted centroid of (source + lens)
import numpy as np
positions = np.array([[0.0, 0.0], [0.3, -0.1]])  # source, lens
fluxes = np.array([1.5, 0.2])
centroid = CentroidAddition.add_centroids(positions, fluxes)
```

## Workflow (Intended)

1. Use GULLS to generate photometric light curves (and master tables).
2. Parse produced files (`GullsParser`, WIP) into DataFrames + parameter dicts.
3. Instantiate appropriate lens model via `Astrometry` utilities.
4. Merge model centroid path with observed/simulated flux history.
5. Export augmented `.lc` file including astrometric shift columns.

## Status / Limitations

- `gulls_parser` not yet fully implemented; tests scaffold expected behavior.
- Minimal validation of physical parameter ranges.
- Triple lens support: fixed internal numerical settings (`secnum`, `basenum`).
- No batch / vectorized parameter exploration yet.
- Plotting routine is a prototype (single panel quiver only).

## Roadmap (Short Term)

- Complete `GullsParser` implementation (robust I/O + metadata capture).
- Output writer for augmented light curves mirroring original format.
- Consistent unit handling & explicit Einstein radius scaling.
- Error propagation (flux → centroid uncertainty estimates).
- Improved visualization (multi-panel: photometry + astrometry + geometry).

## Testing

Run unit tests:

```bash
pytest -q
```

## Contributing

Open issues for bugs or enhancement proposals. Submit concise pull requests with tests where feasible.

## License

(Define license here.)

## Citation

Provide citation details for GULLS and GCMicrolensing when publishing results derived from this package.
