class Objectifier(object):
    """
    Object that takes an object as a parameter and returns an object that makes
    object manipulation and inspection very easy. Most effectively used with
    dictionaries.

    >>> data = Objectifier({'name': "Dan", 'cats': [{'name': "Isabelle"}, {'name': "Dante"}]})
    >>> data.name
    Dan
    >>> ", ".join(map(lambda k: k.name, data.cats))
    Isabelle, Dante
    """
    def __init__(self, response_data):
        self.response_data = response_data

    @staticmethod
    def objectify_if_needed(response_data):
        """
        Returns an objectifier object to wrap the provided response_data.
        """
        if type(response_data) in [dict, list]:
            return Objectifier(response_data)
        return response_data

    def __repr__(self):
        if type(self.response_data) == dict:
            return "<Objectifier#dict %s>" % " ".join(["%s=%s" % (k, type(v).__name__) for k, v in self.response_data.iteritems()])
        elif type(self.response_data) == list:
            return "<Objectifier#list elements:%d>" % len(self.response_data)
        else:
            return self.response_data

    def __contains__(self, k):
        if type(self.response_data) in [dict, list]:
            return k in self.response_data
        return False

    def __len__(self):
        return len(self.response_data)

    def __iter__(self):
        """
        Provides iteration functionality for the wrapped object.
        """
        if type(self.response_data) == dict:
            for k, v in self.response_data.iteritems():
                yield (k, Objectifier.objectify_if_needed(v))
        elif type(self.response_data) == list:
            for i in self.response_data:
                yield Objectifier.objectify_if_needed(i)
        else:
            raise StopIteration

    def __getitem__(self, k):
        if type(self.response_data) == dict and k in self.response_data:
            return Objectifier.objectify_if_needed(self.response_data[k])
        elif type(self.response_data) == list and k <= len(self.response_data):
            return Objectifier.objectify_if_needed(self.response_data[k])
        return None

    def __getattr__(self, k):
        if k in self.response_data:
            return Objectifier.objectify_if_needed(self.response_data[k])
        return None


