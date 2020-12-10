ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}


def countFriends(dictionary, key, new_key):
    count = 0
    for items in dictionary[key]:
        count += 1
    new_dictionary = dictionary.copy()
    new_dictionary[new_key] = count
    print(new_dictionary)
    return new_dictionary


countFriends(ramit, 'friends', 'friends_count')


countFriends(ramit, "interests", "interests_count")
