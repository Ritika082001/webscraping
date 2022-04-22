import json
# from bs4 import BeautifulSoup
from task1 import scrape_top_list
from task4 import movie_details
movies=scrape_top_list()
def get_movie_list_details():
    list=[]
    for i in movies:
        a=i["URL"]
        b=movie_details(a)
        list.append(b)
    print(list)
    with open ("task5.json", "w+") as f:
        json.dump(list,f, indent=4)
    # return list
get_movie_list_details()