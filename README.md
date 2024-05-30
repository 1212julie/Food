# DIS-Project

For our DIS-project, we've developed a web-app for searching in a recipes database. In this version, our database consists of the 1000 highest-rated recipes.

If this is the first time using our app, you'll have to initialize a PostgreSQL database.
1. Open PGAdmin
2. Right-click the desired server, then go to Create > Database...
3. Name your new database 'food' and set the owner to 'postgres'
4. Now open the init_db.py file in an editor
5. In line 8 change the password 'password' to your own PostgreSQL master password and save changes
6. Now open a terminal/cmd-prompt and navigate to this folder 'Food'
7. Type 'python init_db.py' in your terminal and press ENTER to initialize the database
8. Now type 'python app.py' in your terminal and press ENTER
9. You should now be able to see an address on which the app is running (It should look something like this: '* Running on http://[0-9]^3[\.0-9]^3:[0-9]^4')
10. Copy this address, open your preferred browser and insert it

How to use the app:
1. Type some ingredients in the search field (e.g. 'chicken, garlic') then click the 'Search' button or hit ENTER
2. You should now get a list containing all recipes in the database that satisfy these criteria
3. If you want to perform another search, go back to the previous page and change your search criteria
