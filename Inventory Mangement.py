
from datetime import datetime
from datetime import timedelta
from datetime import date

print("Welcome to Donavon's Grocery Store!")

itemdict = {0: {'desc':'Milk', 'stock':60, 'price':3.20, 'product_code':101, 'exp_date':'19/05/20'},
            1: {'desc':'Eggs', 'stock':20, 'price':2.50, 'product_code':105, 'exp_date':'21/05/21'},
            2: {'desc':'Apples', 'stock':22, 'price':5.50, 'product_code':106, 'exp_date':'23/05/20'},
            3: {'desc':'Coffee', 'stock':31, 'price':4.70, 'product_code':102, 'exp_date':'25/08/20'},
            4: {'desc':'Fish', 'stock':44, 'price':8.60, 'product_code':111, 'exp_date':'28/05/21'},
            5: {'desc':'Orange', 'stock':73, 'price':2.60, 'product_code':32, 'exp_date':'28/05/21'},
            6: {'desc':'Grapes', 'stock':52, 'price':2.30, 'product_code':43, 'exp_date':'28/05/21'},
            7: {'desc':'Pear', 'stock':176, 'price':1.60, 'product_code':12, 'exp_date':'28/05/21'},
            8: {'desc':'Durian', 'stock':99, 'price':10.90, 'product_code':48, 'exp_date':'28/05/21'},
            9: {'desc':'Mango', 'stock':84, 'price':4.20, 'product_code':84, 'exp_date':'28/05/21'},
            10: {'desc':'Rambutan', 'stock':49, 'price':1.30, 'product_code':121, 'exp_date':'28/05/21'}
            }


def addItem():
    pos = len(itemdict)
    itemdict[pos] = {}
    itemName = input("Enter the name of the item: ").lower()
    itemdict[pos]['desc'] = itemName
    while True:
        try:
            stock = int(input("Enter stock amount:"))
            itemdict[pos]['stock'] = stock
        except ValueError:
            print("Please enter a valid quantity.")
            continue
        break
    while True:
        try:
            price = float(input("Enter price amount:"))
            itemdict[pos]['price'] = price
        except ValueError:
            print("Please enter a valid price.")
            continue
        break
    while True:
        try:
            product_code = int(input("Enter product code:"))
            itemdict[pos]['product_code'] = product_code
        except ValueError:
            print("Please enter a valid product code.")
            continue
        break
    for i in itemdict:
        if itemdict[pos]['product_code'] in itemdict[i].values():
            print('Duplicate Product code!')
            itemdict.pop(pos)
            main()
        else:
            break
    while True:
        itemExpDate = input("Enter expiry date(dd/mm/yy): ")
        itemdict[pos]['exp_date'] = itemExpDate
        if len(itemExpDate) != 8:
            print("Please enter the correct date format!")
            continue
        break
    print("Successfully added item!")
    main()


def removeItem():
    while True:
        try:
            delKey = int(input('Please enter the item number to be removed:'))
            n = len(itemdict) - 1
            tmp = itemdict[delKey]
            itemdict[delKey] = itemdict[n]
            itemdict[n] = tmp
            print(itemdict[n])
            del itemdict[n]
            print("Successfully removed item!")
        except KeyError:
            print("Invalid item number!")
            continue
        except ValueError:
            print("Enter a number!")
            continue
        break
    main()

def displayItem():
    for itemNo in itemdict:
        print("=============\nItem No:", itemNo,
              "\ndesc:", itemdict[itemNo]['desc'],
              "\nstock:", itemdict[itemNo]['stock'],
              "\nprice: $%.2f" % itemdict[itemNo]['price'],
              "\nproduct_code:", itemdict[itemNo]['product_code'],
              "\nexp_date:", itemdict[itemNo]['exp_date'])
    main()


def optimizedBubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swap_status = False
        # Bubble the largest item to the end
        for itemNo in theSeq:
            try:
                if theSeq[itemNo]['stock'] > theSeq[itemNo + 1]['stock']:
                    # Swap the j and j+1 items
                    tmp = theSeq[itemNo]
                    theSeq[itemNo] = theSeq[itemNo + 1]
                    theSeq[itemNo + 1] = tmp
                    # Set boolean variable value if swapping occurred
                    swap_status = True
            except KeyError:
                break
        # Exit the loop if no swapping occurred
        # in the previous pass
        if swap_status == False:
            break


def sortByStock():
    optimizedBubbleSort(itemdict)
    for i in itemdict:
        print("---\nItem No:", i, itemdict[i]['desc'], 'Stock:', itemdict[i]['stock'])
    main()


def insertionSort(theSeq):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # Find the position where value fits in the ordered part of the list.
        pos = i
        while pos > 0 and value['price'] < theSeq[pos - 1]['price']:
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = value


def sortByPrice():
    insertionSort(itemdict)
    for i in itemdict:
        print("---\nItem No:", i, itemdict[i]['desc'], 'price: $%.2f' % itemdict[i]['price'])
    main()


def optimizedBubbleSortpdctcode(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swap_status = False
        # Bubble the largest item to the end
        for itemNo in theSeq:
            try:
                if theSeq[itemNo]['product_code'] > theSeq[itemNo + 1]['product_code']:
                    # Swap the j and j+1 items
                    tmp = theSeq[itemNo]
                    theSeq[itemNo] = theSeq[itemNo + 1]
                    theSeq[itemNo + 1] = tmp
                    # Set boolean variable value if swapping occurred
                    swap_status = True
            except KeyError:
                break
        # Exit the loop if no swapping occurred
        # in the previous pass
        if swap_status == False:
            break


def sortByProductCode():
    optimizedBubbleSortpdctcode(itemdict)
    return itemdict


def binarySearch(theValues, target):
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1
    # Repeatedly subdivide the sequence in half
    # until the target is found
    try:
        while low <= high:
            # Find the midpoint of the sequence
            mid = (high + low)//2
            # Does the midpoint contain the target?
            # If yes, return midpoint (i.e. index of the list)
            if theValues[mid]['product_code'] == target:
                print("Item found!", theValues[mid])
                return mid
            # Or is the target before the midpoint?
            elif target < theValues[mid]['product_code']:
                high = mid - 1
            # Or is the target after the midpoint?
            else:
                low = mid + 1
        # If the sequence cannot be subdivided further,
        # target is not in the list of values
        print("Item not found!")
    except KeyError:
        print('Invalid Product Code')


def findItem(value):
    sortByProductCode()
    binarySearch(itemdict, value)


def findProductCode():
    code = int(input("Enter product code you want to display:"))
    findItem(code)
    main()


def showAvgTotalStock():
    totalStock = 0
    noOfItem = len(itemdict)
    for itemNo in itemdict:
        totalStock += itemdict[itemNo]['stock']
    averageStock = (totalStock // noOfItem)
    print("Total number of stocks: %d\n"
          "Average number of stocks per item: %d stocks per %d items"% (totalStock, averageStock,noOfItem))
    main()


def runOutStock():
    option = input("Enter (1) for individual item or (2) for all items:")
    if option == '1':
        iPrdctNo = int(input("Enter the Product Code:"))
        amtSold = int(input("Enter number sold today:"))
        for i in itemdict:
            if itemdict[i]['product_code'] == iPrdctNo:
                stock = itemdict[i]['stock']
                print("Stock left:", stock)
                count = 0
                runOutStockRecFn(stock, amtSold, count)
    elif option == '2':
        amtSold = int(input("Enter average number sold today:"))
        for i in itemdict:
            print('---\nItem: ', itemdict[i]['desc'])
            stock = itemdict[i]['stock']
            print("Stock left:", stock)
            count = 0
            runOutStockRecFn(stock, amtSold, count)
    else:
        print("Invalid option!")
        runOutStock()
    main()


def runOutStockRecFn(stock, amtSold, count):
    if stock < amtSold:
        a = date.today() + timedelta(days=count)
        restockdate = a.strftime('%d/%m/%y')
        print('Stocks can last for', count, 'more days')
        print('Date to restock by:', restockdate)
    else:
        count += 1
        stock -= amtSold
        return runOutStockRecFn(stock, amtSold, count)


def main():
    firstchoice = input("=======================================================\n"
                            "Please select any of the following option to continue: \n"
                            "(1) Add items \n"
                            "(2) Remove items \n"
                            "(3) Display items \n"
                            "(4) Bubble sort item by [Stock] \n"
                            "(5) Insertion sort item by [Price] \n"
                            "(6) Binary search item by item [Product Code] \n"
                            "(7) Display Total and Average stock level \n"
                            "(8) Estimate item run-out date based on Today's sale \n"
                            "(0) Exit program(Enter Q/q to exit)\n"
                        "=======================================================\n").lower()
    if firstchoice == "1":
        addItem()
    elif firstchoice == "2":
        removeItem()
    elif firstchoice == "3":
        displayItem()
    elif firstchoice == "4":
        sortByStock()
    elif firstchoice == "5":
        sortByPrice()
    elif firstchoice == "6":
        findProductCode()
    elif firstchoice == "7":
        showAvgTotalStock()
    elif firstchoice == "8":
        runOutStock()
    elif firstchoice == "0":
        exit()
    elif firstchoice == "q":
        exit()
    else:
        print("Please enter a valid option!")
        main()


main()