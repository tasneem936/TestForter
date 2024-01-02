import csv


def load_nicknames_from_csv(csv_file):
    nickname_mapping = {}
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            nicknames = row[1:]
            nickname_mapping[name] = set([name] + nicknames)
    return nickname_mapping


def are_names_similar(name1, name2):
    # Check if names have the same length
    if len(name1) != len(name2):
        return False

    # Count the number of differing characters
    differing_chars = sum(c1 != c2 for c1, c2 in zip(name1, name2))

    # Check if only one character is different
    return differing_chars == 1


def is_nickname(nickname, first_name, nickname_mapping):
    # Check if the first name is a nickname of the other name based on the mapping
    return first_name in [n.split()[0] for n in nickname_mapping.get(nickname, set())]


def countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv):

    # Extract only the first name and last name from billNameOnCard
    cardFirst = billNameOnCard.split()[0] if ' ' in billNameOnCard else billNameOnCard
    cardLast = billNameOnCard.split()[1] if ' ' in billNameOnCard else billNameOnCard

    # Extract only the first name and last name from billing and shipping addresses
    billFirst = billFirstName.split()[0] if ' ' in billFirstName else billFirstName
    billLast = billLastName

    shipFirst = shipFirstName.split()[0] if ' ' in shipFirstName else shipFirstName
    shipLast = shipLastName

    # Combine billing first name and last name
    fullBillName = billFirst + ' ' + billLast

    # Combine shipping first name and last name
    fullShipName = shipFirst + ' ' + shipLast

    # Combine Reverse shipping first name and last name
    rev_fullShipName = shipLast + ' ' + shipFirst

    # Combine Reverse card first name and last name
    rev_fullCardName = cardLast + ' ' + cardFirst

    # Load nicknames from the CSV file
    nickname_mapping = load_nicknames_from_csv(nickname_csv)

    # Assume that there are 3 different names as a default
    count = 3

    # base cases
    if billNameOnCard == fullBillName and billNameOnCard == fullShipName:
        return 1
    if rev_fullCardName == fullBillName and fullShipName == fullBillName:
        return 1
    if rev_fullShipName == fullBillName and billNameOnCard == fullBillName:
        return 1
    if rev_fullShipName == fullBillName and rev_fullCardName == fullBillName:
        return 1

    #################
    if are_names_similar(billFirst, cardFirst) or are_names_similar(billLast, cardLast) \
            or is_nickname(billFirst, cardFirst, nickname_mapping) \
            or (billFirst == cardLast and billLast):
        count = count - 1

    if are_names_similar(billFirst, shipFirst) or are_names_similar(billLast, shipLast) \
            or is_nickname(billFirst, shipFirst, nickname_mapping):
        count = count - 1

    # check if the name on card was reversed
    if (are_names_similar(billFirst, cardLast) and are_names_similar(billLast, cardFirst)) \
            or (are_names_similar(billFirst, cardLast) and is_nickname(billLast, cardFirst, nickname_mapping)):
        count = count - 1

    # check if the name on ship address was reversed
    if (are_names_similar(billFirst, shipLast) and are_names_similar(billLast, shipFirst)) \
            or (are_names_similar(billFirst, shipLast) and is_nickname(billLast, shipLast, nickname_mapping)):
        count = count - 1
    #################

    return count


# Example 1
billFirstName = "Egnora"
billLastName = "Doe"
shipFirstName = "Jane Marie"
shipLastName = "Smith"
billNameOnCard = "Egni Doe"
nickname_csv = "names_.csv"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 1
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Deborah"
shipLastName = "Egli"
billNameOnCard = "Deborah Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 2
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Debbie"
shipLastName = "Egli"
billNameOnCard = "Debbie Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 3
billFirstName = "Deborah"
billLastName = "Egni"
shipFirstName = "Debbie"
shipLastName = "Egli"
billNameOnCard = "Debbie Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 4
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Deborah"
shipLastName = "Egli"
billNameOnCard = "Egli Deborah"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 5
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Mechael"
shipLastName = "Egli"
billNameOnCard = "Debbie Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 6
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Egli"
shipLastName = "Deborah"
billNameOnCard = "Deborah Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 6
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Deborah"
shipLastName = "Egli"
billNameOnCard = "Debbie Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 7
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Egli"
shipLastName = "Deborah"
billNameOnCard = "Deborah Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)

# Example 8
billFirstName = "Deborah"
billLastName = "Egli"
shipFirstName = "Deb"
shipLastName = "Eglah"
billNameOnCard = "DD Egli"

result = countUniqueNames(billFirstName, billLastName, shipFirstName, shipLastName, billNameOnCard, nickname_csv)
print("Number of unique names:", result)
