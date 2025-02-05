
def determine_card(cards, query):
    cards.sort(reverse = True)
    print("The sorted array is ", cards)
    low = 0
    high = len(cards) - 1
    while low <= high:
        mid = low=(high-low)//2
        if cards[mid] == query:
            return True
        elif cards[mid] < query:
            high = mid +1
        elif cards[mid] > query:
            low = mid -1
        else :
            return False
#main
cards = [11,13,12,4,7,1,3,0,]
print("The Orignal array is: ", cards)
query = int(input("Which number do you want to find: "))
orignal_index = cards.index(query)
determine_card(cards,query)
if determine_card(cards,query) is True:
    print(f"Value found at index: {cards.index(query)} (After reverse sorting)")
    print(f"It's {query} orignal index before sorting was {orignal_index}")
else:
    print(f"Value not found in array")