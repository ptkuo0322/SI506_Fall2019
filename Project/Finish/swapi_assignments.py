import json, requests


ENDPOINT = 'https://swapi.co/api'

PEOPLE_KEYS= ('url','name','height','mass','hair_color','skin_color','eye_color','birth_year','gender','homeworld','species')
PLANET_KEYS= ('url','name','system_position','natural_satellites','rotation_period','orbital_period','diameter','climate','gravity','terrain','surface_water','population','indigenous_life_forms')
STARSHIP_KEYS= ('url','starship_class','name','model','manufacturer','length','width','max_atmosphering_speed','hyperdrive_rating','MGLT','crew','passengers','cargo_capacity','consumables','armament')
SPECIES_KEYS= ('url','name','classification','designation','average_height','skin_colors','hair_colors','eye_colors','average_lifespan','language')
VEHICLES_KEYS= ('url','vehicle_class','name','model','manufacturer','length','max_atmosphering_speed','crew','passengers','cargo_capacity','consumables','armament')





def read_json(filepath):
    '''This function will reads a JSON file and returns a dictionary if provided with a valid filepath.

    Parameters:
        filepath(str):path to file.

    Returns:
        info(dict): dictionary representations of decoded JSON file.
    '''
    with open(filepath, 'r', encoding = 'utf-8') as file:
        info = json.load(file)
    return info

def get_swapi_resource(url, params=None):
    '''Issue a Http request with one optional parameters and return a dictionary that match with the query string if provided.

    Parameters:
        url(str): the base url for the request.
        params(dict): the dictionary that contain specific query string.

    Returns:
        response(dict): a dictionary of the request with the optional parameter.
    '''
    if params:
        response = requests.get(url,params=params).json()
    else:
        response = requests.get(url).json()
    return response

def combine_data(default_data, override_data):
    '''Create a dictionary that combines the key-value pairs from dictionary provided by the two parameter
    Parameters:
        default_data(dict): default dictionary that contains data
        override_data(dict): the dictionary that used to override the same key-value pairs in the default dictionary
    Returns:
        new_dict(dict): a dictionary that combines the key-value paris of both dictionary and the override dictionary, with override values replacing default values on matching keys.
    '''
    new_dict = {}
    for key in default_data.keys():
        new_dict[key] = default_data[key]
    for key in override_data.keys():
        new_dict[key] = override_data[key]
    return new_dict

def filter_data(data, filter_keys):
    '''Create a filtered collection of key-value pairs by the provided two parameters

    Parameters:
        data(dict): the initial dictionary that contain the information.
        filter_keys(tuple): a tuple that can filter the key in the data.

    Returns:
        new_dict1(dict): the filter dictionary containing desire key-value pairs.
    '''
    new_dict1 = {}
    for key in filter_keys:
        if key in data.keys():
            new_dict1[key] = data[key]
    return new_dict1




def is_unknown(value):
    '''This function is used to determine whether the string value equals to what we want
    Parameters:
        value(str): a string that waits to be tested.

    Returns:
        True if a match is obtained.
        False if a match is not obtained.
    '''
    if value.lower().strip() in ['n/a', 'unknown']:
        return True
    else:
        return False

def convert_string_to_float(value):
    '''Converting a string to a floating point value.

    Parameters:
        value(str): the tested string.
    Returns:
        a float if success.
        an unchange value if not success.
    '''
    try:
        return float(value)
    except:
        return value

def convert_string_to_int(value):
    '''Converting a string to a integer value.

    Parameters:
        value(str): the tested string.

    Returns:
        a int if success.
        an unchange value if not success.

    '''
    try:
        return int(value)
    except:
        return value

def convert_string_to_list(value, delimiter=','):
    '''Converting a string of delimited text values to a list.

    Parameters:
        value(str): the string that waits for converting.
        delimiter(str): a string that defaults as ','.

    Returns:
        value_list(list): a desire list.
    '''
    value1 = value.split(delimiter)
    value_list = []
    for element in value1:
        value_list.append(element.strip())

    return value_list

def clean_data(entity):
    '''Coverting dictionary string to different value type such as float,int,list or None
    Parameters:
        entity(dict): key-value pairs that we try to convert.
    Returns:
        cleaned_dict(dict): a dictionary with "cleaned" values.
    '''

    for_float_props=('gravity','length','hyperdrive_rating','width')
    for_int_props=('height','mass','rotation_period','orbital_period','diameter','surface_water','population','average_height','average_lifespan','max_atmosphering_speed','MGLT','crew','passengers','cargo_capacity')
    for_list_props=('hair_color','skin_color','climate','terrain','skin_colors','hair_colors','eye_colors')
    for_dict_props=('homeworld', 'species')
    for_use_props = ('url','name','eye_color','birth_year','gender','surface_water','system_position','natural_satellites','indigenous_life_forms','classification','designation','language','starship_class','model','manufacturer','consumables','vehicle_class','armament')
    #for_notuse_props = ('residents','films','created','edited','peole','manufacturer','model',)
    cleaned_dict = {}

    for key,value in entity.items():

        if type(value) == str and is_unknown(value):
            cleaned_dict[key] = None
        elif key in for_float_props:
            if key == 'gravity':
                value1 = value.split()
                cleaned_dict[key] = convert_string_to_float(value1[0])
            else:
                cleaned_dict[key] = convert_string_to_float(value)
        elif key in for_int_props:
            cleaned_dict[key] = convert_string_to_int(value)
        elif key in for_list_props:
            cleaned_dict[key] = convert_string_to_list(value)
        elif key in for_dict_props[0]:
            info = get_swapi_resource(value)
            info2 = filter_data(info, PLANET_KEYS)
            cleaned_dict[key] = clean_data(info2)
        elif key in for_dict_props[1]:
            info3 = get_swapi_resource(value[0])
            info4 = filter_data(info3, SPECIES_KEYS)
            cleaned_dict[key]= []
            cleaned_dict[key].append(clean_data(info4))
        elif key in for_use_props:
            cleaned_dict[key] = value
        else:
            continue
    return cleaned_dict

#     for_float_props=('gravity','length','hyperdrive_rating','width')
#     for_int_props=('height','mass','rotation_period','orbital_period','diameter','surface_water','population','average_height','average_lifespan','max_atmosphering_speed','MGLT','crew','passengers','cargo_capacity')
#     for_list_props=('hair_color','skin_color','climate','terrain','skin_colors','hair_colors','eye_colors')
#     for_dict_props=('homeworld', 'species')
#     cleaned_dict = {}

#     for key,value in entity.items():

#         if type(value) == str and is_unknown(value):
#             cleaned_dict[key] = None
#         elif key in for_float_props:
#             if key == 'gravity':
#                 value1 = value.split()
#                 cleaned_dict[key] = convert_string_to_float(value1[0])
#             else:
#                 cleaned_dict[key] = convert_string_to_float(value)
#         elif key in for_int_props:
#             cleaned_dict[key] = convert_string_to_int(value)
#         elif key in for_list_props:
#             cleaned_dict[key] = convert_string_to_list(value)
#         elif key in for_dict_props[0]:
#             info = get_swapi_resource(value)
#             info2 = filter_data(info, PLANET_KEYS)
#             cleaned_dict[key] = clean_data(info2)
#         elif key in for_dict_props[1]:
#             info3 = get_swapi_resource(value[0])
#             info4 = filter_data(info3, SPECIES_KEYS)
#             cleaned_dict[key]= []
#             cleaned_dict[key].append(clean_data(info4))
#         else:
#             cleaned_dict[key] = value
#     return cleaned_dict

def assign_crew(starship, crew):
    '''Assign new crew members to a starship by the parameter

    Parameters:
        starship(dict): the dictionary that we want to expand
        crew(dict): the dictionary that provides information for startship to expand.
    Returns:
        starship(dict): the extended key-value pairs.
    '''
    for key, value in crew.items():
        starship[key] = value
    return starship

def write_json(filepath, data):
    '''Writing SWAPI data to a JSON document file.

    Parameters:
        filepath(str): the location of file where we write the file to.
        data: the content that we will write into JSON file.

    Returns:
        None
    '''
    with open(filepath, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent=2)


def main():
    '''This program will interact with local file assets and SWAPI to create two JSON files required by Rebel Alliance Intelligence.

    - A JSON file comprising a list of likely uninhabited planets where a new rebel base could be situated if Imperial forces discover the location of Echo Base.

    - A JSON file of Echo Base information including an evacuation plan of base personnel along with passenger assignments for Princess Leia, the communications droid C-3PO aboard
    the transport Bright Hope escorted by two X-wing starfighters piloted by Luke Skywalker (with astromech droid R2-D2) and Wedge Antilles (with astromech droid R5-D4).

    Parameters:
        None

    Returns:
        None
    '''
    uninhabited_planet_data = []
    source_information = read_json('swapi_planets-v1p0.json')
    for element in source_information:
        if is_unknown(element['population']):
            element_filter = filter_data(element, PLANET_KEYS)
            uninhabited_planet_data.append(clean_data(element_filter))
    write_json('swapi_planets_uninhabited-v1p1.json', uninhabited_planet_data)


    # part2
    echo_base = read_json("swapi_echo_base-v1p0.json")
    params = {'search' : 'Hoth'}
    advanced_url = f'{ENDPOINT}/planets/'
    data1 = get_swapi_resource(advanced_url, params=params)
    swapi_hoth = data1['results'][0]
    echo_base_hoth = echo_base['location']['planet']
    hoth = combine_data(echo_base_hoth, swapi_hoth)
    hoth = filter_data(hoth, PLANET_KEYS)
    hoth = clean_data(hoth)
    echo_base['location']['planet'] = hoth

    echo_base_commander = echo_base['garrison']['commander']
    echo_base_commander = clean_data(echo_base_commander)
    echo_base['garrison']['commander'] = echo_base_commander

    echo_base_smuggler = echo_base['visiting_starships']['freighters'][1]["pilot"]
    echo_base_smuggler = clean_data(echo_base_smuggler)
    echo_base['visiting_starships']['freighters'][1]['pilot'] = echo_base_smuggler

    swapi_vehicles_url = f'{ENDPOINT}/vehicles/'
    swapi_snowspeeder = get_swapi_resource( swapi_vehicles_url, {'search' : 'snowspeeder'})['results'][0]
    echo_base_snowspeeder = echo_base['vehicle_assets']['snowspeeders'][0]['type']
    snowspeeder = combine_data(echo_base_snowspeeder, swapi_snowspeeder)
    snowspeeder = filter_data(snowspeeder, VEHICLES_KEYS)
    snowspeeder = clean_data(snowspeeder)
    echo_base['vehicle_assets']['snowspeeders'][0]['type'] = snowspeeder

    swapi_starships1_url = f'{ENDPOINT}/starships'
    swapi_xwing = get_swapi_resource(swapi_starships1_url, {'search': 't-65 x-wing'})['results'][0]
    echo_base_xwing = echo_base['starship_assets']['starfighters'][0]['type']
    xwing = combine_data(echo_base_xwing, swapi_xwing)
    xwing = filter_data(xwing, STARSHIP_KEYS)
    xwing = clean_data(xwing)
    echo_base['starship_assets']['starfighters'][0]['type'] = xwing

    swapi_starships1_url = f'{ENDPOINT}/starships'
    swapi_gr75 = get_swapi_resource(swapi_starships1_url, {'search': 'gr-75 medium transport'})['results'][0]
    echo_base_gr75 = echo_base['starship_assets']['transports'][0]['type']
    gr75 = combine_data(echo_base_gr75, swapi_gr75)
    gr75 = filter_data(gr75, STARSHIP_KEYS)
    gr75 = clean_data(gr75)
    echo_base['starship_assets']['transports'][0]['type'] = gr75
# code up is no problem

    swapi_starships1_url = f'{ENDPOINT}/starships'
    swapi_falcon = get_swapi_resource(swapi_starships1_url, {'search': 'Millennium Falcon'})['results'][0]
    echo_base_falcon = echo_base['visiting_starships']['freighters'][0]
    falcon = combine_data(echo_base_falcon, swapi_falcon)
    falcon = filter_data(falcon, STARSHIP_KEYS)
    falcon = clean_data(falcon)
    echo_base['visiting_starships']['freighters'][0] = falcon


    swapi_people_url = f"{ENDPOINT}/people/"
    han = get_swapi_resource(swapi_people_url, {'search': 'han solo'})['results'][0]
    han = filter_data(han, PEOPLE_KEYS)
    han = clean_data(han)

    swapi_people_url = f"{ENDPOINT}/people/"
    chewbacca = get_swapi_resource(swapi_people_url, {'search': 'chewbacca'})['results'][0]
    chewbacca = filter_data(chewbacca, PEOPLE_KEYS)
    chewbacca = clean_data(chewbacca)

    m_falcon = assign_crew(falcon, {'pilot': han, 'copilot': chewbacca})
    echo_base['visiting_starships']['freighters'][0] = m_falcon
    write_json('test1.json', echo_base)
# code upto here is no problem

    evac_plan = echo_base['evacuation_plan']
    #print(echo_base['garrison']['personnel'])

    number = 0
    for value in echo_base['garrison']['personnel'].values():
        number = number + value
    evac_plan['max_base_personnel'] = number

    evac_plan['max_available_transports'] = echo_base['starship_assets']['transports'][0]['num_available']

    evac_plan['max_passenger_overload_capacity'] = evac_plan['max_available_transports']*echo_base['starship_assets']['transports'][0]['type']['passengers']*evac_plan['passenger_overload_multiplier']
#write_json('test2.json', echo_base)
    evac_plan = echo_base['evacuation_plan']

    evac_transport = echo_base['starship_assets']['transports'][0]['type'].copy()
    evac_transport['name'] = 'Bright Hope'

# write_json('test2.json', echo_base)

    evac_transport['passenger_manifest'] = []

    swapi_people_url = f"{ENDPOINT}/people/"
    leia = get_swapi_resource(swapi_people_url, {'search': 'leia organa'})['results'][0]
    # print(leia)
    leia = filter_data(leia, PEOPLE_KEYS)
    leia = clean_data(leia)
    evac_transport['passenger_manifest'].append(leia)

    swapi_people_url = f"{ENDPOINT}/people/"
    c3po = get_swapi_resource(swapi_people_url, {'search': 'c-3po'})['results'][0]
    # print(c3po)
    c3po = filter_data(c3po, PEOPLE_KEYS)
    c3po = clean_data(c3po)
    evac_transport['passenger_manifest'].append(c3po)
#write_json('test2.json', echo_base)

    evac_transport['escorts'] = []
    luke_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()
    wedge_x_wing = echo_base['starship_assets']['starfighters'][0]['type'].copy()
    # print(luke_x_wing)
    # print('===============')
    # print(wedge_x_wing)

    swapi_people_url = f"{ENDPOINT}/people/"
    luke = get_swapi_resource(swapi_people_url, {'search': 'luke skywalker'})['results'][0]
    luke = filter_data(luke, PEOPLE_KEYS)
    luke = clean_data(luke)

    swapi_people_url = f"{ENDPOINT}/people/"
    r2d2 = get_swapi_resource(swapi_people_url, {'search': 'r2-d2'})['results'][0]
    r2d2 = filter_data(r2d2, PEOPLE_KEYS)
    r2d2 = clean_data(r2d2)
    luke_x_wing = assign_crew(luke_x_wing, {'pilot': luke, 'astromech_droid': r2d2})
    evac_transport['escorts'].append(luke_x_wing)

    swapi_people_url = f"{ENDPOINT}/people/"
    antilles = get_swapi_resource(swapi_people_url, {'search': 'wedge antilles'})['results'][0]
    antilles = filter_data(antilles, PEOPLE_KEYS)
    antilles = clean_data(antilles)

    swapi_people_url = f"{ENDPOINT}/people/"
    r5d4 = get_swapi_resource(swapi_people_url, {'search': 'r5-d4'})['results'][0]
    r5d4 = filter_data(r5d4, PEOPLE_KEYS)
    r5d4 = clean_data(r5d4)
    wedge_x_wing = assign_crew(wedge_x_wing, {'pilot': antilles, 'astromech_droid': r5d4})
    evac_transport['escorts'].append(wedge_x_wing)
    #print(evac_transport['escorts'])

    evac_plan['transport_assignments'].append(evac_transport)
    echo_base['evacuation_plan'] = evac_plan
    write_json('swapi_echo_base-v1p1.json', echo_base)




if __name__ == '__main__':
    main()
