<<<<<<< HEAD
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
=======
def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
>>>>>>> 5ca132270be588e1ae4abb0eccc6736a5943ab4f
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

<<<<<<< HEAD
user_profile = build_profile('albert','einstein',
                             location ='princeton',
                             field='physics')

print(user_profile)
=======
user_profile = build_profile('albert','einstein', location='princeton', field='physics')

seang = build_profile('sean','g', height = "5ft10", weight = 157)

print(user_profile)
print(seang)

