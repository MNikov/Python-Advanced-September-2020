def add_products_to_dict():
    products = {x: [] for x in input().split(', ')}
    n = int(input())
    total_count = 0
    total_quality = 0
    for _ in range(n):
        category, item, quantity_and_quality_tokens = input().split(' - ')
        quantity_tokens, quality_tokens = quantity_and_quality_tokens.split(';')
        quantity = int(quantity_tokens.split(':')[1])
        quality = int(quality_tokens.split(':')[1])
        total_count += quantity
        total_quality += quality
        products[category].append(item)
    return products, total_count, total_quality


products, total_count, total_quality = add_products_to_dict()

print(f'Count of items: {total_count}')
print(f'Average quality: {total_quality / len(products):.2f}')
[print(f'{c} -> {", ".join(i)}') for c, i in products.items()]
