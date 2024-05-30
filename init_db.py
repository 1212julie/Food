import psycopg2
import pandas as pd
import csv

# Database connection parameters
db_params = {
    'host': "localhost",
    'user': 'postgres',
    'password': '1212Julie'
}

# Connect to SQLite database (or create it if it doesn't exist)
conn = psycopg2.connect(**db_params, database='postgres')
conn.autocommit = True
cursor = conn.cursor()

#Check if the 'food' database exists
cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'food';")
exists = cursor.fetchone()

# If not exist then create the 'food' database
if not exists:
    cursor.execute("CREATE DATABASE food;")

conn.close()
cursor.close()

# Connect to the 'food' database
conn = psycopg2.connect(**db_params, database='food')
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS Recipes;")
cursor.execute("DROP TABLE IF EXISTS Reviews;")
cursor.execute("DROP TABLE IF EXISTS Food;")

# Create recipes table
cursor.execute('''CREATE TABLE Recipes (
    RecipeId INT, 
    Name TEXT, 
    AuthorId INT, 
    AuthorName TEXT, 
    CookTime TEXT,
    PrepTime TEXT,
    TotalTime TEXT,
    DatePublished TEXT,
    Description TEXT,
    Images TEXT,
    RecipeCategory TEXT,
    Keywords TEXT,
    RecipeIngredientQuantities TEXT,
    RecipeIngredientParts TEXT,
    AggregatedRating TEXT,
    ReviewCount TEXT,
    Calories TEXT,
    FatContent TEXT,
    SaturatedFatContent TEXT,
    CholesterolContent TEXT,
    SodiumContent TEXT,
    CarbohydrateContent TEXT,
    FiberContent TEXT,
    SugarContent TEXT,
    ProteinContent TEXT,
    RecipeServings TEXT,
    RecipeYield TEXT,
    RecipeInstructions TEXT
);''')

# Create reviews table
cursor.execute('''CREATE TABLE Reviews (
    ReviewId INT,
    RecipeId INT,
    AuthorId INT,
    AuthorName TEXT,
    Rating INT,
    Review TEXT,
    DateSubmitted TEXT,
    DateModified TEXT
);''')

# Create Food table
cursor.execute('''CREATE TABLE Food (
    RecipeId INT, 
    Name TEXT, 
    AuthorId INT, 
    AuthorName TEXT, 
    CookTime TEXT,
    PrepTime TEXT,
    TotalTime TEXT,
    Description TEXT,
    Images TEXT,
    RecipeCategory TEXT,
    Keywords TEXT,
    RecipeIngredientQuantities TEXT,
    RecipeIngredientParts TEXT,
    AggregatedRating TEXT,
    ReviewCount TEXT,
    RecipeServings TEXT,
    RecipeInstructions TEXT,
    ReviewId INT,
    recipeId_review INT,
    authorId_review INT,
    authorName_review TEXT,
    Rating INT,
    Review TEXT
);''')

# Load data from CSV files into pandas DataFrames
recipes_df = pd.read_csv('recipes_top1000.csv')
reviews_df = pd.read_csv('reviews_top1000.csv')

# Insert data into recipes table
recipes_df.to_sql('Recipes', conn, if_exists='append', index=False)

# Insert data into reviews table
reviews_df.to_sql('Reviews', conn, if_exists='append', index=False)

# Insert data into Food table by joining recipes and reviews
cursor.execute('''
INSERT INTO Food 
    SELECT 
        rec.RecipeId, 
        rec.Name, 
        rec.AuthorId, 
        rec.AuthorName, 
        rec.CookTime,
        rec.PrepTime,
        rec.TotalTime,
        rec.Description,
        rec.Images,
        rec.RecipeCategory,
        rec.Keywords,
        rec.RecipeIngredientQuantities,
        rec.RecipeIngredientParts,
        rec.AggregatedRating,
        rec.ReviewCount,
        rec.RecipeServings,
        rec.RecipeInstructions,
        rev.ReviewId,
        rev.RecipeId as recipeId_review,
        rev.AuthorId as authorId_review,
        rev.AuthorName as authorName_review,
        rev.Rating,
        rev.Review
    FROM Recipes as rec
    LEFT JOIN Reviews as rev 
    ON rec.RecipeId = rev.RecipeId;
''')

# Commit the transaction
conn.commit()

# Select all data from Food table and print it
cursor.execute("SELECT * FROM Food;")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

# Close the connection
conn.close()
