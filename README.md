# E-NEWS

# Author
Josphine Ndanu



### Description
E-NEWS is a web appliction that displays a list of news sources from around the world. A user is able to click on a news source and view an abreviated version of the particular news article. Clicking on the news article will then redirect you to the news article's web page.


## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |-------------| ------------|
|Display news source| Home page | A list of various news sources|
| Viewing articles  | click view articles button| A list of articles from a specific source|
| Read article      | CLick read more | Redirect to the original source| 

#### Prerequisties
Python 3.8
Flask
Pip

## Setup/ running application
To acccess this project on your local files, follow the following procedure

1. Install python version 3.8
1. Clone this repository :  `$ git clone https://github.com/ndanu-josy/News-API.git'
1. create  a virtual environment 
1. Get an api key from https://newsapi.org/ 
1. Create a start.sh file and store your key there: i.e
    export NEWS_API_KEY='<Your-Api-Key>'
    python3.8 manage.py server

1. run $chmod a+x start.sh
1. then  run ./start.sh

## View Site
View [live](https://e-news5020.herokuapp.com/)


## Technologies used
Python 3.8
Bootstrap
Flask


This project is under the  [MIT](LICENSE) licence


 

