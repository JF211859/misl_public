"""
Creates a csv file that containes the urls to the largest police departments, excluding
those that we already have categorized.
"""


import pandas as pd

large_police_departments = pd.read_csv("largestPDs3.25.csv")

finished_urls = pd.read_csv("PD Web Scraping_March 25, 2024_14.55.csv")

department_list = pd.read_csv(
    "Fall22_DeptListRA.xlsx - Combined.csv", usecols=["NAME", "URL"]
)

large_police_departments = large_police_departments.merge(
    department_list, on="NAME", how="left"
)

finished_urls_list = set(finished_urls["URL"])

print(f"Total URLS  : {large_police_departments.shape[0]}")

large_police_departments = large_police_departments[
    ~large_police_departments["URL"].isin(finished_urls_list)
].copy()

print(f"Unfinished URLS  : {large_police_departments.shape[0]}")

large_police_departments.reset_index().to_csv(
    "UnfinishedLargePoliceDepartments.csv",
    columns=["NAME", "URL"],
    index_label="Index",
)
