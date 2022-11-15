from itertools import permutations

def setup():
    """setup()
    Takes the number of candidates, current voter rankings and coalition size.
    Creates a dictionary with the current votes for each candidate, and a list
    of potential elimination orders."""
    no_of_cand = 4

    # list of ordered votes that we already know about
    voter1 = {"A":2, "B": 1, "C": 3, "D": 4}
    voter2 = {"A":2, "B": 1, "C": 2, "D": 3}
    voter3 = {"A":1, "B": 2, "C": 3, "D": 3}
    voting_array = [voter1,voter2,voter3]

    candidates_and_votes = tally_votes(voting_array, no_of_cand)

    # potential orders of elimination of candidates
    elimination_orders= []
    # Get permutations of n-1 candidates
    cand = list(candidates_and_votes.keys())
    perms_of_candidates = permutations(cand[0:no_of_cand-1])
    for i in perms_of_candidates:
        x = list(i)+[cand[-1]]
        elimination_orders.append(x)

    # how many voters we have to play with
    coalition_size = 3
    coalition = []
    for i in range(0,coalition_size):
        coalition.append([])
    print(coalition)
    return candidates_and_votes, elimination_orders, voting_array


def tally_votes(voting_array, no_of_cand):
    # the candidates and the number of 1st choice votes they have
    candidates_and_votes = {}

    for i in range(65,65+no_of_cand):
        candidates_and_votes[str(chr(i))] = 0
    
    # add each voter's current 1st choice to the voting_array
    for voter in voting_array:
        for key in voter:
            if voter[key]==1:
                candidates_and_votes[key]+=1
    return(candidates_and_votes)

def check_order(candidates_and_votes ,ord, coalition_size, voting_array):
    coalition_votes = []
    for i in range(0,coalition_size):
        coalition_votes.append([])
    coalition_current_votes = {"A":0, "B": 0, "C": 0, "D": 0}
    count = 1
    # copy of candidates and votes
    variable_votes = dict(candidates_and_votes)
    for i in ord:
        for j in ord[ord.index(i)+1:]:
            # compute votes required for j to beat i
            votes_req = int(variable_votes[i]) - int(variable_votes[j]) + 1
            # check that difference is positive
            if votes_req > 0:
                if coalition_size >= votes_req: # check if coalition size >= votes required to make j beat i
                    variable_votes[j] += votes_req
                    # decrease the amount of votes we can maniplulate this round
                    coalition_size -= votes_req
                    for c in range(0,votes_req):
                        coalition_votes[c]
                    # tally
                    coalition_current_votes[j] +=votes_req

                else:
                    # coalition was too small
                    print("Elimination order is impossible", ord)
                    return
        if count < len(ord): # no point in doing the very last step of redistrbuting
            for en, voter in enumerate(voting_array):
                # Changes any first preference votes to the next available candidate in their preference order
                if voter[i] == 1:
                    voting_array[en] = {key: voter[key]-1 for key in voter}
                else:
                    # Eliminate candidate i from everyone elses list
                    voter[i] = 0
            # voters in coalitions next spot available to be filled
            coalition_size += coalition_current_votes[i]
            count +=1
    print(coalition_current_votes)
    print("Successful Manipulation: ", ord)

candidates_and_votes, elimination_orders, voting_array = setup()
coalition_size = 4
for order in elimination_orders:
    check_order(candidates_and_votes, order, coalition_size, voting_array)