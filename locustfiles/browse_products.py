from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1, 5) # as user doesnt open all the tasks at once so this is for 
    # giving some wait between each task randomly to give it a real look

    # Viewing products
    @task(2) # now the value in the task is for priority
    def view_products(self):
        # print("viewing products")
        collection_id = randint(2, 6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name='/store/products')

    # Viewing product details
    @task(4)
    def view_product(self):
        # print("viewing specific product")
        product_id = randint(1, 1000)
        self.client.get(f'/store/products/{product_id}', name='/store/products/:id')

    # Add product to cart
    @task(1)
    def add_to_cart(self):
        # print("Adding products to cart")
        product_id = randint(1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            json={
                'product_id':product_id,
                'quantity': 1 
            }
        )
    @task
    def say_hello(self):
        self.client.get('/playground/hello/')

    # this is the default method which is called whenever a new user start 
    # browsing our website
    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']
        print(f"Cart ID created: {self.cart_id}")

