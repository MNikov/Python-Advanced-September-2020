def age_assignment(*args, **kwargs):
    return {name: kwargs[name[0]] for name in args}


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
