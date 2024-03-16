# Python - Object-relational mapping
** Object-Relational Mapping (ORM) is a programming technique used in software development to bridge the gap between the object-oriented programming (OOP) paradigm, typically used in application code, and relational databases, which store data in tables with rows and columns.**

** In traditional programming, data is often represented as objects with properties and methods. However, relational databases store data in tables, where each table consists of rows and columns. This disconnect between the object-oriented world and relational databases can lead to complexities and inefficiencies when interacting with databases. **

```
 ORM solves this problem by providing a mechanism to map objects in application code to rows in database tables and vice versa. It allows developers to work with data in the database using objects and classes, rather than dealing directly with SQL queries and database-specific syntax.
 ```


## Learning Objectives
+ Why Python programming is awesome
- How to connect to a MySQL database from a Python script
+ How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
- What ORM means
* How to map a Python Class to a MySQL table


## More Info
Install and activate venv

To create Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```


## Install MySQLdb module version 2.2x
for installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](/rltoken/paGukker_OKoG3D9FqymNQ)

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zliblg-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
 (2, 0, 'final', 0)
```

## Install SQLAlchemy module version 1.4.x

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-package/sqlalchemy/engine/default.py:552: Warning: (1681, " '@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
 cursor.execute(statement, parameters)
```

You can ignore it.
