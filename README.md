# DIS-Project

For our DIS-project, we've developed a web-app for searching in a movies database. In this version our database consists of the 1000 highest rated movies of IMDb.
If this is the first time using our app, you'll have to initilize a postgres database.
  1. Open PGAdmin
  2. Rightclick the desired server, then go to Create > Database...
  3. Name your new database 'movies' and the owner to 'postgres'
  4. Now open the init_db.py file in an editor
  5. In line 8 change the password 'passwor' to your own postgres master password and save changes
  6. Now open a terminal/cmd-prompt and navigate to this folder 'DIS-Project'
  7. Now type 'python app.py' in your terminal and ENTER
  8. You should now be able to see an address on which the app is running (It should look something like this: '* Running on http://[0-9]^3[\.0-9]^3:[0-9]^4)
  9. Copy this address, open your preffered browser and insert it

How to use the app:
  1. Type some criteria in one or more of the search fields (e.g. Actor: Mikkelsen and Genre: Drama) then click the 'Search' button or hit ENTER
  2. You should now get a list containing all movies in the database that satisfies these criteria
        (in the above example tyou should get the result: 'Adams Æbler', 'Druk', 'Efter Brylluppet' and 'Jagten')
  3. If you want to perferm another search go back to the previous page and change your search criteria
