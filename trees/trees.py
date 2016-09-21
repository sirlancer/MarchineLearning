from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob*log(prob,2)
	return shannonEnt

def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reduceFeatVec =featVec[:axis]
			reduceFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reduceFeatVec)
	return retDataSet

def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	labels = ['no surfacing','flippers']
	return dataSet,labels

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	print "the base entropy is %d" % (baseEntropy)
	bestInfoGain = 0.0;
	bestFeature = -1;
	for i in range(numFeatures):
		featureList = [example[i] for example in dataSet]
		uniqueVals = set(featureList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet,i,value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy +=prob*calcShannonEnt(subDataSet)
		infoGain = baseEntropy-newEntropy
		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature