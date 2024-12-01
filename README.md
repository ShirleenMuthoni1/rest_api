# rest_api
This describes a rest API to manage products.

#Setting up the environment
1. I first nstalled Python
2. I installed Flask using the command: `pip install Flask`
3. I installed the requests library (for client script) using the command: `pip install requests`
4. I created a virtual environment by running the command: python -m venv .venv
   
I created an api file and under it I created two files which are:
1. app.py: Contains the Flask app code.
2. client.py: Contains the client script to interact with the API.

Within the app.py file I wrote code for:
1. Importation: Flask for the app, request and jsonify for handling data.
2. Flask App: Creates a Flask app instance.
3.Products Storage: Initializes an empty list for products.
4. POST Endpoint (/products):
5. Handles POST requests to create products.
6. Extracts JSON data from the request.
7. Validates required fields (name, description, price).
8. Validates price as a number (float).
9. Creates a new product dictionary and appends it to the list.
10. Returns the created product (201 Created) or an error message (400 Bad Request).

The GET Endpoint (/products):
- Handles GET requests to retrieve all products.
- Returns the list of products as JSON.

Handling Requests and Responses
- Endpoints handle JSON requests and responses.
- The HTTP status codes mean:
1. 201 Created: Successful product creation.
2. 400 Bad Request: Invalid data (missing fields, invalid price format).

Within the app.py file I wrote code for:
1. Importing requests- Used for making HTTP requests.
2. create_product function:
-Constructs URL and data for POST request.
-Sends POST request and prints success/error message based on the response.
3. get_products function:
-Sends GET request and prints retrieved products or an error message.
-Example : Creates a new product and retrieves the product list.

I finally committed the assignment in a github repository and submitted the link via google classroom.
