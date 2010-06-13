from tinvent.tests import *

class TestItemsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='items', action='index'))
        # Test response...
