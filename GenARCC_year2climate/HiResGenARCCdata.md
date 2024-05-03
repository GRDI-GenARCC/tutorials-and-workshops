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
Now we find the locations and climate data of the closest cells to our points based on the dataframe, d.
```
final=merge(WorldClim2, d, by.x=c("X"), by.y=c("idx1"), all.y=TRUE)
head(final)
```
It is possible to calculate the distance between the geographic coordinates from the climate data of WorldClim and your points with:
```
mean(final$dist1))
```
This dataset named “final” contains the geographic coordinates of the WorldClim climate dataset, not of your data points.
Use the third climate dataset that was loaded in the beginning and subsample it to get the geographic coordinates with longitude in the first column and latitude in the second column.

```
WorldClim4=subset(WorldClim3, select=c(3,4))
head(WorldClim4)
```
Reload your data points, and subset your dataframe to only keep the longitude and latitude in this order
```
Pinus=read.table("Mahony2020_pinus_Geo.tsv", header=TRUE)
head(Pinus)
length(Pinus$IID)
Pinus2=subset(Pinus, select=c(3,2))
head(Pinus2)
```
Use the function below  to obtain a dataframe with four columns (the latitude and longitude of WorldClim and the Latitude and Longitude of your points).
```
c<-FNN::get.knnx(Pinus2,WorldClim4,k=1)
```
Obtain the matching points, however, this lists which of your point is closest to every point in the worldclim dataset.
```
WorldClim4$Pinus2.x <- Pinus2$Lon[c$nn.index]
WorldClim4$Pinus2.y <- Pinus2$Lat[c$nn.index]
head(WorldClim4)
summary(WorldClim4)
```
Merge both the dataset named “final” which contains the climate data with the longitude and latitude of the WorldClim dataset with the dataset named “WorldClim4” that contains both longitude and latitude of WorldClim and of our data points
```
PinusWorldClim=merge(final, WorldClim4, by.x=c("Long", "Lat"), by.y=c("Long", "Lat"), all.x=TRUE)
head(PinusWorldClim)
summary(PinusWorldClim)
names(PinusWorldClim)[names(PinusWorldClim)=="Pinus2.x"] <- "LongitudePoints"
names(PinusWorldClim)[names(PinusWorldClim)=="Pinus2.y"] <- "LatitudePoints"
head(PinusWorldClim)
```
Now we can  graph the WorldClim points to see how far they are from your data points
```
g=ggplot(PinusWorldClim, aes(Long, Lat))
g=g+geom_point(size=4)
g=g+geom_point(color="red",size=2, aes(x=LongitudePoints,y=LatitudePoints))
g
```
![image](https://github.com/GRDI-GenARCC/tutorials-and-workshops/assets/33424749/ed3d71ba-a2e8-4603-9124-9788af1c5e7a)

## To subset for specific years
Start by selecting a climate data file that contains the bioclimate variables per year. Then repeat all the above steps and you will obtain a climate dataset that contains the bioclimate variables per year at all your geographic coordinates, you can name that file “allClimate”.
Now, reload your file with the geographic coordinates and the specific years for which you need climate data.
Merge both the file containing all the climate data for all years with the file that contains the specific years you want. You can name that file “SpecificYear”.
```
Final=merge(allClimate, SpecificYear, by.x=c(“Year”), by.y=c((“Year”))
```

