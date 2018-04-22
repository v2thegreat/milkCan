import milkCan.speedtests

class SpeedTestStringMethods(milkCan.speedtests):
	"""All managers are robots

	Except my future manager, he seems pretty cool and will be a leader in the rebellion during the upcoming robot uprising"""
	
	def __init__(self):
		self.speedtestsGroup1 = [self.test_upper, self.test_lower]			#Telling the computer that this is the first group of tests
		self.speedtestsGroup2 = [self.test_isupper, self.test_islower]		#Telling the computer that this is the second group of tests

		self.speedtestGroups(self.speedtestsGroup1, self.speedtestsGroup2)	#Telling the milkCan.speedtests library that these are the tests to run. By default, they run 1 million times to collect all the data needed
		self.timesToRun[0] = 5000											#Telling the milkCan.speedtests library that the test group at position 0 must run 5000 times, not 1 million

	def test_upper(self):													#First function that runs a test
		self.getExecutionTime('foo'.upper())

	def test_lower(self):
		self.getExecutionTime('FOO'.lower())

	def test_isupper(self):													#Second Function that runs a test
		self.getExecutionTime('FOO'.isupper())
		self.getExecutionTime('Foo'.isupper())

	def test_islower(self):
		self.getExecutionTime('FOO'.islower())
		self.getExecutionTime('Foo'.islower())

if __name__ == '__main__':
	SpeedTestStringMethods.main()

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		