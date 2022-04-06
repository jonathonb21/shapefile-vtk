# PyGTV - GIS vectors to VTK for ParaView

**Maintainer:** [Jonathon Brunson](mailto:jonathonbrunson21@gmail.com)

PyGTV reads ESRI shapefiles (.shp + .dbf) and exports binary VTK meshes you can open in ParaView, VisIt, or PyVista.

Fork of [paulo-herrera/PyGTV](https://github.com/paulo-herrera/PyGTV). See ATTRIBUTION.md.

## Quick start

```bash
pip install -e .
shapeToVTK --help
python src/examples/points.py src/examples/ex1/points.shp
```

## License

MIT - see LICENSE.
<!-- history:readme-030 -->
