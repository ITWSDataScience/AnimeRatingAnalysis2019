import matplotlib.pyplot as plt
import random
import numpy as np
import csv

from matplotlib.pyplot import figure

anime = {}

minEp = float('inf')
maxEp = 0
minRat = float('inf')
maxRat = 0

numEpisodesArr = []
avgRatingsArr = []
everythingArr = []

with open('anime.csv', encoding="utf-8") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:

		if line_count % 1000 == 0:
			print(line_count)


		#if line_count == 1000:
		#	break

		if line_count == 0:
			line_count += 1
			continue
		else:
			line_count += 1
			aType = row[3]
			if aType == "Movie" or aType == "Hentai":
				continue

			animeID = row[0]
			numEpisodes = row[4]
			avgRatings = row[5]

			if numEpisodes == "Unknown":
				continue

			try:
				float(avgRatings)
			except ValueError:
				print("Not a float")
				continue

			try:
				int(numEpisodes)
			except ValueError:
				print("Not an int")
				continue

			if float(avgRatings) < minRat:
				minRat = float(avgRatings)
			if float(avgRatings) > maxRat:
				maxRat = float(avgRatings)

			if int(numEpisodes) < minEp:
				minEp = int(numEpisodes)
			if int(numEpisodes) > maxEp:
				maxEp = int(numEpisodes)

			if (int(numEpisodes) > 300):
				continue

			#plt.plot([numEpisodes], [avgRatings], marker='o', markersize=3, color="black")
			numEpisodesArr.append(int(numEpisodes))
			avgRatingsArr.append(float(avgRatings))
			everythingArr.append([int(numEpisodes), float(avgRatings)])


print(max(numEpisodesArr))
	
numEpisodesArr = np.array(numEpisodesArr)
avgRatingsArr = np.array(avgRatingsArr)

everythingArr = np.array(everythingArr)

x, y = everythingArr.T

figure(figsize=(12, 6))

plt.scatter(numEpisodesArr, avgRatingsArr, 3, c="b")

print(max(numEpisodesArr))
print(max(avgRatingsArr))

#plt.plot(everythingArr, marker='o', markersize=3, color="black")

plt.xlabel("Number of Episodes")
plt.ylabel("Ratings")
#plt.xticks(np.arange(maxEp, minEp, 50))
#plt.yticks(np.arange(minRat, maxRat, 1))

#plt.xticks([])
#plt.yticks([])

plt.xticks(np.arange(min(numEpisodesArr),max(numEpisodesArr),25))
plt.yticks(np.arange(min(avgRatingsArr), max(avgRatingsArr), 1))

#figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.show()


##########################################################################################################################

episodesCounts = {}
totalRatings = {}

with open('anime.csv', encoding="utf-8") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:

		if line_count % 1000 == 0:
			print(line_count)


		#if line_count == 1000:
		#	break

		if line_count == 0:
			line_count += 1
			continue
		else:
			line_count += 1
			aType = row[3]
			if aType == "Movie" or aType == "Hentai":
				continue

			animeID = row[0]
			numEpisodes = row[4]
			avgRatings = row[5]

			if numEpisodes == "Unknown":
				continue

			try:
				float(avgRatings)
			except ValueError:
				print("Not a float")
				continue

			try:
				int(numEpisodes)
			except ValueError:
				print("Not an int")
				continue

			#plt.plot([numEpisodes], [avgRatings], marker='o', markersize=3, color="black")

			'''
			numEpisodesArr.append(int(numEpisodes))
			avgRatingsArr.append(float(avgRatings))
			everythingArr.append([int(numEpisodes), float(avgRatings)])
			'''

			if (int(numEpisodes) > 300):
				continue

			if int(numEpisodes) in episodesCounts:
				episodesCounts[int(numEpisodes)] += 1
				totalRatings[int(numEpisodes)] += float(avgRatings)
			else:
				episodesCounts[int(numEpisodes)] = 1
				totalRatings[int(numEpisodes)] = float(avgRatings)


'''
print(max(numEpisodesArr))
	
numEpisodesArr = np.array(numEpisodesArr)
avgRatingsArr = np.array(avgRatingsArr)

everythingArr = np.array(everythingArr)

x, y = everythingArr.T
'''

numEpisodesArr = []
avgRatingsArr = []

for i in totalRatings.keys():
	numEpisodesArr.append(i)
	avgRatingsArr.append(totalRatings[i]/episodesCounts[i])

bucketEpisodeArr = []
bucketAvgRatingArr = []

newAvg = 0
newCount = 0

for i in range(300):

	if i in totalRatings.keys():
		toAdd = totalRatings[i]/episodesCounts[i]
	else:
		#continue
		if i % 10 == 0:
			newAvg = newAvg/10

			bucketAvgRatingArr.append(newAvg)
			bucketEpisodeArr.append(i-5)

			newAvg = 0
			newCount = 0
			continue

	newAvg += toAdd
	newCount += 1

	if i % 10 == 0:
		newAvg = newAvg/10

		bucketAvgRatingArr.append(newAvg)
		bucketEpisodeArr.append(i-5)

		newAvg = 0
		newCount = 0
	
	'''
	newAvg += numEpisodesArr[i]
	newAvg += numEpisodesArr[i+1]
	newAvg += numEpisodesArr[i+2]
	newAvg += numEpisodesArr[i+3]
	newAvg += numEpisodesArr[i+4]
	newAvg += numEpisodesArr[i+5]
	newAvg += numEpisodesArr[i+6]
	newAvg += numEpisodesArr[i+7]
	newAvg += numEpisodesArr[i+8]
	newAvg += numEpisodesArr[i+9]
	

	newAvg = newAvg/10

	bucketAvgRatingArr.append(newAvg)
	bucketEpisodeArr.append(i)
	'''

newAvg = newAvg/newCount

bucketAvgRatingArr.append(newAvg)
bucketEpisodeArr.append(len(numEpisodesArr) - newCount)

print(bucketAvgRatingArr)

newAvg = 0
newCount = 0

figure(figsize=(12, 6))

plt.bar(bucketEpisodeArr, bucketAvgRatingArr, width=(.8*12))

numBins = int(len(numEpisodesArr)/10)

#plt.hist(bucketAvgRatingArr, bins=numBins)
#plt.scatter(numEpisodesArr, avgRatingsArr, 3, c="b")

print(max(numEpisodesArr))
print(max(avgRatingsArr))

#plt.plot(everythingArr, marker='o', markersize=3, color="black")

plt.xlabel("Number of Episodes")
plt.ylabel("Average Rating")
#plt.xticks(np.arange(maxEp, minEp, 50))
#plt.yticks(np.arange(minRat, maxRat, 1))

#plt.xticks([])
#plt.yticks([])

#plt.xticks(np.arange(min(numEpisodesArr),max(numEpisodesArr),25))
plt.yticks(np.arange(min(bucketAvgRatingArr), max(bucketAvgRatingArr), 1))

#figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.show()

