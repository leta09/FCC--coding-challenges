
def array_diff(arr1, arr2):

    r1 = set(arr1).difference(set(arr2))
    r2 = set(arr2).difference(set(arr1))
    return sorted(list(r1) + list(r2))




print(array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]))

print(array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]))


