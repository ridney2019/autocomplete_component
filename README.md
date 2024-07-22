Autocomplete Component
This repository contains a Django-based autocomplete component designed to provide search suggestions for artists and their albums from a JSON dataset.
Features
•	Autocomplete search functionality for artists.
•	Displays artist information and album details.
•	Records and displays recent searches.
•	Implements a responsive design using Bootstrap.
Installation
1.	Clone the repository:
git clone https://github.com/ridney2019/autocomplete_component.git
cd autocomplete_component
2.	Set up a virtual environment:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
3.	Install dependencies:
pip install -r requirements.txt
4.	Run migrations:
python manage.py migrate
5.	Load initial data (if any):
python manage.py loaddata initial_data.json
Usage
1.	Start the development server:
python manage.py runserver
2.	Navigate to the home page: Open http://127.0.0.1:8000/ in your web browser.
Project Structure
•	autocomplete_component/: Main Django project folder.
•	search_app/: Django app containing views, templates, and static files.
•	static/: Directory for static files (CSS, JavaScript, images, etc.).
•	templates/: HTML templates for the project.
Views
•	autocomplete: Handles AJAX requests for the autocomplete functionality.
•	recent_searches_view: Displays a list of recent searches.
Templates
•	search.html: Main search page with the autocomplete search box.
•	recent_searches.html: Page displaying recent searches.
Contributing
1.	Fork the repository.
2.	Create a new branch:
git checkout -b feature-name
3.	Commit your changes:
git commit -m 'Add some feature'
4.	Push to the branch:
git push origin feature-name
5.	Create a new Pull Request.
License
This project is licensed under the MIT License.
