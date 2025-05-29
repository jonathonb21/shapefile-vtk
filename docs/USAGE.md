# Shapefile VTK usage

Developed by Jonathon Brunson (jonathonbrunson21@gmail.com).

## CLI

```bash
shapeToVTK --help
shapeToVTK input.shp output.vtk
```

## Python API

```python
# Add src to PYTHONPATH or install editable
from files.shp import ShpFile
```

## ParaView workflow

1. Export `.vtk` from this tool
2. Open in ParaView and apply filters as needed
3. Combine with simulation meshes for GIS context overlays