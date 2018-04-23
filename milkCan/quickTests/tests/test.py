from test_lib import quickTests
from unittest import TestCase
from unittest import main

class Unittests_quickTests(TestCase):
	"""docstring for Test_quickTests"""

	def setUp(self):
		from test_lib.primetest import isPrime, isPrime2

		self.testItem1 = isPrime
		self.testItem2 = isPrime2

	def test_quickTests(self):
		t = quickTests.quickTests(range(10**4), self.testItem1, self.testItem2)
		t.run()

		self.assertEqual(t.fastest, self.testItem2)

if __name__ == '__main__':
	main()
