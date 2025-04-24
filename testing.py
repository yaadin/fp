import unittest, sqlite3, tempfile, os
from model.classes import Customer, Movie
from model.dao import CustomerDAO, MovieDAO


DDLSQL = """
CREATE TABLE Customers(id INTEGER PRIMARY KEY,
                       name TEXT, email TEXT, password TEXT);
CREATE TABLE Movies(id INTEGER PRIMARY KEY,
                    title TEXT, genre TEXT,
                    description TEXT, rating TEXT, picture TEXT);
"""

class TestDAO(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
        self.db_path = self.tmp.name

        conn = sqlite3.connect(self.db_path)
        conn.executescript(DDLSQL)
        conn.close()

        self.cust_dao = CustomerDAO(db_name=self.db_path)
        self.mov_dao  = MovieDAO(db_name=self.db_path)

    def tearDown(self):
        os.unlink(self.db_path)


    def test_customer_create_get(self):
        cid = self.cust_dao.create_customer("meder","rakhatbbekov@gmail.com", "123")
        cust = self.cust_dao.get_customer_by_email("rakhatbbekov@gmail.com")
        self.assertEqual(cust.id, cid)
        self.assertEqual(cust.password, "123")

    def test_customer_none(self):
        self.assertIsNone(self.cust_dao.get_customer_by_email("salam@gmail.com"))

    def test_movie_create_get(self):
        mid = self.mov_dao.create_movie(
            "x", "y", "das", "dasd", "dasd"
        )
        movies = self.mov_dao.get_all_movies()
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].id, mid)

if __name__ == '__main__':
    unittest.main()