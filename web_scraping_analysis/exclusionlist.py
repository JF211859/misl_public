import pandas as pd

fall22 = pd.read_csv("Fall22_DeptListRA.xlsx - Combined.csv")

fall22_urls = fall22["URL"]

qualtrics = pd.read_csv("Qualtrics_Fall2022.csv")

qualtrics_urls = qualtrics["Link"][2:]

need_to_do = pd.concat([fall22_urls, qualtrics_urls]).drop_duplicates(keep=False)

need_to_do.to_csv("Unfinished_URLS.csv")
