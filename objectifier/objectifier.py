import json

class Objectifier(object):
    def __init__(self, response_data):
        if type(response_data) == list:
            try:
                self.response_data = dict(response_data)
            except:
                self.response_data = response_data
        else:
            try:
                self.response_data = json.loads(response_data)
            except ValueError:
                self.response_data = response_data
            except TypeError:
                self.response_data = response_data

    @staticmethod
    def objectify_if_needed(response_data):
        """
        Returns an objectifier object to wrap the provided response_data.
        """
        if hasattr(response_data, 'pop'):
            return Objectifier(response_data)
        return response_data

    def __dir__(self):
        try:
            return self.response_data.keys()
        except AttributeError:
            return []

    def __repr__(self):
        try:
            return "<Objectifier#dict {}>".format(" ".join(["%s=%s" % (k, type(v).__name__)
                for k, v in self.response_data.iteritems()]))
        except AttributeError:
            try:
                return "<Objectifier#list elements:{}>".format(len(self.response_data))
            except TypeError:
                return self.response_data

    def __contains__(self, k):
        return k in self.response_data

    def __len__(self):
        return len(self.response_data)

    def __iter__(self):
        """
        Provides iteration functionality for the wrapped object.
        """
        try:
            for k, v in self.response_data.iteritems():
                yield (k, Objectifier.objectify_if_needed(v))
        except AttributeError:
            try:
                for i in self.response_data:
                    yield Objectifier.objectify_if_needed(i)
            except TypeError:
                raise StopIteration

    def __getitem__(self, k):
        try:
            return Objectifier.objectify_if_needed(self.response_data[k])
        except TypeError:
            return None

    def __getattr__(self, k):
        if k in self.response_data:
            return Objectifier.objectify_if_needed(self.response_data[k])
        return None


