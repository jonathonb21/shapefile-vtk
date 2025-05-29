# Shapefile VTK - GIS vectors to VTK for ParaView

**Developer:** [Jonathon Brunson](https://github.com/jonathonb21) | [jonathonbrunson21@gmail.com](mailto:jonathonbrunson21@gmail.com)

I built this Python library to read ESRI shapefiles (`.shp` + `.dbf`) and export binary VTK meshes for ParaView, VisIt, and PyVista. The project includes pure-Python shapefile parsers, a `shapeToVTK` CLI, and sample GIS workflows.

<p align="center">
  <img src="ex_image1.png" alt="Shapefile polygons rendered in ParaView" width="550">
  <br>
  <em>GIS polygons from a shapefile overlaid on a ParaView visualization.</em>
</p>

## Quick start

```bash
pip install -e .
shapeToVTK --help
python src/examples/points.py src/examples/ex1/points.shp
```

## Repository

https://github.com/jonathonb21/shapefile-vtk

## License

MIT - see [LICENSE](LICENSE).