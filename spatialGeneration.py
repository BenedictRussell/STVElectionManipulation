def returnRankings(C,V,GridSize=1000,NormallyDistributeAboutOrigin=True):
    import random
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.stats
    from itertools import permutations
    from math import factorial
    import csv
    import time
    def GenerateRandomPosition_NORMAL(GridSize):
        lower = -GridSize
        upper = GridSize
        mu,sigma = 0,GridSize/2
        Generator = scipy.stats.truncnorm((lower-mu)/sigma, (upper-mu)/sigma, loc=mu, scale=sigma)
        X,Y= Generator.rvs(2)
        return (X,Y)
    def GenerateRandomPosition_UNIFORM(GridSize):
        X = random.uniform(-GridSize,GridSize)
        Y = random.uniform(-GridSize,GridSize)
        return (X,Y)

    if NormallyDistributeAboutOrigin == True:
        CandLocs = np.array([GenerateRandomPosition_NORMAL(GridSize) for i in range(0,C)])
        VoterLocs = np.array([GenerateRandomPosition_NORMAL(GridSize) for i in range(0,V)])
    else:
        CandLocs = np.array([GenerateRandomPosition_UNIFORM(GridSize) for i in range(0,C)])
        VoterLocs = np.array([GenerateRandomPosition_UNIFORM(GridSize) for i in range(0,V)])
    Rankings = []
    for k in range(V):
        VoterDistancesToCandidates = [np.linalg.norm(VoterLocs[k]-CandLocs[c]) for c in range(C)]
        VoterRankings = scipy.stats.rankdata(VoterDistancesToCandidates)
        VoterCandidateOrder = {"C"+str(int(i+1)):int(VoterRankings[i]) for i in range(C)}#{"C"+str(int(i+1)):list(np.where(VoterRankings==i+1)[0])[0]+1 for i in range(C)}
        Rankings.append(VoterCandidateOrder)
    Candidates = ["C"+str(i) for i in range(1,C+1)]
    return Rankings, Candidates


    
