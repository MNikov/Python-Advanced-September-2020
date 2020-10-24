def match_capitals_to_countries():
    countries = input().split(', ')
    capitals = input().split(', ')
    result = zip(countries, capitals)
    [print(f'{t[0]} -> {t[1]}') for t in result]
    # or {t[0]: t[1] for t in result} and print in the specified way


match_capitals_to_countries()
