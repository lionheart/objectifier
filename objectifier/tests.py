from unittest import TestCase

from objectifier import Objectifier


class BasicTests(TestCase):

    def test_str_1(self):
        obj = Objectifier('abc')
        self.assertEqual(repr(obj), '<Objectifier#list elements:3>')
        self.assertEqual(obj[0], 'a')
        self.assertEqual(obj[1], 'b')
        self.assertEqual(obj[2], 'c')

    def test_str_empty(self):
        obj = Objectifier('')
        self.assertEqual(repr(obj), '<Objectifier#list elements:0>')

    def test_tuple_1(self):
        obj = Objectifier(('abc', 'def'))
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0], 'abc')
        self.assertEqual(obj[1], 'def')

    def test_tuple_of_tuples(self):
        obj = Objectifier((('abc', 'def'), ('ghi', 'jkl')))
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0][0], 'abc')
        self.assertEqual(obj[0][1], 'def')
        self.assertEqual(obj[1][0], 'ghi')
        self.assertEqual(obj[1][1], 'jkl')

    def test_tuple_empty(self):
        obj = Objectifier(())
        self.assertEqual(repr(obj), '<Objectifier#list elements:0>')

    def test_dict_1(self):
        obj = Objectifier({'a': 1, 'b': 2})
        self.assertEqual(repr(obj), '<Objectifier#dict a=int b=int>')
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b, 2)

    def test_dict_2(self):
        obj = Objectifier({'a': 1, 'b': 'c'})
        self.assertEqual(repr(obj), '<Objectifier#dict a=int b=str>')
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b, 'c')

    def test_dict_3(self):
        obj = Objectifier({'a': 1, 'b': {'c': 2}})
        self.assertEqual(repr(obj), '<Objectifier#dict a=int b=dict>')
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b.c, 2)

    def test_dict_3(self):
        obj = Objectifier({'a': 1, 'b': {'c': 2, 'd': {'e': [3, {'f': 4}]}}})
        self.assertEqual(repr(obj), '<Objectifier#dict a=int b=dict>')
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b.c, 2)
        self.assertEqual(obj.b.d.e[0], 3)
        self.assertEqual(obj.b.d.e[1].f, 4)

    def test_list_of_ints(self):
        obj = Objectifier([1, 2])
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0], 1)
        self.assertEqual(obj[1], 2)

    def test_list_of_strings(self):
        obj = Objectifier(['a', 'b'])
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0], 'a')
        self.assertEqual(obj[1], 'b')

    def test_list_of_dicts_1(self):
        obj = Objectifier([{'a': 1}, {'b': 2}])
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0].a, 1)
        self.assertEqual(obj[1].b, 2)

    def test_list_of_dicts_2(self):
        obj = Objectifier([{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
        self.assertEqual(repr(obj), '<Objectifier#list elements:2>')
        self.assertEqual(obj[0].a, 1)
        self.assertEqual(obj[0].b, 2)
        self.assertEqual(obj[1].c, 3)
        self.assertEqual(obj[1].d, 4)

    def test_list_of_tuples(self):
        obj = Objectifier([('a', 1), ('b', 2)])
        self.assertEqual(repr(obj), '<Objectifier#dict a=int b=int>')
        self.assertEqual(obj.a, 1)
        self.assertEqual(obj.b, 2)

    def test_json_1(self):
        people_json = """
            {
                "People": {
                    "Person": [
                        {
                            "Name": "Marc"
                        },
                        {
                            "Name": "Zach"
                        }
                    ]
                }
            }
        """.strip()
        obj = Objectifier(people_json)
        self.assertEqual(repr(obj), '<Objectifier#dict People=dict>')
        self.assertEqual(obj.People.Person[0].Name, 'Marc')

    def test_json_2(self):
        people_json = """
            {
                "People": {
                    "Person": [
                        {
                            "Name": "Marc",
                            "Age": 37
                        },
                        {
                            "Name": "Zach",
                            "Age": 3
                        }
                    ]
                }
            }
        """.strip()
        obj = Objectifier(people_json)
        self.assertEqual(repr(obj), '<Objectifier#dict People=dict>')
        self.assertEqual(obj.People.Person[0].Name, 'Marc')
