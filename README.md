# simple web-server

### Easy Setup
```python
pip install Flask
python hello.py

# Running on http://localhost:5000/
```

#Lessons learned : 
- `pip freeze > requirements.txt` :: places all dependencies inside txt file which can be read later
 - `pip install -r requirements.txt`
- `mongorestore` reads dump directory and builds mongodb 
- running server.py, which references mongo_liaison.py, will create temporary python compiled file ? 
 - `mongo_liaison.pyc` gets created during exection of web server
- dumps (converts binary object to JSON)
- flask responses