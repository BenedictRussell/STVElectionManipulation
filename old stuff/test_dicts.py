diction = {"A":5, "B": 6}

listion = [diction]

for listy in listion:
    listy = {key: listy[key]-1 for key in listy}
print(listion)