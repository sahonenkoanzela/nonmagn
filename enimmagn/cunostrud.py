from osgeo import gdal

# Open the GeoTIFF file
dataset = gdal.Open('your_geotiff_file.tif', gdal.GA_ReadOnly)

# Use the dataset object for processing or reading

# Close the dataset to release resources
dataset = None
