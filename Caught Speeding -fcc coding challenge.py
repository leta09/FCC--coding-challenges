
def speeding(speeds, limit):

    over_limit = [speed - limit for speed in speeds if speed > limit]
  
    len_over_limit = len(over_limit)

    if len_over_limit == 0:
        return [0, 0]
    
    return [len_over_limit, sum(over_limit)/len_over_limit]



print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([50, 60, 55], 60))
print(speeding([58, 50, 60, 55], 55))


