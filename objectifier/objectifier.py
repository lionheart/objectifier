import json
try:
    import xml.etree.cElementTree as ElementTree
except ImportError:
    import xml.etree.ElementTree as ElementTree


def etree_list_items_all_have_same_tag(l):
    last_tag = None

    for x in l:
        if last_tag is not None and last_tag != x.tag:
            return False

        last_tag = x.tag

    return True


def arrayify_etree(e):
    children = e.getchildren()

    if len(children) == 0:
        return {e.tag: e.text}
    elif len(children) > 1 and etree_list_items_all_have_same_tag(children):
        l = []

        for x in children:
            l.append(arrayify_etree(x)[x.tag])

        return {e.tag: {children[0].tag: l}}
    else:
        d = {}

        for x in children:
            d.update(arrayify_etree(x))

        return {e.tag: d}


def arrayify_xml(xml_str):
    return arrayify_etree(ElementTree.fromstring(xml_str))


class Objectifier(object):
    def __init__(self, response_data):
        if type(response_data) == list:
            if self.is_list_of_2_element_tuples(response_data):
                self.response_data = dict(response_data)
            else:
                self.response_data = response_data
        else:
            try:
                self.response_data = json.loads(response_data)
            except ValueError:
                try:
                    self.response_data = arrayify_xml(response_data)
                except ElementTree.ParseError:
                    self.response_data = response_data
            except TypeError:
                self.response_data = response_data

    def is_list_of_2_element_tuples(self, input):
        if not isinstance(input, list):
            return False

        for item in input:
            if not isinstance(item, tuple) or len(item) != 2:
                return False

        return True

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


