import unittest
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from recommend import create_matrix, find_similar_movies, movie_titles

class TestMovieRecommendations(unittest.TestCase):
    
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'userId': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
                'movieId': [1, 2, 2, 3, 3, 4, 4, 5, 5, 6],
                'rating': [4, 5, 3, 4, 5, 3, 4, 2, 1, 4]}
        self.sample_df = pd.DataFrame(data)
        self.sample_X, _, _, _, _ = create_matrix(self.sample_df)
        
    def test_create_matrix(self):
        # Test the create_matrix function
        self.assertIsInstance(self.sample_X, csr_matrix, "X should be a CSR matrix")
        self.assertEqual(self.sample_X.shape[0], len(self.sample_df['movieId'].unique()), "Incorrect number of movies in the matrix")
        self.assertEqual(self.sample_X.shape[1], len(self.sample_df['userId'].unique()), "Incorrect number of users in the matrix")
    
    def test_find_similar_movies(self):
        # Test the find_similar_movies function
        movie_id = 3  # Replace with a valid movie ID from your dataset
        similar_ids = find_similar_movies(movie_id, self.sample_X, k=2)
        self.assertIsInstance(similar_ids, list, "Output should be a list of movie IDs")
        self.assertEqual(len(similar_ids), 2, "Should return 2 similar movie IDs")
    
    def test_movie_recommendation(self):
        # Test the movie recommendation functionality
        movie_id = 3  # Replace with a valid movie ID from your dataset
        similar_ids = find_similar_movies(movie_id, self.sample_X, k=2)
        recommended_titles = [movie_titles[i] for i in similar_ids]
        self.assertIsInstance(recommended_titles, list, "Output should be a list of movie titles")
        self.assertEqual(len(recommended_titles), 2, "Should recommend 2 movies")

if __name__ == '__main__':
    unittest.main()
