from flask import Flask, render_template, request
import init_db
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='movies',
                            user='postgres',
                            password='passwor')
    return conn

@app.route('/')
def index():
    return render_template('search_form.html')


@app.route('/search', methods=['POST'])
def search_movies():
    # Retrieve the search criteria from the request
    title = request.form.get('title')
    actor = request.form.get('actor')
    genre = request.form.get('genre')
    director = request.form.get('director')
    yearfrom = request.form.get('yearfrom')
    yearto = request.form.get('yearto')
    keywords = request.form.get('keywords')
    rating = request.form.get('rating')

    # Set up a database connection
    conn =  get_db_connection()
    cursor = conn.cursor()

    try:
        # Construct the SQL query based on the search criteria
        query = "SELECT DISTINCT movies.title, movies.year, movies.genres, movies.director, movies.overview, movies.rating FROM movies"

        # Join acts_in table to fetch movies where the specified actor is involved
        if actor:
            query += " INNER JOIN acts_in ON movies.title = acts_in.movie AND movies.year = acts_in.year"

        conditions = []
        values = []

        if title:
            conditions.append("movies.title ILIKE %s")
            values.append(f"%{title}%")

        if actor:
            conditions.append("acts_in.actor ILIKE %s")
            values.append(f"%{actor}%")

        if genre:
            conditions.append("movies.genres ILIKE %s")
            values.append(f"%{genre}%")

        if director:
            conditions.append("movies.director ILIKE %s")
            values.append(f"%{director}%")

        if yearfrom:
            conditions.append("movies.year >= %s")
            values.append(yearfrom)

        if yearto:
            conditions.append("movies.year <= %s")
            values.append(yearto)

        if keywords:
            conditions.append("movies.overview ILIKE %s")
            values.append(f"%{keywords}%")
        
        if rating:
            conditions.append("movies.rating >= %s")
            values.append(rating)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Execute the query
        cursor.execute(query, values)
        movies = cursor.fetchall()
        length = []
        length.append(len(movies))
        return render_template('search_results.html', movies=movies, length=length)

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
    