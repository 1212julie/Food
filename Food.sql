DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS Food;

--Add primary keys

CREATE TABLE recipes (
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
);

CREATE TABLE reviews (
	ReviewId INT,
	RecipeId INT,
	AuthorId INT,
	AuthorName TEXT,
	Rating INT,
	Review TEXT,
	DateSubmitted TEXT,
	DateModified TEXT
);

CREATE TABLE Food (
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
);

COPY recipes FROM 'recipes_top1000.csv' HEADER CSV; 
COPY reviews FROM 'reviews_top1000.csv' HEADER CSV;

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
FROM recipes as rec
	LEFT JOIN reviews as rev 
		ON rec.RecipeID = rev.RecipeID
;

SELECT * FROM Food