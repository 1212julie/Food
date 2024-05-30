import sqlite3
import csv

def create_tables():
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    cursor.execute('''
    DROP TABLE IF EXISTS recipes;
    DROP TABLE IF EXISTS reviews;
    ''')

    cursor.execute('''
    CREATE TABLE recipes (
        RecipeId INT PRIMARY KEY, 
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
        AggregatedRating REAL,
        ReviewCount INT,
        Calories REAL,
        FatContent REAL,
        SaturatedFatContent REAL,
        CholesterolContent REAL,
        SodiumContent REAL,
        CarbohydrateContent REAL,
        FiberContent REAL,
        SugarContent REAL,
        ProteinContent REAL,
        RecipeServings TEXT,
        RecipeYield TEXT,
        RecipeInstructions TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE reviews (
        ReviewId INT PRIMARY KEY,
        RecipeId INT,
        AuthorId INT,
        AuthorName TEXT,
        Rating INT,
        Review TEXT,
        DateSubmitted TEXT,
        DateModified TEXT,
        FOREIGN KEY (RecipeId) REFERENCES recipes (RecipeId)
    );
    ''')

    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect('food.db')
    cursor = conn.cursor()

    with open('recipes_top1000.csv', 'r') as recipes_file:
        dr = csv.DictReader(recipes_file)
        to_db = [(i['RecipeId'], i['Name'], i['AuthorId'], i['AuthorName'], i['CookTime'], i['PrepTime'], 
                  i['TotalTime'], i['DatePublished'], i['Description'], i['Images'], i['RecipeCategory'], 
                  i['Keywords'], i['RecipeIngredientQuantities'], i['RecipeIngredientParts'], 
                  i['AggregatedRating'], i['ReviewCount'], i['Calories'], i['FatContent'], 
                  i['SaturatedFatContent'], i['CholesterolContent'], i['SodiumContent'], 
                  i['CarbohydrateContent'], i['FiberContent'], i['SugarContent'], i['ProteinContent'], 
                  i['RecipeServings'], i['RecipeYield'], i['RecipeInstructions']) for i in dr]
        cursor.executemany('''
            INSERT INTO recipes (RecipeId, Name, AuthorId, AuthorName, CookTime, PrepTime, TotalTime, DatePublished, 
            Description, Images, RecipeCategory, Keywords, RecipeIngredientQuantities, RecipeIngredientParts, 
            AggregatedRating, ReviewCount, Calories, FatContent, SaturatedFatContent, CholesterolContent, 
            SodiumContent, CarbohydrateContent, FiberContent, SugarContent, ProteinContent, RecipeServings, 
            RecipeYield, RecipeInstructions) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', to_db)

    with open('reviews_top1000.csv', 'r') as reviews_file:
        dr = csv.DictReader(reviews_file)
        to_db = [(i['ReviewId'], i['RecipeId'], i['AuthorId'], i['AuthorName'], i['Rating'], i['Review'], 
                  i['DateSubmitted'], i['DateModified']) for i in dr]
        cursor.executemany('''
            INSERT INTO reviews (ReviewId, RecipeId, AuthorId, AuthorName, Rating, Review, DateSubmitted, DateModified) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        ''', to_db)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    load_data()
    print("Database initialized with data from CSV files.")
