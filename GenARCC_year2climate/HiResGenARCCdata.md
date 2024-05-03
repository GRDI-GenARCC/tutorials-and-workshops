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
