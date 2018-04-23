#milkCan
The way that this is designed is to make it work similar to how unit tests work, as well as adding additional features to ensure that speed comparison tests usually end up running faster

##Usage:
Let's you write standard tests that are similar to Unit tests to check and compare execution speeds for different functions on the current hardware

###Understanding Usage in comparison to Unit Tests

####Unit tests

This is what a unit test generally looks like. This one is brutally plagiarised from the [Python 3.6.5 doc](https://docs.python.org/3/library/unittest.html, Python Unit Tests)

```
import unit test

class TestStringMethods(unittest.TestCase): 								#Test class that usually runs all tests

    def test_upper(self):													#First function that runs a test
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):													#Second Function that runs a test
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):													#You get the idea
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()															#This line of code tells the beep-boop thing called a computer to run the afforementioned tests in this module
```

####milkCan tests

Here is what a simple milkCan test look like:

```
import milkCan.speedtests

class SpeedTestStringMethods(milkCan.speedtests):
	"""All managers are robots

	Except for my future manager, he seems pretty cool and will be a leader in the rebellion during the upcoming robot uprising"""
	
	def __init__(self):
		super(ClassName, self).__init__()
		self.speedtestsGroup1 = [self.test_upper, self.test_lower]			#Telling the computer that this is the first group of tests
		self.speedtestsGroup2 = [self.test_isupper, self.test_islower]		#Telling the computer that this is the second group of tests

		self.speedtestGroups(self.speedtestsGroup1, self.speedtestsGroup2)	#Telling the milkCan.speedtests library that these are the tests to run. By default, they run 1 million times to collect all the data needed
		self.timesToRun[0] = 5000											#Telling the milkCan.speedtests library that the test group at position 0 must run 5000 times, not 1 million

	def test_upper(self):													#First function in group 1
		self.getExecutionTime('foo'.upper())								#Getting how long it takes to run this function


	def test_lower(self):													#Second function in group 2
		self.getExecutionTime('FOO'.lower())								#Getting how long it takes to run this function


	def test_isupper(self):													#First function in group 2
		self.getExecutionTime('FOO'.isupper())								#milkCan will add how long it takes for these two function to run together
		self.getExecutionTime('Foo'.isupper())


	def test_islower(self):													#Second function in group 2
		self.getExecutionTime('FOO'.islower())								#milkCan will add how long it takes for these two function to run together
		self.getExecutionTime('Foo'.islower())

if __name__ == '__main__':
	SpeedTestStringMethods.main()											#just like unit tests, we'll run the main method of milkCan.speedtests which the SpeedTestStringMethods inherits
```

For more information, look at the documentation [here](link)
