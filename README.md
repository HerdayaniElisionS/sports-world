# sports world

## Assignment2
### Explain how you implemented the checklist above step-by-step (not just by following the tutorial).*
I implement the checklist by first set up and create the project. After setting up the project, in the main/models.py i added product models with the required fields : name, price, description, thumbnail, category, is_featured. Then, i updated the view and template that send the app name, my name, and my class to the template. I also updated the routing in main/urls.py and sports_world/urls.py. After that i ran a local test and since the test is allready correct, i deploy the app to the PWS

### Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.
diagram link : https://drive.google.com/file/d/1M8k1nuCKPGi-nJR1B6YPyZArKHfcyfnu/view?usp=sharing
urls.py : maps the url to view
models.py : define database
html file : display the data in browser

### Explain the role of settings.py in a Django project!
stores global config like installed apps, middleware, databases, allowed hosts, static files, and environment variables.

### How does database migration work in Django?
When we change the model,we need to run makemigrations for django to create a migration files and after that run migrations so django can  change and update the database

### In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development?
Because it have a clear structure(MVT), comes with build in features, used in many apps, it is  capable to do documentation, and have a strong comunity

### Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed?
I think the instruction were clear 

---

## Assignment3

### Why do we need data delivery in implementing a platform?
We need data delivery so that different parts of the app (frontend, backend, mobile, API) can share and use the same data. Without data delivery, they cannot communicate.

### In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
JSON is better because it is simpler, shorter, and faster to read. XML is too heavy with tags. JSON is more popular because it works easily with JavaScript and modern apps.

### What is the purpose of the is_valid() method in Django forms, and why do we need it?
It checks if the form data is correct and safe. If valid, we can save it to the database. If not, Django will show errors.

### Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?
We need csrf_token to stop CSRF attacks. Without it, attackers can trick users into sending fake requests (like deleting data) without permission.

### Explain how you implemented the checklist above step-by-step (not just following the tutorial).
I made a Product model with fields like name, price, description, thumbnail, category, and is_featured. Then I created forms.py for product input. In views.py I added list, add, detail, XML, and JSON views. I updated urls.py for each route. I made templates (main.html, add_product.html, product_detail.html, and base.html). After testing locally, I checked data with Postman, then pushed everything to GitHub.

### Do you have any feedback for the teaching assistants for Tutorial 2?
The tutorial was clear, maybe add more tips for fixing common errors.

## Assignment 4

### What is Django's AuthenticationForm? Explain its advantages and disadvantages.
Django's AuthenticationForm is a built in Django form used to handle user login. It checks the user's username and password. This built in form helps developers manage the login functionality more easily.

### What is the difference between authentication and authorization? How does Django implement the two concepts?
Authentication means checking the identity of users, usually by verifying their username and password so the web application can recognize the user. Authorization means ensuring that each account can only access the resources or perform actions that are meant for them. In Django, after it checks the identity of the user, it ensures that the user has the appropriate permissions to access specific views or resources based on their roles and permissions.

### What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
Sessions store data on the server, making them more secure since they do not expose sensitive information to the user. However, sessions can be slower compared to cookies. Cookies, on the other hand, are faster because they store data on the user's side. However, if not handled properly, cookies can be insecure and vulnerable

### in web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
 Explain how you implemented the checklist above step-by-step (not just following the tutorial).
Cookies are not secure by default. They can be vulnerable to attacks like cross-site scripting (XSS) or cross-site request forgery (CSRF) if not handled properly. These risks happen when hackers can access or change the data stored in cookies. Django helps protect against these risks by adding bult in security options, like the HttpOnly flag to stop JavaScript from accessing cookies, the Secure flag to make sure cookies are only sent over HTTPS,etc. Django also stores sensitive data in sessions on the server, rather than in cookies. To make cookies secure in my project, i make sure i did not store sensitive data in cookies.I keep the sensitive information like passwords or personal data on the server using Django sessions.


## Assignment 5

### CSS Selector Priority: If multiple CSS selectors target an HTML element, explain the priority order for CSS selector selection
CSS specificity hierarchy: inline styles > IDs > classes/attributes/pseudo-classes > elements. !important overrides all. When specificity is equal, the last rule in source order wins.

### Responsive Design
Ensures apps work across all devices, improves UX, boosts SEO, and maintains a single codebase instead of separate versions.

Example
Responsive: Twitter, Shopee
Non-responsive: Older news websites

#### Box Model
Content: The main content 
Padding: Space around the content
Border: Surrounds the padding
Margin: Space outside the border

### Layout System
Flexbox: A layout system that arranges items in a single direction, either in a row or column. It is suitable for simple layouts like navbars, button groups, or aligning items in a row or column.
Grid: A layout system that arranges items in both rows and columns at the same time, suitable for more complex page structures like multi-column designs or complex grids with rows and columns

### Implementation steps
I created Edit and Delete buttons for each product card, visible only to the product owner. I customized the design with SportsWorld branding using green for Sports and blue for World. All buttons use rounded corners so it looks modern. Each product category has a specific color to make it more noticable, orange for shoes, purple for jersey, and brown for equipment. The layout is fully responsive with a grid system that adapts from 1 to 3 columns based on screen size, and prices are displayed in Rp




