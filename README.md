# Python demo portfilo

## Preview
http://tomkiworld.pythonanywhere.com/

## Usage 
A demo portfolio website using python for the backend.
For the purpose of practicing Pyhton I used a template from [mashup](http://www.mashup-template.com/templates.html).
The template is called [Univer](http://www.mashup-template.com/preview.html?template=univers).
From which I used the html, js and css to generate templates and macros with [Jinja](https://jinja.palletsprojects.com/en/2.11.x/).

To replace a Database for this exercise. Once a visitor sends a message via the contact form, a line with contact information is add to both database.txt and database.csv in the Database folder.

## Local setup
After cloning the project, run `pip3 install -r requirements.txt` to set up the virtual environment locally.

To start the server execute `flask run` from root directory and `Ctrl + C` to quit.
The server will run on port 5000 `http://127.0.0.1:5000/`

## Libraries 

### [csv](https://docs.python.org/3/library/csv.html)
To save contact information to a csv file instead of a databse
> The csv module implements classes to read and write tabular data in CSV format. It allows programmers to say, 
>“write this data in the format preferred by Excel,” or “read data from this file which was generated by Excel,” 
>without knowing the precise details of the CSV format used by Excel. Programmers can also describe the CSV formats 
>understood by other applications or define their own special-purpose CSV formats.

### [Flask](https://flask.palletsprojects.com/en/1.1.x/)
The micro web framework to handle the server, depending on the 
[Jinja](https://palletsprojects.com/p/jinja/) template engine to generate reusable macro's and use variables in templates.
