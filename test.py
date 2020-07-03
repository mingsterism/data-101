def checkIfEven( number ):
    if number % 2 == 0:
        return True
    else:
        return False

def main(x):
    for count in range(x):
        if checkIfEven(count) == True:
            print("Number", count, "is even", checkIfEven(count))

print(checkIfEven(10))
print("Number 101 Even status is: ", checkIfEven(101))
main(1000)


