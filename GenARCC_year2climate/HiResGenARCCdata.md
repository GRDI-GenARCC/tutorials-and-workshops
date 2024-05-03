Sure, here is your tutorial in Git Markdown language:

# How to Retrieve Climate Data at Your Sites from the Climate Data Gathered on the GPSC for the GenARCC Project

## Steps to Access the Climate Data

1. Navigate to the GPSC under `grdi-genarcc`.
2. Follow the path: `genarcc/common/envdata/Past_Current_Climate_Canada_Wide`.
3. You can either download the data or obtain the climate data directly on the GPSC.

In this folder, you will find nine dataframes containing climate data stored as .csv files. The climate data comes from different organizations: WorldClim, TerraClimate, BioSim, and Era5-land reanalyses. It contains the 19 bioclimate variables as defined by WorldClim. 

There are two datasets per organizations, one containing yearly climate data from 1980-2018 and another one containing the average of all years. However, for ERA5-land reanalyses, there are three datasets. 

Here is the list of the files:

- `BioSimMap_avg.csv` = Average of all years from the BioSim software.
- `BioSimMap_BioClim.csv`= All years from the BioSim software.
- `ERA5_Bio_avg.csv`= Adjusted average of all years from the ERA5-land reanalyses organization.
- `ERA5_BiClim_1979_2018_adjusted.csv` = All years with climate data adjusted from the ERA5-land reanalyses organization.
- `ERA5_BioClim_1979_2018.csv` = All years with climate data not adjusted from the ERA5-land reanalyses organization.
- `TerraClimate_Bio_avg.csv`= Average of all years from the TerraClimate organization.
- `TerraClimateBioClimate.csv`= All years from the TerraClimate organization.
- `WorldClim_Bio_avg.csv` = Average of all years from the WorldClim organization.
- `WorldClim_BioClim_CanadaWide.csv` = All years from the WorldClim organization.

## R Libraries

You will need the following R libraries:

```R
# knn functions
library(spatialEco)
library(RANN)
library(FNN)

# Handle geographic coordinate
library(rgdal)
library(rnaturalearth)
library(rnaturalearthdata)
library(sf)
library(sp)

# Data handling and reshaping
library(tidyr)
library(reshape2)

# Graph
library(ggplot2)
library(ggspatial)
library(ggsn)
library(ggthemes)
```

## Example Using the WorldClim Climate Data

Read the WorldClim climate data.

```R
WorldClim=read.csv("WorldClim_Bio_avg.csv", header=TRUE)
head(WorldClim)
tail(WorldClim)
summary(WorldClim)
```
Plot the data if you want to see it.

```R
g=ggplot(WorldClim, aes(Long, Lat))
g=g+geom_point(aes(color=bio1))
g
```
![image](https://github.com/GRDI-GenARCC/tutorials-and-workshops/assets/33424749/4421fcf9-0f36-4102-b9cb-d652493065e7)

You will need to load the data three times with different names.
```
WorldClim2=read.csv("WorldClim_Bio_avg.csv", header=TRUE)
head(WorldClim2)
summary(WorldClim2)

WorldClim3=read.csv("WorldClim_Bio_avg.csv", header=TRUE)
head(WorldClim3)
summary(WorldClim3)
```
Find the closest points from a dataframe (your GPS coordinates) that match the bioclimate variables in the WorldClim dataset.
Transform the coordinates from the WorldClim dataset into geographic coordinates system
```
coordinates(WorldClim) <- ~ Long + Lat
```
Store the coordinates in the “WorldClimGeo” object.
```
WorldClimGeo =coordinates(WorldClim)
head(WorldClimGeo)
```
Load your dataset containing the geographic locations you want to obtain climate.

```
Pinus=read.table("Mahony2020_pinus_Geo.tsv", header=TRUE)
head(Pinus)
length(Pinus$IID)
```
Transform the coordinates stored in your file into coordinates belonging to a geographic system, and store the coordinates in the “PinusGeo” object.

```
coordinates(Pinus) <- ~ Lon + Lat
PinusGeo=coordinates(Pinus)
head(PinusGeo)
str(PinusGeo)
```
Now we use the knn function to find the coordinates of the climate dataframe that is the closest (now stored in the “WorldClimGeo” object) to your data points that are now stored as the object named “PinusGeo”.

```
d=spatialEco::knn(PinusGeo, WorldClimGeo, k=1, indexes=TRUE)
head(d)
```
We need to relate the values of the idx column to the climate dataset. However, we removed the latitude and longitude from the climate dataset since we transformed the coordinates for using the knn function. This is why we loaded the climate dataset twice with two different names.
Now we find the locations and climate data of the closest cells to our points based on the dataframe name d
```
final=merge(WorldClim2, d, by.x=c("X"), by.y=c("idx1"), all.y=TRUE)
head(final)
```

