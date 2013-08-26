import unittest
import todotools as tt

class TestTodoItem(unittest.TestCase):

    def setUp(self):
        pass

    def test_priority(self):
        from queue import PriorityQueue
        q = PriorityQueue()
        tiP1 = tt.TodoItem('vacuum bedroom', priority=1)
        tiP2 = tt.TodoItem('play video games', priority=2)
        q.put(tiP1)
        q.put(tiP2)
        self.assertEqual(q.get(), tiP1)
        self.assertTrue(q.get(), tiP2)

    def test_name(self):
        ti = tt.TodoItem('vacuum bedroom')
        self.assertEqual(ti.name, 'vacuum bedroom')

        ti.name = 'vacuum hallway'
        self.assertEqual(ti.name, 'vacuum hallway')

    def test_category(self):
        ti = tt.TodoItem('vacuum bedroom', category='household chores')
        self.assertEqual(ti.category, 'household chores')

        ti.category = 'household boredom'
        self.assertEqual(ti.category, 'household boredom')

    def test_category_default(self):
        ti = tt.TodoItem('vacuum bedroom')
        self.assertEqual(ti.category, 'general')

    def test_priority(self):
        ti = tt.TodoItem('vacuum bedroom', priority=3)
        self.assertEqual(ti.priority, 3)

        ti.priority = 5
        self.assertEqual(ti.priority, 5)

if __name__ == '__main__':
    unittest.main()

