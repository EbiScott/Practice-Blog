# Microblog: 
## A Simple Flask App
***
This is a simple Flask application for creating a microblog. Users can post short entries, and the app displays them on the homepage with formatted dates.

### Features
1. Create new blog entries
2. Display existing entries with formatted dates

### Requirements
* Python 3.6 or later
* Flask
* pymongo
* Flask-dotenv (optional, for managing environment variables)
* MongoDB

---

Setup
Clone this repository:
``` Bash
  git clone https://github.com/EbiScott/Practice-Blog/
```

#### Install the required dependencies:
``` Bash
  pip install -r requirements.txt
``` 

Create a .env file in the project root directory and add your MongoDB connection URI:
```
  MONGODB_URI="mongodb://your_mongodb_host:port/"
```
Replace "your_mongodb_host:port" with your actual MongoDB connection details.

* Create a static directory in the project root to store your CSS file (style.css).
  
---

Running the App
#### Start the development server:
``` Bash
  python app.py
```

* Access the app in your web browser at `http://127.0.0.1:5000/` by default.
  
---

### Contributing
Feel free to fork this repository and contribute your own improvements!

___

### License
This project is licensed under the MIT License. See the LICENSE file for details.
