"""
Module for generating a report discussing how similar the current mission statements are
against older mission statements. And create filtered csv files for later analysis.
"""

# pylint: disable=import-error
import pandas as pd
from pylev import wfi_levenshtein  # type: ignore


def percent_difference(string1: str, string2: str) -> float:
    """
    Function that returns the percent levenshtein difference between two strings
    Based off of the percent difference in words.
    """

    string1_list = string1.split(" ")
    string2_list = string2.split(" ")

    total = max(len(string1_list), len(string2_list))

    difference = wfi_levenshtein(string1_list, string2_list)

    return difference / total


# Should be a csv file that contains at least the columns 'MissionText' and 'WBText'
CSV_FILENAME = "PD Web Scraping_March 14, 2024_09.29.csv"

# Percent difference where any statemnts under this amount will be automatically filtered in
# auto filter step
SIMILARITY_THRESHOLD = 0.05

df = pd.read_csv(CSV_FILENAME)

# Drops any row that does not have a current mission statement
current_mission_statement = df[df["MissionText"].notna()].copy()

# Drops any row that does not have a way back mission statement
both_mission_statements = current_mission_statement[
    current_mission_statement["WBText"].notna()
].copy()

NOT_STATEMENTS = [
    "Mission text:",
    "Wayback mission text",
    '{"ImportId":"QID5_TEXT"}',
    '{"ImportId":"QID3_TEXT"}',
    "n/a",
    "N/A",
    "no mission",
    "(on an image)",
    "no",
    "no ",
    "no mission statement ",
    "none",
    "none - no mission text ",
    "not accessible",
    "not found - there was a server error",
]

# Drop anyhting that isn't a mission statement

both_mission_statements = both_mission_statements[
    ~both_mission_statements["MissionText"].isin(NOT_STATEMENTS)
].copy()
both_mission_statements = both_mission_statements[
    ~both_mission_statements["WBText"].isin(NOT_STATEMENTS)
].copy()

# Filters any row that has identical current and way back misison statements
similar_missions = both_mission_statements[
    both_mission_statements["MissionText"] == both_mission_statements["WBText"]
].copy()

# Filters any row that has differenct current and way back misison statements, difference can potentially be very small
different_missions = both_mission_statements[
    both_mission_statements["MissionText"] != both_mission_statements["WBText"]
].copy()

print(f"Total URLS  : {df.shape[0]}")
print(
    f"Total URLS with current mission statements : {current_mission_statement.shape[0]}"
)
print(f"Total URLS with both mission statements : {both_mission_statements.shape[0]}")
print(f"Same Mission Statements : {similar_missions.shape[0]}")
print(f"Different Misison Statements : {different_missions.shape[0]}")

# Saves to csv for manual review
different_missions[["MissionText", "WBText"]].to_csv("DifferentTexts.csv")

# Calculates percent difference between current and way back mission statements
different_missions["percent difference"] = different_missions.apply(
    lambda x: percent_difference(x.MissionText, x.WBText), axis=1
)

# Filters mission statements which are too similar
auto_remove_too_similar = different_missions[
    different_missions["percent difference"] > 0.05
]

print(
    f"After Auto Filtering ({SIMILARITY_THRESHOLD}% difference are considered identical) : {auto_remove_too_similar.shape[0]}"
)

print(
    f"Average difference in Auto Filtered ({SIMILARITY_THRESHOLD}% difference are considered identical) : "
    f"{sum(auto_remove_too_similar['percent difference']) / auto_remove_too_similar.shape[0]:.3f}"
)

# Saves filtered mission statements
auto_remove_too_similar.reset_index().to_csv(
    "filteredMissionStatements.csv",
    columns=["MissionText", "WBText"],
    index_label="Index",
)

# Reads in csv file after being manually checked to compare to auto filter.
manually_check_differences = pd.read_csv("DifferentTextsManuallyChecked.csv")

# Removes any row that has an 'x' in the "Not Acually Different" column
manually_check_differences = manually_check_differences[
    manually_check_differences["Not Actually Different"] != "x"
]

# Calculates percent difference in manually checked dataset.
manually_check_differences["percent difference"] = manually_check_differences.apply(
    lambda x: percent_difference(x.MissionText, x.WBText), axis=1
)

print(
    f"Manually Checked Different Misison Statements (No automatic filtering): {manually_check_differences.shape[0]}"
)
print(
    f"Average difference in Manually Checked Misison Statements (No automatic filtering) : "
    f"{sum(manually_check_differences['percent difference']) / manually_check_differences.shape[0]:.3f}"
)
