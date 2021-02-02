# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# String-Matching-Tool


class StringMatcher:

		methods = ['naive', 'finite-state']

		def __init__(self, method='naive'):
				if method not in self.methods:
						raise NotImplementedError
				self.method = method

		def match(self, pattern, text):
			if self.method == 'naive':
				return self.__naive_matching(pattern, text)
			elif self.method == 'finite-state':
				pass

		@staticmethod
		def __naive_matching(pattern, text):
			matched_positions = []
			n = len(text)
			m = len(pattern)
			# For each position from 0 to n-m in text check if 
			# text[position] + (m-1) following element(s) match pattern
			for pos in range((n - m) + 1):
				if pattern == text[pos:(pos+m)]:
					matched_positions.append(pos)
			return matched_positions
