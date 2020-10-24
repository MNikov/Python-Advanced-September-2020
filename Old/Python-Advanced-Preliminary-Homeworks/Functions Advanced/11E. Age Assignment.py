def age_assignment(*args, **kwargs):
    name_dict = {}
    # name_dict = {arg: kwargs[args[0]] for arg in args}
    for name in args:
        for key in kwargs:
            if name[0] == key:
                name_dict[name] = kwargs[key]
    return name_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))