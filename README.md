#sports world

*Explain how you implemented the checklist above step-by-step (not just by following the tutorial).*
I implement the checklist by first set up and create the project. After setting up the project, in the main/models.py i added product models with the required fields : name, price, description, thumbnail, category, is_featured. Then, i updated the view and template that send the app name, my name, and my class to the template. I also updated the routing in main/urls.py and sports_world/urls.py. After that i ran a local test and since the test is allready correct, i deploy the app to the PWS

*Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.*

diagram link : https://drive.google.com/file/d/1M8k1nuCKPGi-nJR1B6YPyZArKHfcyfnu/view?usp=sharing
urls.py : maps the url to view
models.py : define database
html file : display the data in browser

*Explain the role of settings.py in a Django project!*
stores global config like installed apps, middleware, databases, allowed hosts, static files, and environment variables.

*How does database migration work in Django?*
When we change the model,we need to run makemigrations for django to create a migration files and after that run migrations so django can  change and update the database

*In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development?*
Because it have a clear structure(MVT), comes with build in features, used in many apps, it is  capable to do documentation, and have a strong comunity

*Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed?*
I think the instruction were clear 


