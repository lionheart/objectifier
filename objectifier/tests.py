from unittest import TestCase

from objectifier import Objectifier


class BasicTests(TestCase):

    def test_that_succeeds(self):
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
        # print("obj = %r" % obj)
        # print("obj.People = %r" % obj.People)
        # print("obj.People.Person = %r" % obj.People.Person)
        # print("obj.People.Person[0] = %r" % obj.People.Person[0])
        # print obj.People.Person[0]
        self.assertEqual(obj.People.Person[0].Name, 'Marc')

    def test_that_fails(self):
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
        print("obj = %r" % obj)
        print("obj.People = %r" % obj.People)
        print("obj.People.Person = %r" % obj.People.Person)
        print("obj.People.Person.Age = %r" % obj.People.Person.Age)
        print("obj.People.Person[0] = %r" % obj.People.Person[0])
        print obj.People.Person[0]
        self.assertEqual(obj.People.Person[0].Name, 'Marc')
