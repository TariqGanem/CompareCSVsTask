#About

###Python project which aimed for comparing two CSV files according to the instructions below:

#####Input -

    ● Path to the first csv file to compare

    ● Path to the second csv file to compare

#####Output - String in json format of:

    ● “added” record IDs - records which are found in the first file but not in the second file.

    ● “deleted” record IDs- records which are found in the second csv file and not found in the first csv file.

    ● “changed” record IDs - records which appeared in both csv files but at least one of the values is different.


##Libraries
    ● pandas - Used to analyze data and reading each one of the CSV files into a dataframe to easy use.

    ● flask, flask_restful -  Lightweight WSGI web application frameworks which helped in the process of creating REST API Endpoint. 

    ● unittest - It's built-in module which used for testing the API.

##Manual
####In order to execute the tests follow the steps below:
      
1. Open the terminal or command prompt in your current working directory.
2. Run " python test_app.py "

####On the other hand, in order to run the server and manually check some tests by sending a GET request, follow these steps:
1. Open the terminal or command prompt in your current working directory.
2. Run " python main.py "
3. Open another terminal/command prompt in your current working directory.
4. Run " python test.py "


##Changes In Production
    ●  You should remove the " debug=True " from the main since it's only or local testing.
    ●  You should add more tests and include all edge cases.

##Testing Strategy
The testing strategy used in this project is the simple unittests which initiates a client and sending GET requests to the API.