# PyGTV usage

## Install

```bash
pip install -e .
```

## CLI

```bash
shapeToVTK --help
shapeToVTK path/to/layer.shp output_prefix
```

## Python API

```python
from gtv.files.shp import read_shp
```

## ParaView

1. Export .vtu / .vtk from PyGTV
2. File -> Open in ParaView
3. Combine with DEM or simulation meshes for GIS context overlays

Maintainer: Jonathon Brunson (jonathonbrunson21@gmail.com)