# AirBnB clone project!
<p align="center">
<img src="https://www.siliconweek.com/wp-content/uploads/2015/09/airbnb_horizontal_lockup_web.png">
</p>

## Description
<p>
A command interpreter to manage your AirBnB objects, it is a limited to specific use-cases for managing the objects of this project.
</p>

## Learning Objectives

General
- How to create a ``Python package``
- How to create a command interpreter in Python using the ``cmd module``
- What is ``Unit testing`` and how to implement it in a ``large project``
- How to ``serialize`` and ``deserialize`` a Class
- How to ``write`` and ``read`` a JSON file
- How to manage ``datetime``
- What is an ``UUID``
- What is ``*args`` and how to use it
- What is `` **kwargs `` and how to use it
- How to handle ``named arguments`` in a function

## Usage
The console works in interactive and non-interactive mode. Prints the indicator (hbnb) and waits for the instruction:

Command                  | Example
--------                 | -------------
Run the console          | ./console.py
Quit the console         | (hbnb) quit
Display the help         | (hbnb) help <command>
Create an object         | (hbnb) create <class>
Show an object           | (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object        | (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects         | (hbnb) all or (hbnb) all <class>
Update an object         | (hbnb) update <class> <id> <attribute name> "<attribute value>"

## Non-interactive mode example

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

## Interactive mode example
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
# Authors
* Piero Ramírez - [GitHub](https://github.com/Piero2023) - [Linkedin](https://www.linkedin.com/in/piero-fernando-ram%C3%ADrez-esteban-33b8b822a/)
* Edgar Condo - [GitHub](https://github.com/EdgaWill) - [Linkedin]()
