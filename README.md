# DIS-Project

Our DIS-project is a web-app for searching in a recipe database. 

How to run and use our app:
1. Open pgAdmin4 and create a database called "Food" whíth "postgres" as owner
2. In line 12 in app.py change the password to your own PostgreSQL master password and save changes.
3. In line 10 in init_db.py change the password to your own PostgreSQL master password and save changes.
4. Now open a terminal and navigate to this folder.
5. Run 'python app.py' or 'python3 app.py' in your terminal. 
6. You should now be able to see an address on which the app is running.
7. Click on the address or copy it into your browser. 
8. Type some ingredient, recipe title and/or rating and click 'Search'.
9. You should now get at list containing all the recipes in the database that satisfy these criteria.
10. Tip: recipe title should always start with a capital letter.
11. Example: 

        Recipe Title: Chicken 
        Ingredient: curry
        Minimum Average Rating: 3.5

Search Results

Chicken Curry

Total Time: 45 minutes

Description: A spicy and flavorful dish

Servings: 4

Instructions: 1. Cook the chicken. 2. Prepare the curry sauce. 3. Mix and serve.

Ingredients: Chicken, Coconut Milk, Curry Powder, Garlic, Onions

Average Review Rating: 4.00

Review Count: 2

Reviews:

Perfect blend of spices.
Good but could use more heat.
