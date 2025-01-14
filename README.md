# Stylophora pistillata Putative Venom Gene Expression Analysis from Savary et al. 2021
##### The file SWBio DataSci Proj.py contains the script for performing a PCA analysis and visulaization for Long term (RSS) and Short term (CB) heat stress experiemtns conducted by Savary et al. 2021

## Dependencies
##### This script requires Python vrersion 3.12.2
##### Aditionally: 
##### Pandas, seaborn, numpy, sklearn and matplotlib.pyplot
###### These packages can be installed using: 

        pip3 install pandas seaborn numpy matplotlib scikit-learn

## Running the Script
#### Download python script and file 'Savary  TPM Data.xlsx' to the same folder
#### Working in the same folder, run the script as written to produce the PCA visulazations for the RSS (long term) and CB (short term) heat stress groups
#### The script will output two plots, 'CBASS Short Term Heat Stress' and 'RSS Long Term Heat Stress which will save into the working folder
###### See 'CB.png' and 'RSS.png' for output plots

## Data Frames
### There are several data frames that are created in this script.
#### The first set of data frames are those that are extracting the data from each sheet of the Excel file, which are seperated by assigned sample genotype (G8-15)
#### The second set are those same dataframes, but cut down to only contain the 37 target putative toxin genes with which the analysis will be performed
##### This is done with each of the 5 genotype data frames
#### The data frames are then seperated by the treatment types, either the short term (CB) or long term (RSS) treatments
###### ie. G8_CB or G8_RSS
#### The ten seperate data sheets are then further broken down based on if the samples were taken at the end of the stress event (T1) or at the time of recovery (T2)
###### ie. G8_CB1/G8_CB2 or G8_RSS1/G8_RSS2
#### This leaves a total of 20 data frames, 10 for each treatment

## Sample Tracking
#### The next section of code adds in a colunm for each of the 20 dataframes
#### This colunm is a repeated value that indicates within the dataframe to which group the samples belong
###### ie. G8-T1/G8-T2
#### This was done without including which treatment group the samples belong to as these treatment groups will remain seperate

## Data Consolidation
### The ten data frames from each treatment are then consolidated
#### This is frist done by creating four data frames, one for two within each treatment for the two samples groups
###### ie. CB1/ CB2 and RSS1/ RSS2 which each contain the corisponding sample data from all five genotypes
#### The four data frames are then further consolidated into two final data frames, one for each treatment containing both sample times
###### The two data frames are CD and RSS

## Preparing for the PCA
#### The data frames are first re-ordered from a wide format to a long format and reorder data to allow for a PCA to be performed
#### Next, the data frame is broken up to support the components of the PCA and the appropriate commands applied
##### These comands run the PCA and select the two principal components

## PCA
#### Once the two principal components are selected by the program, the cumulative variance and percentage of explain variance are calculated for these two components
###### The cumulative explained variance for the prinical components of CB is 94.69%, and of RSS is 80.98%

## Visualization
#### The broken down data frames as well as the principal component data are then consolidated into one data frame, and plotted
#### Plotting is done using a seaborn scatterplot , and all code for customized labels are colors are included
###### To adjust plot title edit infomation following 'title=' in 'df'_plot.set
###### To adjust axis titles edit infomation following 'xlabel' or 'ylabel' in 'df'_plot.set
###### Color palette can be adjusted by changing the setting of 'palette='

## Additional information
#### Before each of the visulaization there are several lines of code which adjust the data types of the data frames
#### This is done to allow for all data frames to be consolicated into one using pd.concat
