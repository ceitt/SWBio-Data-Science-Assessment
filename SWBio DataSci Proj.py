import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# read in data

Savay=pd.read_excel('Savay TPM Data.xlsx', sheet_name=None)

# assign each sheet a df

G8=Savay['G8A']

G9=Savay['G9A']

G13=Savay['G13A']

G14=Savay['G14A']

G15=Savay['G15A']

# create list of toxins

toxins=pd.read_csv('~/Desktop/Coral Venom PhD/Rotation Project 1/Toxin list.csv',header=None)
toxins=list(toxins[0])
toxins

# create list of highly putative toxins (not used yet)

tox=pd.read_csv('~/Desktop/tox.list.csv',header=None)
tPut=list(tox[0])
tPut

#check df format

G8

#elimnate unwanted genes

G8=G8[G8['Gene ID'].isin(toxins)]
G9=G9[G9['Gene ID'].isin(toxins)]
G13=G13[G13['Gene ID'].isin(toxins)]
G14=G14[G14['Gene ID'].isin(toxins)]
G15=G15[G15['Gene ID'].isin(toxins)]

# Seperate DFs by Short and Long term stress treatments

G8_CB= G8.iloc[:,[0,1,2,3,4,5,6,7,8]]
G9_CB= G9.iloc[:,[0,1,2,3,4,5,6,7,8]]
G13_CB= G13.iloc[:,[0,1,2,3,4,5,6,7,8]]
G14_CB= G14.iloc[:,[0,1,2,3,4,5,6,7,8]]
G15_CB= G15.iloc[:,[0,1,2,3,4,5,6,7,8]]

G8_RSS= G8.iloc[:,[0,9,10,11,12,13,14,15,16]]
G9_RSS= G9.iloc[:,[0,9,10,11,12,13,14,15,16]]
G13_RSS= G13.iloc[:,[0,9,10,11,12,13,14,15,16]]
G14_RSS= G14.iloc[:,[0,9,10,11,12,13,14,15,16]]
G15_RSS= G15.iloc[:,[0,9,10,11,12,13,14,15,16]]

# Seperate DF's further by samples taken at end of stress (T1) or after recovery (T2)

G8_CB1= G8.iloc[:,[0,1,2,3,4]]
G9_CB1= G9.iloc[:,[0,1,2,3,4]]
G13_CB1= G13.iloc[:,[0,1,2,3,4]]
G14_CB1= G14.iloc[:,[0,1,2,3,4]]
G15_CB1= G15.iloc[:,[0,1,2,3,4]]

G8_CB2= G8.iloc[:,[0,5,6,7,8]]
G9_CB2= G9.iloc[:,[0,5,6,7,8]]
G13_CB2= G13.iloc[:,[0,5,6,7,8]]
G14_CB2= G14.iloc[:,[0,5,6,7,8]]
G15_CB2= G15.iloc[:,[0,5,6,7,8]]

G8_RSS1= G8.iloc[:,[0,9,10,11,12]]
G9_RSS1= G9.iloc[:,[0,9,10,11,12]]
G13_RSS1= G13.iloc[:,[0,9,10,11,12]]
G14_RSS1= G14.iloc[:,[0,9,10,11,12]]
G15_RSS1= G15.iloc[:,[0,9,10,11,12]]

G8_RSS2= G8.iloc[:,[0,13,14,15,16]]
G9_RSS2= G9.iloc[:,[0,13,14,15,16]]
G13_RSS2= G13.iloc[:,[0,13,14,15,16]]
G14_RSS2= G14.iloc[:,[0,13,14,15,16]]
G15_RSS2= G15.iloc[:,[0,13,14,15,16]]

# Rename columns to simplify DFs

G8_CB1=G8_CB1.rename(columns={'CB-T1-27':'27', 'CB-T1-29':'29',	'CB-T1-32':'32', 'CB-T1-34.5':'34.5'}) 	
G9_CB1=G9_CB1.rename(columns={'CB-T1-27':'27', 'CB-T1-29':'29',	'CB-T1-32':'32', 'CB-T1-34.5':'34.5'}) 
G13_CB1=G13_CB1.rename(columns={'CB-T1-27':'27', 'CB-T1-29':'29',	'CB-T1-32':'32', 'CB-T1-34.5':'34.5'}) 
G14_CB1=G14_CB1.rename(columns={'CB-T1-27':'27', 'CB-T1-29':'29',	'CB-T1-32':'32', 'CB-T1-34.5':'34.5'}) 
G15_CB1=G15_CB1.rename(columns={'CB-T1-27':'27', 'CB-T1-29':'29',	'CB-T1-32':'32', 'CB-T1-34.5':'34.5'}) 

G8_CB2=G8_CB2.rename(columns={'CB-T2-27':'27', 'CB-T2-29':'29',	'CB-T2-32':'32', 'CB-T2-34.5':'34.5'}) 
G9_CB2=G9_CB2.rename(columns={'CB-T2-27':'27', 'CB-T2-29':'29',	'CB-T2-32':'32', 'CB-T2-34.5':'34.5'}) 
G13_CB2=G13_CB2.rename(columns={'CB-T2-27':'27', 'CB-T2-29':'29',	'CB-T2-32':'32', 'CB-T2-34.5':'34.5'}) 
G14_CB2=G14_CB2.rename(columns={'CB-T2-27':'27', 'CB-T2-29':'29',	'CB-T2-32':'32', 'CB-T2-34.5':'34.5'}) 
G15_CB2=G15_CB2.rename(columns={'CB-T2-27':'27', 'CB-T2-29':'29',	'CB-T2-32':'32', 'CB-T2-34.5':'34.5'}) 

G8_RSS1=G8_RSS1.rename(columns={'RSS-T1-27':'27', 'RSS-T1-29':'29',	'RSS-T1-32':'32', 'RSS-T1-34.5':'34.5'}) 	
G9_RSS1=G9_RSS1.rename(columns={'RSS-T1-27':'27', 'RSS-T1-29':'29',	'RSS-T1-32':'32', 'RSS-T1-34.5':'34.5'}) 
G13_RSS1=G13_RSS1.rename(columns={'RSS-T1-27':'27', 'RSS-T1-29':'29',	'RSS-T1-32':'32', 'RSS-T1-34.5':'34.5'}) 
G14_RSS1=G14_RSS1.rename(columns={'RSS-T1-27':'27', 'RSS-T1-29':'29',	'RSS-T1-32':'32', 'RSS-T1-34.5':'34.5'}) 
G15_RSS1=G15_RSS1.rename(columns={'RSS-T1-27':'27', 'RSS-T1-29':'29',	'RSS-T1-32':'32', 'RSS-T1-34.5':'34.5'}) 

G8_RSS2=G8_RSS2.rename(columns={'RSS-T2-27':'27', 'RSS-T2-29':'29',	'RSS-T2-32':'32', 'RSS-T2-34.5':'34.5'}) 
G9_RSS2=G9_RSS2.rename(columns={'RSS-T2-27':'27', 'RSS-T2-29':'29',	'RSS-T2-32':'32', 'RSS-T2-34.5':'34.5'}) 
G13_RSS2=G13_RSS2.rename(columns={'RSS-T2-27':'27', 'RSS-T2-29':'29',	'RSS-T2-32':'32', 'RSS-T2-34.5':'34.5'}) 
G14_RSS2=G14_RSS2.rename(columns={'RSS-T2-27':'27', 'RSS-T2-29':'29',	'RSS-T2-32':'32', 'RSS-T2-34.5':'34.5'}) 
G15_RSS2=G15_RSS2.rename(columns={'RSS-T2-27':'27', 'RSS-T2-29':'29',	'RSS-T2-32':'32', 'RSS-T2-34.5':'34.5'}) 

#Insert column with assigned genotype for sample tracking

G8_CB1.insert(1, 'Genotype/Sample', 'G8A-T1')
G9_CB1.insert(1, 'Genotype/Sample', 'G9A-T1')
G13_CB1.insert(1, 'Genotype/Sample', 'G13A-T1')
G14_CB1.insert(1, 'Genotype/Sample', 'G14A-T1')
G15_CB1.insert(1, 'Genotype/Sample', 'G15A-T1')

G8_CB2.insert(1, 'Genotype/Sample', 'G8A-T2')
G9_CB2.insert(1, 'Genotype/Sample', 'G9A-T2')
G13_CB2.insert(1, 'Genotype/Sample', 'G13A-T2')
G14_CB2.insert(1, 'Genotype/Sample', 'G14A-T2')
G15_CB2.insert(1, 'Genotype/Sample', 'G15A-T2')

G8_RSS1.insert(1, 'Genotype/Sample', 'G8A-T1')
G9_RSS1.insert(1, 'Genotype/Sample', 'G9A-T1')
G13_RSS1.insert(1, 'Genotype/Sample', 'G13A-T1')
G14_RSS1.insert(1, 'Genotype/Sample', 'G14A-T1')
G15_RSS1.insert(1, 'Genotype/Sample', 'G15A-T1')

G8_RSS2.insert(1, 'Genotype/Sample', 'G8A-T2')
G9_RSS2.insert(1, 'Genotype/Sample', 'G9A-T2')
G13_RSS2.insert(1, 'Genotype/Sample', 'G13A-T2')
G14_RSS2.insert(1, 'Genotype/Sample', 'G14A-T2')
G15_RSS2.insert(1, 'Genotype/Sample', 'G15A-T2')

# Re-form larger DFs first by four seperate sample times (Short term T1, T2, Long term T1, T2), then simply into the two experimental treatments (short and long term stress)

frames1=[G8_CB1,G9_CB1,G13_CB1,G14_CB1,G15_CB1]
frames2=[G8_CB2,G9_CB2,G13_CB2,G14_CB2,G15_CB2]
frames3=[G8_RSS1,G9_RSS1,G13_RSS1,G14_RSS1,G15_RSS1]
frames4=[G8_RSS2,G9_RSS2,G13_RSS2,G14_RSS2,G15_RSS2]

CB1=pd.concat(frames1)
CB2=pd.concat(frames2)
RSS1=pd.concat(frames3)
RSS2=pd.concat(frames4)

frames5=[CB1,CB2]
frames6=[RSS1,RSS2]

CB=pd.concat(frames5)
RSS=pd.concat(frames6)

#Sanity Check

CB

#Create Long format of DF

melted_df = pd.melt(CB, 
                    id_vars=['Gene ID', 'Genotype/Sample'],
                    value_vars=['27', '29', '32', '34.5'],
                    var_name='Temperature',
                    value_name='Value')

# Then pivot GenoTime to create new columns
CB_long = melted_df.pivot(index=['Gene ID', 'Temperature'],
                          columns='Genotype/Sample',
                          values='Value').reset_index()

CB_long

#Sanity Check

print(CB_long['Gene ID'].nunique())

#Breakdown DF and perform PCA analysis

X = CB_long.loc[:, ['G13A-T1', 'G13A-T2', 'G14A-T1', 'G14A-T2', 'G15A-T1', 'G15A-T2', 'G8A-T1', 'G8A-T2', 'G9A-T1', 'G9A-T2']]
Y = CB_long.loc[:, ["Gene ID", 'Temperature']]
Z = CB.loc[:, ['Genotype/Sample']]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X = scaler.fit_transform(X)

from sklearn.decomposition import PCA
PCA = PCA(n_components=2)
components = PCA.fit_transform(X)
PCA.components_

cumVar = pd.DataFrame(np.cumsum(PCA.explained_variance_ratio_)*100, 
                      columns=["cumVarPerc"])
expVar = pd.DataFrame(PCA.explained_variance_ratio_*100, columns=["VarPerc"])
pd.concat([expVar, cumVar], axis=1)\
    .rename(index={0: "PC1", 1: "PC2"})

componentsDf = pd.DataFrame(data = components, columns = ['PC1', 'PC2'])

#Reasign data types as needed to support analysis

# Check for unique indices
print("ComponentsDf index unique:", componentsDf.index.is_unique)
print("Y index unique:", Y.index.is_unique)

componentsDf = componentsDf.reset_index(drop=True)
Y = Y.reset_index(drop=True)

Y["Gene ID"] = [float(str(i).replace('Spis', "")) for i in Y["Gene ID"]]

Y['Temperature'] = Y['Temperature'].astype(float)

Y

print(Y.dtypes)

print("Z index unique:", Z.index.is_unique)

Z = Z.reset_index(drop=True)

Z =Z.astype(float,errors = 'ignore')

Z

print(Z.dtypes)

pcaDf = pd.concat([componentsDf, Y, Z], axis=1)

#Plot PCA analysis for Short Term Heat Stress

plt.figure(figsize=(12, 6))

CB_plot=sns.scatterplot(data=pcaDf, x="PC1", y="PC2", hue="Temperature", style= 'Genotype/Sample', palette='Set1')

CB_plot.set(title= 'CBASS Short Term Heat Stress', xlabel="PC2 (2.536459% Explained Varience)",
      ylabel="PC1 (92.154495% Explained Varience)")

plt.show()

#Repeat from long formatting data with RSS (Long term heat stress) data, creating PCA Analysis and plotting


melted_df = pd.melt(RSS, 
                    id_vars=['Gene ID', 'Genotype/Sample'],
                    value_vars=['27', '29', '32', '34.5'],
                    var_name='Temperature',
                    value_name='Value')

# Then pivot GenoTime to create new columns
RSS_long = melted_df.pivot(index=['Gene ID', 'Temperature'],
                          columns='Genotype/Sample',
                          values='Value').reset_index()

X1 = RSS_long.loc[:, ['G13A-T1', 'G13A-T2', 'G14A-T1', 'G14A-T2', 'G15A-T1', 'G15A-T2', 'G8A-T1', 'G8A-T2', 'G9A-T1', 'G9A-T2']]
Y1 = RSS_long.loc[:, ["Gene ID", 'Temperature']]
Z1 = RSS.loc[:, ['Genotype/Sample']]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X1 = scaler.fit_transform(X1)

from sklearn.decomposition import PCA
PCA = PCA(n_components=2)
components1 = PCA.fit_transform(X1)
PCA.components_

cumVar1 = pd.DataFrame(np.cumsum(PCA.explained_variance_ratio_)*100, 
                      columns=["cumVarPerc"])
expVar1 = pd.DataFrame(PCA.explained_variance_ratio_*100, columns=["VarPerc"])
pd.concat([expVar1, cumVar1], axis=1)\
    .rename(index={0: "PC1", 1: "PC2"})


componentsDf1 = pd.DataFrame(data = components1, columns = ['PC1', 'PC2'])

# Check for unique indices
print("ComponentsDf index unique:", componentsDf1.index.is_unique)
print("Y index unique:", Y1.index.is_unique)

componentsDf1 = componentsDf1.reset_index(drop=True)
Y1 = Y1.reset_index(drop=True)

Y1["Gene ID"] = [float(str(i).replace('Spis', "")) for i in Y1["Gene ID"]]

Y1['Temperature'] = Y1['Temperature'].astype(float)

Y1

print(Y1.dtypes)

print("Z index unique:", Z1.index.is_unique)

Z1 = Z1.reset_index(drop=True)

Z1 =Z1.astype(float,errors = 'ignore')

Z1

print(Z1.dtypes)

pcaDf1 = pd.concat([componentsDf1, Y1, Z1], axis=1)

plt.figure(figsize=(12, 6))

RSS_plot=sns.scatterplot(data=pcaDf1, x="PC1", y="PC2", hue="Temperature", style= 'Genotype/Sample', palette='Set1')

RSS_plot.set(title= 'RSS Long Term Heat Stress',xlabel="PC2 (12.449607% Explained Varience)",
      ylabel="PC1 (68.531026% Explained Varience)")

plt.show()
