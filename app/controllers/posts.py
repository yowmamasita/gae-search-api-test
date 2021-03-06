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

    @route_with('/api/posts/verify')
    def api_verify(self):
        # case 1: query = test, limit = 4
        results = self.components.search(query="test", limit=4)
        assert len(results) == 4

        # case 2: query = APPLE
        results = self.components.search(query="APPLE")
        assert len(results) == 1

        # case 3: query = carrot
        results = self.components.search(query="carrot")
        assert len(results) == 1

        # case 4: query = Hello World, sorted by title in asc order
        results = self.components.search(query="Hello World", sort_field='title', sort_direction='asc')
        assert len(results) == 5
        assert 'Banana' in results[0].title
        assert 'apple' in results[4].title

        # case 5: query = Lorem, sorted by title in desc order
        results = self.components.search(query="lorem", sort_field='title', sort_direction='desc')
        assert len(results) == 3
        assert 'Zebra' in results[0].title
        assert 'CARROT' in results[2].title

        return "All tests passed"

    @route_with('/api/posts/prime_db')
    def api_prime_db(self):
        Post(title="apple test", content="Hello, World!").put()
        Post(title="Banana test", content="Hello, World!").put()
        Post(title="CARROT TEST", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="Jackfruit Test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        Post(title="Zebra test", content="Hello, World! Lorem ipsum dolor sit amet.").put()
        return 200

    @route_with('/api/posts/clear_db')
    def api_clear_db(self):
        for key in Post.query().fetch(keys_only=True):
            key.delete()
        return 200
