"""File that highlights the changes that are made to Mission Statements"""

# imports

from difflib import ndiff

# import pandas as pd


def differences(text1, text2) -> tuple[str, str]:
    """
    Finds differences between two texts, returns two strings, the first being what
    must be insterted into text1 to get text2, and the second being what must be deleted
    from text1 to get text2
    """

    deletians = ""
    insertians = ""

    text1 = text1.split(" ")
    text2 = text2.split(" ")

    for diff in ndiff(text1, text2):
        if diff[0] == "-":
            deletians += diff[2:] + " "
        if diff[0] == "+":
            insertians += diff[2:] + " "

    return insertians, deletians

insertians, deletians = differences("A B C D","B C D E F")

print(f"Insertians = {insertians}, Deletians = {deletians}")


# CSV_FILENAME = "filteredMissionStatements.csv"

# df = pd.read_csv(CSV_FILENAME)

# df["insertians"] = df.apply(lambda x: differences(x.MissionText, x.WBText)[0], axis=1)
# df["deletians"] = df.apply(lambda x: differences(x.MissionText, x.WBText)[1], axis=1)

# df.to_csv("insertians.csv")
