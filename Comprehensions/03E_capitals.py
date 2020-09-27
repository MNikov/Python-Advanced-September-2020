def pair_capitals_and_countries(countries, capitals):
    return {t[0]: t[1] for t in zip(countries, capitals)}


print('\n'.join(f'{k} -> {v}'for k, v in pair_capitals_and_countries(input().split(', '), input().split(', ')).items()))