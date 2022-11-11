#from base64 import encode
from itertools import permutations

#no_of_cand = 4
#voting_array = [[1,4,2,3],[4,2,1,3],[1,4,3,2],[3,2,4,1],[2,3,4,1]]
no_of_cand = 3
voting_array = [[2,1,3,4,5,5,6],[1,2,3,4],[1,3,2,4,5]]
candidates_and_votes = []
elimination_orders= []
coalition_size = 4

for i in range(1,no_of_cand+1):
    candidates_and_votes.append([i,0])

# Get permutations of n-1 candidates
perms_of_candidates = permutations(candidates_and_votes[0:no_of_cand-1])
for i in perms_of_candidates:
   x = list(i)+[candidates_and_votes[-1]]
   elimination_orders.append(x)
#print(elimination_orders)

def TallyVotes(c_and_v, votes):
    for i in c_and_v:
        for j in votes:
            if i[0] == j[0]:
                i[1] += 1
    return c_and_v

def redistribute(cand_for_elimination_and_votes, c_and_v, votes):
    for v in votes:
        v.remove(cand_for_elimination_and_votes[0])
    del c_and_v[0]#deleting the bottom ranked candidate (aka, cand_for_elimination)
    new_c_and_v = TallyVotes(c_and_v, votes)
    return new_c_and_v

def check_order(ord, coalition_size, c_and_v, votes):
    print(ord)
    tallied_c_and_v = TallyVotes(c_and_v, votes)
    cohort_size = 0
    for j in len(ord):
        for k in ord[j[0]:]:
            while int(k[1]) <= int(j[1]):#while votes for candidate k is leq votes for candidate j
                #votes_required = int(k[1])-int(j[1])+1
                if coalition_size > 0:#coalition_size>=votes_required
                    #k[1]+=votes_required
                    k[1] +=1
                    coalition_size -= 1
                    #coalition_size-=votes_required
                    cohort_size += 1
                    #cohort_size
                else:
                    print("Elimination order is impossible",elimination_orders)
                    return

        if j[0] < no_of_cand:
            c_and_v = redistribute(j, c_and_v, votes)
            coalition_size += cohort_size
    print("Successful Manipulation: ",ord)
    

for x in elimination_orders:
    print("swe",elimination_orders)
    check_order(x, coalition_size, candidates_and_votes, voting_array)