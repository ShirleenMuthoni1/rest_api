import requests 

def create_product(name, description, price):
    url = 'http://127.0.0.1:5000/products'
    data = {'name': name, 'description': description, 'price': price}
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print('Product created successfully!')
    else:
        print('Error creating product:', response.text)

    def get_products():
        url = 'http://127.0.0.1:5000/products'
        response = requests.get(url)
        if response.status_code == 200:
            print('Products:', response.json())
        else:
            print('Error fetching products:', response.text)

# Example
create_product('Car', 'German machine', 2,500,000)
get_products()

