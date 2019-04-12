import unittest
import entry
import work_log
import database
import entry


class simpleTest(unittest.TestCase):
    def setUp(self):
        self.entry = entry.Entry()

    def test_entry(self):
        self.assertIsInstance(self.entry, entry.Entry)
        self.assertEqual(self.entry, entry.Entry())

    def test_collect_new_entry(self):
        work_log.collect_new_entry(entry)
        self.assertEqual(entry, entry.Entry(name="sachin", title="cricket", time_spent=230, notes="most number of 100s"))


if __name__ == "__main__":
	unittest.main()
