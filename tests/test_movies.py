import unittest
from app.models import Movie

# Movie = movie.Movie

class TestMovie(unittest.TestCase):
  '''
  Test class to test behavior of movie class
  '''
  def setUp(self):
    '''
    setup method that will run before each test
    '''
    self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

  def test_instance(self):
    self.assertTrue(isinstance(self.new_movie, Movie))
