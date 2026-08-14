import requests

url = "https://dummyjson.com/products"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(type(data))
print(data.keys())

products = data["products"]

print(type(products))
print(len(products))

first_product = products[0]

print(type(first_product))
print(first_product.keys())

print(first_product["title"])

for product in products:
    print(product["title"])