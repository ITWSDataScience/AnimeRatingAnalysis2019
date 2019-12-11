import pandas as pd 
import matplotlib.pyplot as plt 
import csv
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm
from scipy.interpolate import interp1d

data = pd.read_csv("../anime-recommendations-database/anime.csv")


####################################
#DATA CLEANING#
print(data["genre"])
print(data.dtypes)


#drop rows with at least one missing value
data = data.dropna()


#drop rows with the hetnai category by applying a boolean mask over the dataframe
data = data[data.genre.apply(lambda x: 'hentai' not in x.lower())]
data = data[data.genre.apply(lambda x: 'movie' not in x.lower())]
data = data[data.episodes != "Unknown"]
data.episodes = data.episodes.astype(int)

print(data["episodes"])
print(data.dtypes)

members = []
ratings = []
episodes = []

for index, row in data.iterrows():
	if row["members"] > 5000000:
		continue
	if np.isnan(row["episodes"]) or row["episodes"] < 1:
		continue
	if row["episodes"] > 500:
		continue
	members.append(row["members"])
	ratings.append(row["rating"])
	episodes.append(int(row["episodes"]))

plt.figure(num=1, figsize=(20,10))
plt.title("Anime Ratings vs Members")
plt.scatter(members, ratings)
plt.xlabel("Members")
plt.ylabel("Ratings")

npepisodes = np.array(episodes)
npmembers = np.array(members)
npratings = np.array(ratings)

regmembers = npmembers.reshape(-1,1)
regratings = npratings.reshape(-1,1)

lr = LinearRegression()
lr.fit(regmembers, regratings)

prediction = lr.predict(regmembers)
plt.plot(regmembers, prediction, color="red")

slope = (prediction[2] - prediction[1])/ (regmembers[2] - regmembers[1])
print(slope)


##Histogram of data 
plt.figure(num=2, figsize=(20,10))
h = np.hstack(npmembers)
plt.title("Amount of Members per Anime")
plt.ylabel("Number of Animes")
plt.hist(h, bins='auto')
plt.xlabel("Members")






#Local weighted regression
plt.figure(num=3, figsize=(20,10))
plt.title("Locally Weighted Regression for Anime Ratings vs Members")
lowess = sm.nonparametric.lowess(npratings, npmembers, frac=.3)

lowx = list(zip(*lowess))[0]
lowy = list(zip(*lowess))[1]

inter = interp1d(lowx, lowy, bounds_error=False)



plt.plot(npmembers, npratings, "o")
plt.plot(lowx, lowy, "*")
plt.xlabel("Members")
plt.ylabel("Ratings")



plt.figure(4)
plt.title("Members per Anime")
plt.ylabel("Members")
mdata = pd.DataFrame(npmembers, columns=["members"])
membersboxplot = mdata.boxplot(column = ["members"])
plt.xlabel("Animes")

plt.figure(5)
plt.title("Ratings per Anime")
plt.ylabel("Rating")
rdata = pd.DataFrame(npratings, columns=["rating"])
ratingsboxplot = rdata.boxplot(column = ["rating"])
plt.xlabel("Animes")




#Lowess for Episodes
plt.figure(num=6, figsize=(20,10))
plt.title("Locally Weighted Regression for Anime Ratings vs Episodes")
lowessep = sm.nonparametric.lowess(npratings, npepisodes, frac=.5)

lowxep = list(zip(*lowessep))[0]
lowyep = list(zip(*lowessep))[1]

inter = interp1d(lowxep, lowyep, bounds_error=False)

plt.plot(npepisodes, npratings, "o")
plt.plot(lowx, lowy, "*")
plt.xlabel("Episodes")
plt.ylabel("Ratings")



plt.show()