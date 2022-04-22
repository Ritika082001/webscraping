import json
# import requests
# from bs4 import BeautifulSoup
with open("task5.json","r") as f:
    a=json.load(f)
    # print(a)
def annlyse_movie_languages(a):
    dict={}
    for i in a:
        if "Language" in i:
            Language=i["Language"]
            for i in Language:
                if i not in dict:
                    dict[i]= 1
                else:
                    dict[i]+=1
        print(dict)
    with open("task6.json","w") as file:
        json.dump(dict,file,indent=4)
annlyse_movie_languages(a)