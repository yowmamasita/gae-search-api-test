from ferris import Controller, messages, route_with
from ferris.components.search import Search
from app.models.post import Post


class Posts(Controller):
    class Meta:
        Model = Post
        components = (messages.Messaging, Search,)
        prefixes = ('api',)

    @route_with('/api/posts/search')
    def api_search(self):
        self.context['data'] = self.components.search()

    @route_with('/api/posts/primedb')
    def api_prime_db(self):
        Post(title="apple test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="Banana test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="CARROT TEST", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="Jackfruit Test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="Zebra test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        return 200
