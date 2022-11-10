#from base64 import encode
from itertools import permutations

def setup():
    """setup()
    Takes the number of candidates, current voter rankings and coalition size.
    Creates a dictionary with the current votes for each candidate, and a list
    of potential elimination orders."""

    #no_of_cand = 4
    #voting_array = [[1,4,2,3],[4,2,1,3],[1,4,3,2],[3,2,4,1],[2,3,4,1]]
    no_of_cand = 3

    #list of ordered votes that we already know about
    voter1 = {"A":2, "B": 1, "C": 3}
    voter2 = {"A":1, "B": 2, "C": 3}
    voter3 = {"A":1, "B": 2, "C": 3}
    voting_array = [voter1,voter2,voter3]

    #the candidates and the number of 1st choice votes they have
    candidates_and_votes = {}

    for i in range(65,65+no_of_cand):
        candidates_and_votes[str(chr(i))]=0
    
    #add each voter's current 1st choice to the voting_array
    for voter in voting_array:
        for key in voter:
            if voter[key]==1:
                candidates_and_votes[key]+=1
    print(candidates_and_votes)


    print(candidates_and_votes)

    #potential orders of elimination of candidates
    elimination_orders= []

    #how many voters we have to play with
    coalition_size = 4

setup()
