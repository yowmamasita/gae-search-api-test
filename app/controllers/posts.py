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
        # case 1: query = test
        try:
            results = self.components.search(query="test")
            assert len(results) == 5
        except:
            raise Exception("Case: query = test, failed")

        # case 2: query = APPLE
        try:
            results = self.components.search(query="APPLE")
            assert len(results) == 1
        except:
            raise Exception("Case: query = APPLE, failed")

        # case 3: query = carrot
        try:
            results = self.components.search(query="carrot")
            assert len(results) == 1
        except:
            raise Exception("Case: query = carrot, failed")

        # case 4: query = Hello, World!
        try:
            results = self.components.search(query="Hello World")
            assert len(results) == 5
        except:
            raise Exception("Case: query = Hello, World!, failed")

        # case 5: query = Lorem
        try:
            results = self.components.search(query="lorem")
            assert len(results) == 3
        except:
            raise Exception("Case: query = Lorem, failed")

        return 200

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
