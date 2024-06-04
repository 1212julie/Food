import psycopg2
import pandas as pd
import csv

# Database connection parameters
db_params = {
    'host': "localhost",
    'user': 'postgres',
    'password': '1212Julie'
}

# Connect to the default 'postgres' database to check for the existence of the 'Food' database
conn = psycopg2.connect(**db_params, database='postgres')
conn.autocommit = True  # Enable autocommit mode for database creation
cur = conn.cursor()

# Check if the 'Food' database exists
cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'Food'")
exists = cur.fetchone()

# If the database does not exist, create it
if not exists:
    cur.execute('CREATE DATABASE Food')

cur.close()
conn.close()

# Now connect to the newly created or existing 'Food' database
conn = psycopg2.connect(**db_params, database='Food')
cursor = conn.cursor()

# Drop tables if they exist, with CASCADE to handle dependencies
cursor.execute("DROP TABLE IF EXISTS reviews CASCADE;")
cursor.execute("DROP TABLE IF EXISTS ingredients CASCADE;")
cursor.execute("DROP TABLE IF EXISTS recipes CASCADE;")

# Create recipes table
cursor.execute('''CREATE TABLE recipes (
    RecipeId INT PRIMARY KEY, 
    Name TEXT, 
    TotalTime TEXT,
    Description TEXT,
    RecipeServings INT,
    RecipeInstructions TEXT
);''')

# Create reviews table
cursor.execute('''CREATE TABLE reviews (
    ReviewId INT PRIMARY KEY,
    RecipeId INT,
    Rating INT,
    Review TEXT,
    FOREIGN KEY (RecipeId) REFERENCES recipes (RecipeId)
);''')

# Create ingredients table
cursor.execute('''CREATE TABLE ingredients (
    RecipeId INT,
    Ingredient TEXT,
    FOREIGN KEY (RecipeId) REFERENCES recipes (RecipeId)
);''')

# Load data from CSV files into pandas DataFrames
recipes_df = pd.read_csv('recipes.csv')
reviews_df = pd.read_csv('reviews.csv')
ingredients_df = pd.read_csv('ingredients.csv')

# Insert data into recipes table
for index, row in recipes_df.iterrows():
    cursor.execute('''
    INSERT INTO recipes (RecipeId, Name, TotalTime, Description, RecipeServings, RecipeInstructions)
    VALUES (%s, %s, %s, %s, %s, %s)
    ''', tuple(row))

# Insert data into reviews table
for index, row in reviews_df.iterrows():
    cursor.execute('''
    INSERT INTO reviews (ReviewId, RecipeId, Rating, Review)
    VALUES (%s, %s, %s, %s)
    ''', tuple(row))

# Insert data into ingredients table
for index, row in ingredients_df.iterrows():
    cursor.execute('''
    INSERT INTO ingredients (RecipeId, Ingredient)
    VALUES (%s, %s)
    ''', tuple(row))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
