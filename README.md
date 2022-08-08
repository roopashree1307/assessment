# assessment
Creating a structured project for dynamic data adaption like credentials
Install Pyhton, Pycharm, PIP, Pytest and set up the Path in environment variables.Run the files created using following command for example use command py.test -v -s login_test.py run the the file login_test.py
navigate to Github login page and inspect the page to identify its HTML elements
The id of the login and password input fields, and the name of the Sign-in button will be useful for us to retrieve these elements in code and insert to it programmatically
The find_element_by_id() function retrieves an HTML element by its id, and the send_keys() method simulates keypresses, the above code cell will make Chrome type in the email and the password, and then click the Sign in button
The next thing to do is to determine whether our login was successful, there are a lot of ways to detect that, but in this tutorial, we'll do it by detecting the shown errors upon login
The above image shows what happens when we insert wrong credentials, you'll see a new HTML div element with the class "px-2" that has the text of "Incorrect username or password."
If rigth credentials are given then using text "The home for all developers — including you" that will appear once logged in will be checked for the element being present and successful result will be passed.
Functions like getloginlink, getemailfield, getpasswordfield,getloginbutton is created where it will return element and the actions like clicking on the located element or sending the values to the located elements are performed using clickloginlink, enteremailfield, enterpasswordfield, clickloginbutton
Another method called login will be used to call the above methods given in step 8
Finally methods are used to verify whetehr the passes credentials are valid or not using verifyLoginSuccessful and verifyLoginFailed methods
In login_test directory a file called login_test is present and 2 test cases like test_validLogin and test_invalidLogin are created and their order is set using pytest decorator where the unit test is performed.
