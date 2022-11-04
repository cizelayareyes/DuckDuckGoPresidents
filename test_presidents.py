import pytest
import requests

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler", "Polk",
              "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
              "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Coolidge", "Hoover", "Truman",
              "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():
    resp = requests.get(url_ddg + "?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    # print(rsp_data["RelatedTopics"][30]["Result"])
    presidentsString = ""
    for x in rsp_data["RelatedTopics"]:
        presidentsString += x["Text"]
    assert all(a in presidentsString for a in presidents)


