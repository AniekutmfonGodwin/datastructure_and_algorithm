import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("set up is called")
        self.data = dict(name = "anies")
        return 

    def test_upper(self):
        print("data ",self.data)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("data ",self.data)
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()