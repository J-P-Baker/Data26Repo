"""

Exercise: The data in this database has been pulled from https://swapi.dev/. As well as 'people',
the API has data on starships. In Python, pull data on all available starships from the API.
The "pilots" key contains URLs pointing to the characters who pilot the starship.
Use these to replace 'pilots' with a list of ObjectIDs from our characters collection,
then insert the starships into your own collection. Use functions at the very least!

"""

import pymongo
import requests

client = pymongo.MongoClient()
db = client['starwars']




def call_api(api):
    output = []
    #   call API while there is an api to call
    while api is not None:

        # get the output from api of url api
        #   convert to a list of dictionary
        response = dict(requests.get(api).json())

        # make api the next api (be that None or the next page) if it works, append all dicts in list
        #   else just append whats in there to list and make api None to end loop
        try:
            api = response['next']
            for i in response['results']:
                output.append(i)
        except:
            api = None
            output.append(response)
    return output

def get_mongodb_character_id(value):
    #calls the name from mongo db database and returns id only
    character_id =
    return character_id["_id"]db.characters.find_one({"name": value}, {"_id": 1})

def replace_pilots(file):
    #takes every item in file
    for i in file:
        replace = []
        pilots_api_call_key = []
        # if no pilots, pass. if pilot, look up in mongo db, find get name, add to list, list replace pilots url list
        if not i['pilots']:
            pass
        else:
            for o in i['pilots']:
                call = (call_api(o))
                replace.append(get_mongodb_character_id(call[0]["name"]))
            i['pilots'] = replace
    print(file)
    return file


def upload_to_mongodb(input):
    # for every file, upload to starships collection
    for i in input:
        db.starships.insert_one(i)
    print("done")
    return True


if __name__ == '__main__':
    db.starships.drop()
    db.create_collection('starships')

    starting_api = "https://swapi.dev/api/starships"

    print("calling api to return ships json")
    starship_files = call_api(starting_api)
    print("replace pilots 1 by 1")
    starship_files_with_links = replace_pilots(starship_files)
    print("uploading to mongodb")
    upload_to_mongodb(starship_files_with_links)
