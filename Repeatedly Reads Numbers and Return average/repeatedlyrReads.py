def returnValues():
    mylist = []
    counter = 0
    while True:
        valueOfUser = input("Enter Your Number , if You want to exist Enter [Done]: ")

        if valueOfUser.lower() == "done":
            break
        if valueOfUser.isnumeric():
            valueOfUser = int(valueOfUser)
            mylist.append(valueOfUser)
            counter += 1
        else:
            print("You Enter inValid value")
            continue
    averageOfList = sum(mylist) / len(mylist)
    return mylist, counter, averageOfList


finalData = returnValues()
print(finalData)
