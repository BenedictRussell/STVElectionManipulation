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

    candidates_and_votes = tally_votes(voting_array, no_of_cand)

    #potential orders of elimination of candidates
    elimination_orders= []
    # Get permutations of n-1 candidates
    cand = list(candidates_and_votes.keys())
    perms_of_candidates = permutations(cand[0:no_of_cand-1])
    for i in perms_of_candidates:
        x = list(i)+[cand[-1]]
        elimination_orders.append(x)

    #how many voters we have to play with
    coalition_size = 3
    return candidates_and_votes, elimination_orders, voting_array


def tally_votes(voting_array, no_of_cand):
    #the candidates and the number of 1st choice votes they have
    candidates_and_votes = {}

    for i in range(65,65+no_of_cand):
        candidates_and_votes[str(chr(i))] = 0
    
    #add each voter's current 1st choice to the voting_array
    for voter in voting_array:
        for key in voter:
            if voter[key]==1:
                candidates_and_votes[key]+=1
    return(candidates_and_votes)

def check_order(candidates_and_votes ,ord, coalition_size, voting_array):
    cohort_size = 0
    count = 1
    variable_votes = dict(candidates_and_votes)
    for i in ord:
        for j in ord[ord.index(i)+1:]:
            votes_req = int(variable_votes[i]) - int(variable_votes[j]) + 1 #while votes for candidate k is leq votes for candidate j
                #votes_required = int(k[1])-int(j[1])+1
            if coalition_size >= votes_req: #coalition_size>=votes_required
                #k[1]+=votes_required
                variable_votes[j] += votes_req
                coalition_size -= votes_req
                #coalition_size-=votes_required
                cohort_size += votes_req
                #cohort_size
            else:
                print("Elimination order is impossible", ord)
                return
        if count < len(ord): #no point in doing the very last step of redistrbuting
            for en, voter in enumerate(voting_array):
                if voter[i] == 1:
                    voting_array[en] = {key: voter[key]-1 for key in voter}
                else:
                    voter[i] = 0
            coalition_size += cohort_size
            count +=1

    print("Successful Manipulation: ", ord)

candidates_and_votes, elimination_orders, voting_array = setup()
coalition_size = 3
for order in elimination_orders:
    check_order(candidates_and_votes, order, coalition_size, voting_array)