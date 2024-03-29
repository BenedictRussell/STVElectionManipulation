from itertools import permutations
import itertools

def setup():
    """setup()
    Takes the number of candidates, current voter rankings and coalition size.
    Creates a dictionary with the current votes for each candidate, and a list
    of potential elimination orders."""
    no_of_cand = 5

    # list of ordered votes that we already know about
    voter1 = {"A":2, "B": 4, "C": 3, "D": 1, "E": 5}
    voter2 = {"A":3, "B": 5, "C": 2, "D": 4, "E": 1}
    voter3 = {"A":1, "B": 2, "C": 3, "D": 5, "E": 4}
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

    return candidates_and_votes, elimination_orders, voting_array


def tally_votes(voting_array, no_of_cand):
    # the candidates and the number of 1st choice votes they have
    candidates_and_votes = {}

    for i in range(65,65+no_of_cand):
        candidates_and_votes[str(chr(i))] = 0
    
    # add each voter's current 1st choice to the voting_array
    #print(voting_array)
    for voter in voting_array:
        for key in voter:
            if voter[key]==1:
                candidates_and_votes[key]+=1
    return(candidates_and_votes)


def check_order(candidates_and_votes ,ord, coalition_size, voting_array):
    voting_array_c = voting_array
    coalition_votes = []
    coalition_store = []
    eliminated_candidates = []
    dic__coalition_votes= []
    candidates_remaining = ["A", "B", "C", "D", "E"]
    for i in range(0,coalition_size):
        coalition_votes.append([])
    count = 1
    # copy of candidates and votes
    variable_votes = dict(candidates_and_votes)
    for i in ord:
        eliminated_candidates.append(i)
        for j in ord[ord.index(i)+1:]:
            # compute votes required for j to beat i
            votes_req = int(variable_votes[i]) - int(variable_votes[j]) + 1
            # check that difference is positive
            if votes_req > 0:
                if len(coalition_votes) >= votes_req: # check if coalition size >= votes required to make j beat i
                    variable_votes[j] += votes_req
                    # decrease the amount of votes we can maniplulate this round
                    for c in range(0,votes_req):
                        coalition_votes[0].append(j)
                        coalition_store.append(coalition_votes[0])
                        coalition_votes.remove(coalition_votes[0])

                else:
                    # coalition was too small

                    # CALL funtion which removes orders from elimination orders which dont work.
                    
                    print("Elimination order is impossible", ord)
                    return "fail", "fail"
                    #return [], ord
        candidates_remaining.remove(i)
        if count <= len(ord): # no point in doing the very last step of redistrbuting
            for en, voter in enumerate(voting_array_c):
                # Changes any first preference votes to the next available candidate in their preference order
                if voter[i] == 1:
                    voting_array_c[en] = {key: voter[key]-1 for key in voter}
        
                else:
                   # Eliminate candidate i from everyone elses list
                    for key, value in vote_dict.items():
                    if value > vote_dict[elim_cand]:
                        all_votes[en][key] += -1
            count +=1
        #print(coalition_store)
        for b in coalition_store:
            if list(set(b).intersection(set(candidates_remaining))) == []:
                coalition_votes.insert(0,b)
                coalition_store.remove(b)
            # voters in coalitions next spot available to be filled
            
            
    coalition_votes += coalition_store
    #print("Successful Manipulation: ", ord)
    
    for v in coalition_votes:
        back_ord = ord[::-1]
        dif = list(sorted(set(back_ord) - set(v), key=ord.index))
        for f in dif:
            v.append(f)
        dic__coalition_votes.append({"A":v.index("A")+1, "B": v.index("B")+1, "C": v.index("C")+1, "D": v.index("D")+1,"E": v.index("E")+1})

    return dic__coalition_votes, ord

#coalition_array = []
candidates_and_votes, elimination_orders, voting_array = setup()
coalition_size = 5

for order in elimination_orders:
    a,b = check_order(candidates_and_votes, order, coalition_size, voting_array)
    if b!= "fail":
        print(b)