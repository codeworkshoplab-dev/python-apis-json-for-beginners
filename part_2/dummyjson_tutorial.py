import requests

url = "https://dummyjson.com/products"

response = requests.get(url)

data = response.json()

products = data["products"]

first_product = products[0]

print(first_product["title"])

total = 0

for product in products:
    total = total + product["price"]

print(f"Total: {total:.2f}")

average = total / len(products)

print(f"Average: {average:.2f}")