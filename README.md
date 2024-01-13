0x00. AirBnB clone - The console
Description
HolbertonBnB stands as a comprehensive web application that seamlessly incorporates database storage, a back-end API, and a front-end interface, mirroring the functionalities of AirBnB.

This collaborative endeavor is a crucial component of the (Alx) Holberton School Software Engineering program, serving as an initial stride toward the creation of a fully-fledged web application.

The primary objectives of this initial phase encompass:

Development of a tailored command-line interface for effective data management.
Establishment of foundational classes to facilitate the storage of pertinent data

How to start it:
Run the console	./console.py
Quit the console	(hbnb) quit
Display the help for a command	(hbnb) help <command>
Create an object (prints its id)	(hbnb) create <class>
Show an object	(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object	(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class	(hbnb) all or (hbnb) all <class>
Update an attribute of an object	(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")

How to use it(examples)
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
