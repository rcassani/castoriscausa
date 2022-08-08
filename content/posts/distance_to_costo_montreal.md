Title: How far is a Costco in Montreal?
Date: 2022-05-28 14:00
Modified: 2022-08-07 20:00
Tags: Montreal, Python, GIS, maps, GeoPandas
Author: Raymundo Cassani
Slug: distance_to_costo_montreal
Thumbnail: dist_costco_montreal.png

<hr>
**Updated**: After receiving feedback on this post, I updated this post by adding at the end a similar map but using the driving times, rather than the Euclidean distances.
<hr>

Once clarified the [different meanings of Montreal]({filename}tale_of_too_montreal.md), I'm in a better position to solve a question inspired by a conversation with a friend, the question is:

<center>
**How far from a Costco is everyone in the Montreal?**
</center>

For city, I'll be using a map, that encompasses [all the interpretations of Montreal]({filename}tale_of_too_montreal.md).

<center>
[<img src="/images/montreals_map.png" style="width: 60%;"/>](/images/montreals_map.png)  
<br>
Map for the different "Montreal" meanings
</center>  

This post briefly describes the steps to answering the question, implemented as a script (code and data available [here](https://github.com/rcassani/Python-GIS/tree/master/E04)), using [GeoPandas](https://geopandas.org). If you only want to see the result, jump directly to the map at the end.

## Costco stores in my area
The location of the stores in the Montreal is available in their [Quebec stores listing](https://www.costco.ca/WarehouseListByStateDisplayView). These addresses were then cross-checked with [OpenStreetMap](https://www.openstreetmap.org) and Google maps. Oh surprise! the addresses did not always matched, thus, I had to verify the addressed (street number, street and postal code) with  [Canada Post](https://www.canadapost-postescanada.ca/info/mc/personal/postalcode/fpc.jsf). Interestingly the address in the Costco site were the correct. Don't worry, I've submitted the corrections in OpenStreetMap and Google maps.

There are a total of **14 stores** in the area: Sud-Ouest, Marche central, Point-Claire, Anjou, Laval, Boucherville, Longueuil, Saint-Bruno, Brossard, Candiac, Vaudreuil-Dorion, Terrebonne, Boisbriand and Saint-Jerome.

## Overview of the process
With all the information at hand, making the map as straight forward:

1. Geocoding, converting the store addresses to locations on Earth
2. Defining the map boundaries
3. Making a grid in the map
4. Computing the distance between each store location and each point in the grid
5. Finding the minimum of those distances
6. Plotting

<center>
[<img src="/images/dist_costco_montreal.png" style="width: 100%;"/>](/images/dist_costco_montreal.png)  
<br>
</center>  

This as a fun project, it can be easily modified to do the same analysis with other points for interest.

## Using driving times
How does the map change if driving times are used instead of linear distances?
To obtain map below, the [isochrone maps](https://en.wikipedia.org/wiki/Isochrone_map) were obtained for each store location with [Openrouteservice](https://openrouteservice.org/). Then, for each point in the map grid the minimum driving time to a store was selected. This is the result.

<center>
[<img src="/images/time_costco_montreal.png" style="width: 100%;"/>](/images/time_costco_montreal.png)  
<br>
</center>  

## Relation with population density?
As a quick exploration, this distance-to-Costco map above was plotted on the [2021 population density map of the area](https://www12.statcan.gc.ca/census-recensement/2021/geo/maps-cartes/thematicmaps-cartesthematiques/pd-pl/map-eng.cfm?lang=E&mapid=5&dguid=2021S0503462). The result is interesting, and led to make the prediction:

**The next Costco store in the region will open in Saint-Jean-sur-Richelieu.**

<center>
[<img src="/images/dist_costco_montreal_pop.png" style="width: 100%;"/>](/images/dist_costco_montreal_pop.png)  
<br>
Red background shades indicates high population density.
</center>  
