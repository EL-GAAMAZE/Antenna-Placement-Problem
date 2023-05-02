import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import geomaroc
from shapely.geometry import Point
import data

#read the file
solution_df= pd.read_excel('solution.xlsx')
solution=solution_df.values
# create a list to store all the GeoDataFrames
regions = []

# iterate over each region id and fetch its GeoDataFrame
for region in range(1, 13):
    regions.append(geomaroc.getRegion(id_region=region))

# merge all the GeoDataFrames into a single GeoDataFrame
merged_regions = gpd.GeoDataFrame(pd.concat(regions, ignore_index=True), crs=regions[0].crs)

# plot the merged GeoDataFrame
ax = merged_regions.plot(figsize=(15, 15), alpha=0.2, edgecolor='k')


potential_sites=[Point(xy) for xy in zip(data.potential_sites_df['lng'], data.potential_sites_df['lat'])]
cities = [Point(xy) for xy in zip(data.cities_df['lng'], data.cities_df['lat'])]
solution = [Point(xy) for xy in zip(solution_df['lng'], solution_df['lat'])]

gpd.GeoSeries([cities[0]]).plot(ax=ax,label="cities", markersize=10,color="red")
for city in cities[1:]:
    gpd.GeoSeries([city]).plot(ax=ax, markersize=10,color="red")
gpd.GeoSeries([potential_sites[0]]).plot(ax=ax,label="potential_sites", markersize=10,color="blue")
for city in potential_sites[1:]:
    gpd.GeoSeries([city]).plot(ax=ax, markersize=10,color="blue")
gpd.GeoSeries([solution[0]]).plot(ax=ax,label="solution", markersize=10,color="yellow")
for city in solution[1:]:
    gpd.GeoSeries([city]).plot(ax=ax, markersize=10,color="yellow")

ax.set_title('MOROCCO')
ax.legend(loc='upper left')
plt.show()