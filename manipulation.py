def returnMRRate(votes,C,K):
    import itertools
    from itertools import permutations
    def setup(Rankings,Candidates):
        """setup()
        Takes the number of candidates, current voter rankings and coalition size.
        Creates a dictionary with the current votes for each candidate, and a list
        of potential elimination orders."""

        voting_array = Rankings
        candidates  = Candidates

        candidates_and_votes = tally_votes(voting_array, candidates)

        # potential orders of elimination of candidates
        elimination_orders= []
        # Get permutattions of n-1 candidates
        cand = list(candidates_and_votes.keys())
        perms_of_candidates = permutations(cand[0:len(cand)-1])
        for i in perms_of_candidates:
            x = list(i)+[cand[-1]]
            elimination_orders.append(x)
        no_ords = len(elimination_orders)
        #print("orders: ",elimination_orders)
        #print(candidates_and_votes,voting_array)
        return candidates_and_votes, elimination_orders, voting_array, no_ords
    def tally_votes(v_array, candidates):
        # the candidates and the number of 1st choice votes they have
        candidates_and_votes = {candidates[i]:0 for i in range(0,len(candidates))}
        #print(candidates_and_votes)
        
        # add each voter's current 1st choice to the voting_array
        #print(voting_array)
        for voter in v_array:
            #print(voter)
            for key in voter:
                if voter[key]==1:
                    candidates_and_votes[key]+=1
        return(candidates_and_votes)
    def remove_orders(unsuccesful_start):
        elimination_orders_remove = []
        k = len(unsuccesful_start) 
        copy = yy.copy()
        for i in copy:
            if i[0:k] == unsuccesful_start:
                yy.remove(i)
    def check_order(candidates_and_votes, order, coalition_size, voting_array, candidates):
        voting_array_c = voting_array.copy()
        #print("HERE",candidates_and_votes)
        coalition_votes = []
        coalition_store = []
        dic__coalition_votes= []
        eliminated_candidates = []
        candidates_remaining = candidates.copy()
        for i in range(0,coalition_size):
            coalition_votes.append([])
        count = 1
        # copy of candidates and votes
        variable_votes = dict(candidates_and_votes)
        for i in order:
            eliminated_candidates.append(i)
            for j in order[order.index(i)+1:]:
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
                        remove_orders(yy)
                        print("Elimination order is impossible", order)
                        return 0,0,0
                        #return [], ord
            candidates_remaining.remove(i)
            if count <= len(order): # no point in doing the very last step of redistrbuting
                for en, voter in enumerate(voting_array_c):
                    # Changes any first preference votes to the next available candidate in their preference order
                    if voter[i] == 1:
                        voting_array_c[en] = {key: voter[key]-1 for key in voter}
            
                    else:
                        # Eliminate candidate i from everyone elses list   
                        voting_array_c[en][i]=0                            
                        for key, value in voter.items():
                            """
                            print("i:",i," ",type(i),"\n",
                                  "voter:",voter," ",type(voter),
                                  "key:",key," ",type(key),"\n",
                                  "value:",value, " ", type(key))"""
                            if int(value) > int(voter[i]):
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
            
            back_ord = order[::-1]
            #print("BACK ORD:",back_ord)
            dif = list(sorted(set(back_ord) - set(v), key=order.index))
            #print("V:",v)
            v += dif[::-1]
            #print("V+dif:",v)
            #print("NEW DICT:",{key: value+1 for value, key in enumerate(v)})
            dic__coalition_votes.append({key: value+1 for value, key in enumerate(v)})
        return dic__coalition_votes, order, 1
    
    successful_manipulations = 0
    y,yy,yyy,yyyy = setup(votes,C)
    for i in yy:
        a,b,c = check_order(y, i, K, yyy, C)
        print(successful_manipulations)
        successful_manipulations += c
    
    return successful_manipulations/yyyy
