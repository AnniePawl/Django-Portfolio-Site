## Django Portfolio Site Assignment

**How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?**
One significant difference between Django and Flask is the routing system. Flask uses a route decorator (e.g `@app.route('/')`), whereas routing in Django is handled in urls.py file (e.g `urlpatterns = [path('', views.home),]`). The urlspatterns list consists of url() instances which tell Django what to load. Urls need to be mapped to views to display something. <br>

**Why do we use 2 separate urls.py files? How do they interact?**
When a user requests a specific page, Django determines the root URLconf module to use. It loads that module and looks for the variable 'urlpatterns'. Then it runs thru each pattern and stops at the one that matches the requested URl against path_info. Finally, it calls a given view. <br>

**When is it desirable to split our code over multiple apps? Why would we want to do so?**
A single Django project can have multiple applications, which helps keep the project structure organized. Each app represents a discrete part of a larger project.
