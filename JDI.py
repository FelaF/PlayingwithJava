List = [77, 11, 11, 22, 33, 77, 44, 55, 66, 88, 88, 88]
"""
Number = 88
Count = 0

for each in List:
    if Number == each:
        Count += 1
        print(f"{Number} is in the list {Count - 1} times")
if Number not in List and Count == 0:
        print(f"the number {Number} is not in the List")
"""

"""MY CODE TRY 1"""

SecondList = [100, 10, 55, 92, 33, 45, 66, 99, 11, 23, 44, 45, 45 ,45, 45, 45,]
"""Countings = SecondList.count(45)
print(Countings) Testing Count Method"""

def Countings(Listing: list, SearchValue: int) -> (__name__):
    FoundTimes = Listing.count(SearchValue)
    return (F"""The List {Listing} contains the value {SearchValue} {FoundTimes} times""")

X = Countings(SecondList, 45)
print(X)