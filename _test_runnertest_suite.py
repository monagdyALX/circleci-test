import unittest
from main import *

# Add imports here
from main import app


class UnitTests(unittest.TestCase):

  def test_home_res(self):
      # Enter code here
      with app.test_client as c:
        res = c.get("/")
        assert res.data == b'Hello from Flask!'
        assert res.status == 200
    
      
    
    
    

