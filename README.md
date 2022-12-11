# Bosch Polls Application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/firarasl/bosch.git
$ cd bosch
```

Activate virtual environment
```sh
$ .\venv\Scripts\activate
```

For Linux:
```sh
$ source venv/Scripts/activate
```


Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```

or

```sh
(venv)$ python3 manage.py runserver
```


And navigate to `http://127.0.0.1:8000`.




## Walkthrough

### Polls' administration

Open the administration version of the website by using the link: http://127.0.0.1:8000/admin/
User: admin
Password: admin

Choose questions in the bar menu on the left side to see available features.
You may search for the needed poll by published date or by title. You may also sort the shown polls.
In order to create a new poll, click on green button on the right corner, specify question, publish date and time, 
choices.
To manage the existing polls, you have to click on the desired question in the previous page. A pop up window will be 
opened to make changes.

## Documentation
To view documentation of this app, use the link: http://127.0.0.1:8000/admin/doc/
Alternatively, you can use the button with a book icon in the right corner of the first page in admin panel.
After choosing desired topics, information will be displayed. 

### Voting process

Open the user version of the website by using the link: http://127.0.0.1:8000/
Choose the required language from the drop down on the right corner of the website.
Website is available in 3 languages: English, German, Ukrainian.
If database contains available questions, you will see them on the first page of the website.
In that case, you may click on one of them to view details regarding the shown question.
Choose the most attractive answer for yourself from the available options.
If you want your nickname to be saved in results pages later, you can write down your name in the input line.
After pressing "Vote" button, you will be redirected to results page.

Options of the previously chosen question will be displayed in the result page. You can view how many people have voted 
for this option. To see names of people, you can click on "Info" button.

To go back to voting page, press "Vote again?".
If you do not want to vote and just want to view the results, then press on corresponding button on this page.
To go back to main page, press "Bosch Polls" logo in the navigation bar.

## Tests

To run the tests, `cd` into the directory where `manage.py` is:
```sh
(venv)$ python manage.py test
```