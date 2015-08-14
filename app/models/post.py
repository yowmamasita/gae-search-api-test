from ferris import Model, ndb
from ferris.behaviors import searchable


class Post(Model):
    class Meta:
        behaviors = (searchable.Searchable,)

    title = ndb.StringProperty(indexed=False)
    content = ndb.TextProperty()
