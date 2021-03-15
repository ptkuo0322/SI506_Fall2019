# SI 506 2019F - Problem Set 10

# In this problem set you will work with the Star Wars API. We recommend you read through some of the documentation (https://swapi.co/documentation) and reference it as you work through the following problems. You will also want to reference the requests documentation (https://requests.readthedocs.io/en/master/user/quickstart/#quickstart).

# Responses from the Star Wars API may be slow, don't worry if your terminal "hangs" while making and parsing calls to the API.

# Read the following block quote ENTIRELY before beginning this assignment.

'''
For this assignment, you will build four utility functions (functions that do one small thing) and a main function
(a function that will execute the main purpose of this script). Outside of testing, you should not need to write
any code that is not contained within one of these functions. Below is a description of each of the functions
that you should write. At the bottom of this block quote you will find the grading rubric for the autograder
of this homework. There are tests for several of the functions; you can read about them in the description of
that function.

----- Functions to Create -----

YOU MUST INCLUDE DOCSTRINGS IN ALL YOUR FUNCTIONS TO GET FULL CREDIT

get_data:
    parameters:
        - baseurl (str)
        - resource (str with default value of "")
        - params (dict with default value of an empty dict {})
    description:
        This function should make a call to an API using the <requests> module. <baseurl> should be the
        base url for the API endpoint, <resource> should be which resource is being called, and <params>
        should be a dictionary of any optional parameters.
    returns:
        This function should return a dictionary that is the result of the API call.
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'


search_swapi:
    parameters:
        - resource (str)
        - query (str)
    description:
        This function should use the "search" functionality of SWAPI to search for the <query> string
        given a <resource>. In other words, you might want to search for a query of "luke" in the
        resource "people/". This function should make a call to <get_data> to accomplish this goal.
    returns:
        This function should return a dictionary that is the result of the query.
    test:
        There are a couple tests provided for you at the bottom of this file. They should return 'True'


get_information_on_characters
    parameters:
        - list_of_characters (list)
    description:
        Given a result set of characters from a SWAPI query, return a nested dictionary
        of the character name, birth year, and species name. In other words, <list_of_characters>
        should be a list structured like the value to the key 'results' from the dictionary that
        is returned from <search_swapi>.
    returns:
        This function should return a nested dictionary in the following form:
        {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' : <name of the species of the character>
                    'homeworld_name' : <name of the homeworld of the character>
                }
            <other character name> :
                {
                    ... etc ...
                }
            ... etc ...
        }
    test:
        There is a test provided for you at the bottom of this file. It should return 'True'


write_json:
    parameters:
        - filename (str)
        - data (json-able object, e.g. nested dictionary or list)
    description:
        Write <data> to the .json file specified by <filename>
    returns:
        This function doesn't return anything.
    test:
        There is no test for this function provided, although you are free and encouraged to test this
        function however you see fit.


main:
    parameters:
        (there are no parameters for <main>)
    description:
        Use <search_swapi>, <get_information_on_characters>, and <write_json> to produce the following
        .json files:

        "darth_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "darth" in their name.

        "skywalker_info.json":
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have "skywalker" in their name.

        "tatooine_residents_info.json": <-- CHALLENGE
            - Contains the nested dictionary produced by <get_information_on_characters> for all characters
            in SWAPI that have are residents of "tatooine".
            - HINT: You may want to use your <search_swapi> function with "planets" as the <resource> and
            "tatooine" as the <query> here...and then you'll need to find the URLs of all the characters that
            reside on Tatooine and save their information to a list for <get_information_on_characters> to use.


----- Grading Rubric -----

20 pts: <get_data> works correctly
20 pts: <search_swapi> works correctly
20 pts: <get_information_on_characters> works correctly
20 pts: <write_json> works correctly
10 pts: Every function has a docstring
20 pts: "darth_info.json" is correct
20 pts: "skywalker_info.json" is correct
20 pts: "tatooine_residents_info" is correct
150 points total
'''

import requests
import json

# BEGIN CODING HERE


def get_data(baseurl, resource="",params = {}):
    '''
    description:
        Issue an resquest with two optional parameters and return a dictionary that matched with the query string 
    parameters:
        - baseurl (str) : the base url for the request
        - resource (str): the parameter to specify the the resource which default value is ""
        - params (dict): parameter for the request which default value is an empty dict
    returns:
        a dict of the result of the API call.
    '''
    if params:
        response = requests.get(baseurl+resource + '/', params=params).json()
    else:
        response = requests.get(baseurl+resource + '/').json()
    return response


def search_swapi(resource, query):
    '''
    description:
        given the resource, this function call the get_data to search for the specific <query string> and return the data in dict
    parameters:
        - resource (str): a string specifing the specific resource that we look for.
        - query (str) : a query string that specifies the our target data in the given resource.
    returns:
        a dictionary that is the result of the query.

    '''
    baseurl = "https://swapi.co/api/"
    search_result = get_data(baseurl, resource = resource, params = {"search":query})
    return search_result


def get_information_on_characters(list_of_characters):
    '''
    description:
        Get a result list of characters from the desired SWAPI query.
        Then, return a nested dictionary which contains the character name, birth year,species name, and the homeworld name.
    parameters:
        - list_of_characters (list): a list that is the value to the key 'results' from the dictionary returned from <search_swapi>.

    returns:
        a nested dictionary that contains information of different characters in the following form:
         {
            <character name> :
                {
                    'name' : <character name>
                    'birth_year' : <birth year of the character>
                    'species_name' : <name of the species of the character>
                    'homeworld_name' : <name of the homeworld of the character>
                }
            <other character name> :
                {
                    ... etc ...
                }
            ... etc ...
        }
    '''
    # list_of_characters here is the result that from the search_swapi, 但是list_of_character 只是個代稱
    # 實際上的資料應該是search_swapi所 return 的 data
    nested_dict = {}
    for character in list_of_characters:
        new_char_dict = {}
        new_char_dict['name'] = character['name']
        new_char_dict['birth_year'] = character['birth_year']
        new_char_dict['species_name'] = requests.get(character['species'][0]).json()['name']
        new_char_dict['homeworld_name'] = requests.get(character['homeworld']).json()['name']
        nested_dict[character['name']] = new_char_dict
        
    return nested_dict
# speiced後有index>>>because species on the website is a list but homeworld is not a list.

def write_json(filename, data):
    '''
    description:
        write data to a specified .json file
    parameters:
        - filename (str) : the string that specified the name of the file.
        - data : json-able object, e.g. nested dictionary or list
    returns:
        None
    '''
    with open(filename, 'w', encoding='utf8') as file_obj:
        json.dump(data, file_obj, ensure_ascii=False, indent=2)


def main():
    '''
    description:
        create a json file called 'darth_info.json' containing all characters in SWAPI 
        that have "darth" in their name

        create a json file called 'skywalker_info.json' containing all characters in SWAPI 
        that have "skywalker" in their name

        create a json file called 'tatooine_residents_info.json' containing all characters in SWAPI 
        that are the resident of "tatooine"
        
    parameters:
        None

    returns:
        None
    
    '''

    info_darth = get_information_on_characters(search_swapi('people', 'darth')["results"])
    write_json("darth_info.json", info_darth)

    info_skywalker = get_information_on_characters(search_swapi('people', 'skywalker')["results"])
    write_json("skywalker_info.json", info_skywalker)

    url_link = search_swapi('planets', 'tatooine')["results"][0]['residents']
    resident_list = []
    for url in url_link:
        resident_list.append(requests.get(url).json())
    info_tatooine_residents =get_information_on_characters(resident_list)
    write_json("tatooine_residents_info.json", info_tatooine_residents)
# STOP CODING HERE! DO NOT MODIFY ANYTHING BELOW THIS LINE (except to comment/uncomment tests)!

# The below code will call the <main> function you wrote so long as you are running this
# code directly (as opposed to importing it in another python script).
if __name__ == '__main__':
    main()

    ##### test for <get_data>...uncomment the below two lines when you are ready!
test1 = get_data('https://swapi.co/api/',resource='people',params={'search':'yoda'})['results'][0]['mass']=='17'
print(f"\nTest for <get_data>: {test1}")

    ##### tests for <search_swapi>...uncomment the below four lines when you are ready!
test2 = search_swapi('people','yoda')['results'][0]['mass']=='17'
test3 = search_swapi('starships','tie')['results'][0]['crew']=='1'
print(f"\nTest #1 for <search_swapi>: {test2}")
print(f"Test #2 for <search_swapi>: {test3}")

    ##### test for <get_information_on_characters>...uncomment the below two lines when you are ready!
test4 = get_information_on_characters(search_swapi('people','skywalker')['results'])['Shmi Skywalker']['birth_year']=='72BBY'
print(f"\nTest for <get_information_on_characters>: {test4}")

# END PROBLEM SET 10
