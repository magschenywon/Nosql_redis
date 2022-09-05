# Intro
This project includes three files in total: 
- Database file: **data.json**, 
- Python script to convert the database into my redis database and then output the result to a webpage: **project.py**
- HTML script in the templates file for webpage:  **index.html**

## Database
There are 55 records in data.json file, the first column is the name of each state in U.S., 
and the second column is the number of cases for coronavirus cases in each state in date 4/4/2020. </br>

The code below from project.py is the conversion from my json file to the redis database:

```
r = redis.StrictRedis(host='localhost', port=6379, db=0)
with open('/Users/yiwenchen/desktop/nosql/redis/data.json',encoding="utf8") as data_file:
    test_data = json.load(data_file)
    for x in test_data:
        r.set(str(x['state']), int(x['cases']))
```

## Run as example
- a)	The key value of the key named "District of Columbia"!
```
127.0.0.1:6379> get "District of Columbia"
"902"
```

- b)	To update the value for “District of Columbia”:
```
('state: ', 'District of Columbia', 'cases: ', b'902', '. UPDATED!')
```

- c)	To delete the value for “District of Columba”:
```
('state: ', 'District of Columbia', 'cases: ', b'', '. DELETED!')
```
