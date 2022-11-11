#from base64 import encode
from itertools import permutations
import itertools

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

    #potential orders of elimination of candidates
    elimination_orders= []
    # Get permutations of n-1 candidates
    cand = list(candidates_and_votes.keys())
    perms_of_candidates = permutations(cand[0:no_of_cand-1])
    for i in perms_of_candidates:
        x = list(i)+[cand[-1]]
        elimination_orders.append(x)
    print(elimination_orders)

    #how many voters we have to play with
    coalition_size = 3

setup()


def check_order(candidates_and_votes ,ord, coalition_size, c_and_v, votes):
    cohort_size = 0
    for j in len(ord):
        for k in ord[j[0]:]:
            while int(k[1]) <= int(j[1]): #while votes for candidate k is leq votes for candidate j
                #votes_required = int(k[1])-int(j[1])+1
                if coalition_size > 0:#coalition_size>=votes_required
                    #k[1]+=votes_required
                    k[1] +=1
                    coalition_size -= 1
                    #coalition_size-=votes_required
                    cohort_size += 1
                    #cohort_size
                else:
                    print("Elimination order is impossible", elimination_orders)
                    return

        if j[0] < no_of_cand:
            c_and_v = redistribute(j, c_and_v, votes)
            coalition_size += cohort_size
    print("Successful Manipulation: ",ord)