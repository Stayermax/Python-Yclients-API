# Python-Yclients-API
Python Yclients API wrapper

This is an updated version of this project: https://github.com/Andrii-D/yclients-api

The code added the ability to register a user, as well as work with customer data and their visits.

An example of using the client library is implemented in the main.py file.

Please note that sending requests to get customer data can take time, especially if your database is quite large, since Yclients API can return only 200 results at once. 
Also if sending one request takes more than a few seconds, you may need to connect to another Internet network. 
