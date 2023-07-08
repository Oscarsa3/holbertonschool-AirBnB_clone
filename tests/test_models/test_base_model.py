"""Unittest for class base
"""
import unittest
import datetime
import os
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Test for this class"""

    def test_BaseModel(self):
        b1 = BaseModel()
        b1_dict = b1.to_dict()
        self.assertAlmostEqual(type(b1_dict['updated_at']), str)
        self.assertTrue('__class__' in b1_dict)
        self.assertAlmostEqual(type(b1.created_at), datetime.datetime)
        self.assertAlmostEqual(type(b1.updated_at), datetime.datetime)

    def test_save(self):
        b2 = BaseModel()
        b_cre = "2017-06-14T22:31:03.285259"
        b2.save()
        self.assertNotEqual(b_cre, b2.created_at)
        self.assertAlmostEqual(os.path.exists('file.json'), True)

    def test_to_dict(self):
        b3 = BaseModel()
        b3_dict = b3.to_dict()
        self.assertTrue('__class__' in b3_dict)
        self.assertAlmostEqual(type(b3_dict['id']), str)
        self.assertAlmostEqual(type(b3_dict['updated_at']), str)
        self.assertAlmostEqual(type(b3_dict['created_at']), str)
