
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='Food',
        user='postgres',
        password='1212Julie'
    )
    return conn

@app.route('/')
def index():
    return render_template('search_form.html')

@app.route('/search', methods=['POST'])
def search_recipes():
    title = request.form.get('title')
    ingredient = request.form.get('ingredient')
    min_rating = request.form.get('min_rating')

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        query = '''
        WITH AvgRating AS (
            SELECT RecipeId,
                   AVG(Rating) AS AvgRating,
                   COUNT(Review) AS ReviewCount
            FROM reviews
            GROUP BY RecipeId
        ),
        Reviews AS (
            SELECT RecipeId,
                   STRING_AGG(Review, '; ') AS Reviews
            FROM reviews
            GROUP BY RecipeId
        )
        SELECT r.RecipeId, r.Name, r.TotalTime, r.Description,
               r.RecipeServings, r.RecipeInstructions, 
               STRING_AGG(DISTINCT i.Ingredient, ', ') AS Ingredients,
               ar.AvgRating, ar.ReviewCount,
               rv.Reviews
        FROM recipes r
        LEFT JOIN AvgRating ar ON r.RecipeId = ar.RecipeId
        LEFT JOIN ingredients i ON r.RecipeId = i.RecipeId
        LEFT JOIN Reviews rv ON r.RecipeId = rv.RecipeId
        '''

        conditions = []
        values = []

        if ingredient:
            conditions.append("r.RecipeId IN (SELECT RecipeId FROM ingredients WHERE Ingredient ILIKE %s)")
            values.append(f"%{ingredient}%")

        if title:
            conditions.append("r.Name ILIKE %s")
            values.append(f"%{title}%")

        if min_rating:
            conditions.append("ar.AvgRating >= %s")
            values.append(min_rating)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " GROUP BY r.RecipeId, ar.AvgRating, ar.ReviewCount, rv.Reviews"

        cursor.execute(query, values)
        recipes = cursor.fetchall()
        length = len(recipes)
        return render_template('search_results.html', recipes=recipes, length=length)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
