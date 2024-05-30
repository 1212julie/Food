from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('food.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('search_form.html')

@app.route('/search', methods=['POST'])
def search():
    ingredients = request.form['ingredients']
    ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]
    
    query = """
    SELECT * FROM recipes
    WHERE {}
    """.format(' AND '.join([f"RecipeIngredientParts LIKE '%{ingredient}%'" for ingredient in ingredient_list]))

    conn = get_db_connection()
    recipes = conn.execute(query).fetchall()
    conn.close()

    return render_template('search_results.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
