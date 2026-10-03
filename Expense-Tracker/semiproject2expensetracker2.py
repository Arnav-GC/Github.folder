name = input("hello, what is your name?: ")

listn = input("list name?: ")

items = {

}

prices = []

print("if you do not know the price of an item put 'idk'")

print("once you are out of items or list is done, put 'None' on item name")


item1 = input("item 1 name: ")
item1p = input("item 1 price: ")

item1 = item1.capitalize()
item1p = item1p.lower()
if item1p.isdigit():
    prices.append(int(item1p))
if item1 != "None":
    items[item1] = item1p

    item2 = input("item 2 name: ")
    item2p = input("item 2 price: ")
    item2 = item2.capitalize()
    item2p = item2p.lower()
    if item2p.isdigit():
        prices.append(int(item2p))
    if item2 != "None":
        items[item2] = item2p

        item3 = input("item 3 name: ")
        item3p = input("item 3 price: ")
        item3 = item3.capitalize()
        item3p = item3p.lower()
        if item3p.isdigit():
            prices.append(int(item3p))
        if item3 != "None":
            items[item3] = item3p

            item4 = input("item 4 name: ")
            item4p = input("item 4 price: ")
            item4 = item4.capitalize()
            item4p = item4p.lower()
            if item4p.isdigit():
                prices.append(int(item4p))
            if item4 != "None":
                items[item4] = item4p

                item5 = input("item 5 name: ")
                item5p = input("item 5 price: ")
                item5 = item5.capitalize()
                item5p = item5p.lower()
                if item5p.isdigit():
                    prices.append(int(item5p))
                if item5 != "None":
                    items[item5] = item5p

                    item6 = input("item 6 name: ")
                    item6p = input("item 6 price: ")
                    item6 = item6.capitalize()
                    item6p = item6p.lower()
                    if item6p.isdigit():
                        prices.append(int(item6p))
                    if item6 != "None":
                        items[item6] = item6p

                        item7 = input("item 7 name: ")
                        item7p = input("item 7 price: ")
                        item7 = item7.capitalize()
                        item7p = item7p.lower()
                        if item7p.isdigit():
                            prices.append(int(item7p))
                        if item7 != "None":
                            items[item7] = item7p

                            item8 = input("item 8 name: ")
                            item8p = input("item 8 price: ")
                            item8 = item8.capitalize()
                            item8p = item8p.lower()
                            if item8p.isdigit():
                                prices.append(int(item8p))
                            if item8 != "None":
                                items[item8] = item8p

                                item9 = input("item 9 name: ")
                                item9p = input("item 9 price: ")
                                item9 = item9.capitalize()
                                item9p = item9p.lower()
                                if item9p.isdigit():
                                    prices.append(int(item9p))
                                if item9 != "None":
                                    items[item9] = item9p

                                    item10 = input("item 10 name: ")
                                    item10p = input("item 10 price: ")
                                    item10 = item10.capitalize()
                                    item10p = item10p.lower()
                                    if item10p.isdigit():
                                        prices.append(int(item10p))
                                    if item10 != "None":
                                        items[item10] = item10p

                                        item11 = input("item 11 name: ")
                                        item11p = input("item 11 price: ")
                                        item11 = item11.capitalize()
                                        item11p = item11p.lower()
                                        if item11p.isdigit():
                                            prices.append(int(item11p))
                                        if item11 != "None":
                                            items[item11] = item11p

                                            item12 = input("item 12 name: ")
                                            item12p = input("item 12 price: ")
                                            item12 = item12.capitalize()
                                            item12p = item12p.lower()
                                            if item12p.isdigit():
                                                prices.append(int(item12p))
                                            if item12 != "None":
                                                items[item12] = item12p

                                                item13 = input("item 13 name: ")
                                                item13p = input("item 13 price: ")
                                                item13 = item13.capitalize()
                                                item13p = item13p.lower()
                                                if item13p.isdigit():
                                                    prices.append(int(item13p))
                                                if item13 != "None":
                                                    items[item13] = item13p

                                                    item14 = input("item 14 name: ")
                                                    item14p = input("item 14 price: ")
                                                    item14 = item14.capitalize()
                                                    item14p = item14p.lower()
                                                    if item14p.isdigit():
                                                        prices.append(int(item14p))
                                                    if item14 != "None":
                                                        items[item14] = item14p

                                                        item15 = input("item 15 name: ")
                                                        item15p = input("item 15 price: ")
                                                        item15 = item15.capitalize()
                                                        item15p = item15p.lower()
                                                        if item15p.isdigit():
                                                            prices.append(int(item15p))
                                                        if item15 != "None":
                                                            items[item15] = item15p


print("no of items in your grocery list :", len(items))
total = sum(prices)
print("total: ", total)


if item1p == "idk":
    print("you do not know the price of,", item1, ". Hence it was not added to total")

if item2p == "idk":
    print("you do not know the price of,", item2, ". Hence it was not added to total")

if item3p == "idk":
    print("you do not know the price of,", item3, ". Hence it was not added to total")

if item4p == "idk":
    print("you do not know the price of,", item4, ". Hence it was not added to total")

if item5p == "idk":
    print("you do not know the price of,", item5, ". Hence it was not added to total")

if item6p == "idk":
    print("you do not know the price of,", item6, ". Hence it was not added to total")

if item7p == "idk":
    print("you do not know the price of,", item7, ". Hence it was not added to total")

if item8p == "idk":
    print("you do not know the price of,", item8, ". Hence it was not added to total")

if item9p == "idk":
    print("you do not know the price of,", item9, ". Hence it was not added to total")

if item10p == "idk":
    print("you do not know the price of,", item10, ". Hence it was not added to total")

if item11p == "idk":
    print("you do not know the price of,", item11, ". Hence it was not added to total")

if item12p == "idk":
    print("you do not know the price of,", item12, ". Hence it was not added to total")

if item13p == "idk":
    print("you do not know the price of,", item13, ". Hence it was not added to total")

if item14p == "idk":
    print("you do not know the price of,", item14, ". Hence it was not added to total")

if item15p == "idk":
    print("you do not know the price of,", item15, ". Hence it was not added to total")


if item1 != "None":
    print(items[item1])

if item2 != "None":
    print(items[item2])

if item3 != "None":
    print(items[item3])

if item4 != "None":
    print(items[item4])

if item5 != "None":
    print(items[item5])

if item6 != "None":
    print(items[item6])

if item7 != "None":
    print(items[item7])

if item8 != "None":
    print(items[item8])

if item9 != "None":
    print(items[item9])

if item10 != "None":
    print(items[item10])

if item11 != "None":
    print(items[item11])

if item12 != "None":
    print(items[item12])

if item13 != "None":
    print(items[item13])

if item14 != "None":
    print(items[item14])

if item15 != "None":
    print(items[item15])