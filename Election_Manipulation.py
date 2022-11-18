from itertools import permutations
import itertools

def setup():
    """setup()
    Takes the number of candidates, current voter rankings and coalition size.
    Creates a dictionary with the current votes for each candidate, and a list
    of potential elimination orders."""
    no_of_cand = 4

    # list of ordered votes that we already know about
    voter1 = {"A":1, "B": 2, "C": 3, "D": 4}
    voter2 = {"A":3, "B": 1, "C": 2, "D": 4}
    voter3 = {"A":1, "B": 2, "C": 3, "D": 4}
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


def tally_votes(v_array, no_of_cand):
    # the candidates and the number of 1st choice votes they have
    candidates_and_votes = {}

    for i in range(65,65+no_of_cand):
        candidates_and_votes[str(chr(i))] = 0
    
    # add each voter's current 1st choice to the voting_array
    #print(voting_array)
    for voter in v_array:
        for key in voter:
            if voter[key]==1:
                candidates_and_votes[key]+=1
    return(candidates_and_votes)

def remove_orders(unsuccesful_start):
    elimination_orders_remove = []
    k = len(unsuccesful_start) 
    copy = elimination_orders.copy()
    for i in copy:
        if i[0:k] == unsuccesful_start:
            elimination_orders.remove(i)

def check_order(candidates_and_votes ,ord, coalition_size, voting_array):
    voting_array_c = voting_array.copy()
    coalition_votes = []
    coalition_store = []
    dic__coalition_votes= []
    eliminated_candidates = []
    candidates_remaining = ["A", "B", "C", "D"]
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
                    remove_orders(eliminated_candidates)
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
                    voting_array_c[en][i]=0                            
                    for key, value in voter.items():
                        if value > voter[i]:
                            voting_array_c[en][key] += -1
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
        v += dif
        dic__coalition_votes.append({key: value+1 for value, key in enumerate(v)})
    return dic__coalition_votes, ord

def check_manipulation(votes_set, no_cand):
    k = no_cand
    all_votes = votes_set
    # loop over number of eliminations (n-1 candidates)
    for i in range(0,no_cand-1):
        c_and_v = tally_votes(all_votes, k)
        # needs changing to elimate all candidates with votes = 0 / minimum, and change to while loop (while not just one candidate left with none-zero votes - what if tie?)
        if i == 0:
            elim_cand = min(c_and_v, key=c_and_v.get)#get candidate with least 1st choice votess
        else:
            elim_cand = min(x for x in c_and_v if  c_and_v[x] != 0)

        for en, vote_dict in enumerate(all_votes):
            # Changes any first preference votes to the next available candidate in their preference order
            if vote_dict[elim_cand] == 1:
                all_votes[en] = {key: vote_dict[key]-1 for key in vote_dict}
            else:
                # Eliminate candidate i from everyone elses list
                all_votes[en][elim_cand] = 0
                for key, value in vote_dict.items():
                    if value > vote_dict[elim_cand]:
                        all_votes[en][key] += -1
                  
    c_and_v = tally_votes(all_votes, k)
    #print(c_and_v,"\n")

    return (max(c_and_v, key=c_and_v.get))


#coalition_array = []
candidates_and_votes, elimination_orders, voting_array = setup()
coalition_size = 4

for order in elimination_orders:
    #print(order)
    a,b = check_order(candidates_and_votes, order, coalition_size, voting_array)
    #coalition_array.append([a,b])
    if b != "fail":
        y, yy, yyy = setup()
        check_votes = yyy + a
        #print(check_votes)
        winner = check_manipulation(check_votes,4)
        print(b, winner)