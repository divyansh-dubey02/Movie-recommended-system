import pandas as pd
import pickle
import os

# Folder where app.py is
# Use a raw string (recommended for Windows paths)
current_dir = os.path.dirname(os.path.abspath(r"C:\Users\DELL\Downloads\movie-recommender-system-tmdb-dataset-main\movie-recommender-system-tmdb-dataset-main"))

print(current_dir)


# Path to your CSV file
movies_file = os.path.join(current_dir, "tmdb_5000_movies.csv")  # update if your CSV has a different name

# Load CSV
movies_df = pd.read_csv(movies_file)

# Keep only 'id' and 'title' columns, rename 'id' to 'movie_id'
movies_df = movies_df[['id', 'title']].rename(columns={'id': 'movie_id'})

# Create model folder if it doesn't exist
os.makedirs(os.path.join(current_dir, "model"), exist_ok=True)

# Save as pickle
with open(os.path.join(current_dir, "model", "movie_list.pkl"), "wb") as f:
    pickle.dump(movies_df, f)

print("✅ movie_list.pkl created successfully!")
