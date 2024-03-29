#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Sara Derakhshani, 14.03.21
# Programmierung 1: Projekt


class StringMatcher:
    """Class for creating string matching objects.

    Attributes
    ----------
    method (str): The string matching method (default is 'finite-state')

    Methods
    -------
    match(pattern, text, case_sensitive=True):
        Matches the pattern to the text input.
    """

    # Algorithms that can be chosen for string matching
    methods = ['naive', 'finite-state']

    def __init__(self, method='finite-state'):
        """Initialize StringMatcher object.

        Initialize string matcher object if method is implemented.
        Otherwise don't.

        Keyword Args
        ------------
        method (str): The string matching method (default is 'finite-state')
        """
        if method not in self.methods:
            raise NotImplementedError
        self.method = method

    def match(self, pattern, text, case_insensitive=False):
        """Match a pattern string to a text string.

        Find all pattern occurrences in the text.

        Args
        ----
        pattern (str): The matching pattern.
        text (str): The string to match the pattern to.

        Keyword Args
        ------------
        case_insensitive (bool): Flag for enabeling case sensitivity mode
            (default is False)

        Return
        ------
        list: Start positions of all pattern occurrences
        """
        # If pattern is empty string return every position in text
        if len(pattern) > 0:
            if case_insensitive is True:
                pattern = pattern.lower()
                text = text.lower()
            if self.method == 'naive':
                return self.__naive_matching(pattern, text)
            elif self.method == 'finite-state':
                return self.__finite_state_matching(
                    text,
                    self.__compute_transitions(pattern,
                                               set(text)
                                               ),
                    len(pattern)
                    )
        else:
            return [i for i in range((len(text) + 1))]

    @staticmethod
    def __naive_matching(pattern, text):
        """Do string matching with naive string matching algorithm.

        Args
        ----
        pattern (str): The matching pattern
        text (str): The string to match the pattern to

        Return
        ------
        list: Start positions of all pattern occurrences
        """
        matched_positions = []
        n = len(text)
        m = len(pattern)
        # Last possible pattern starting position in the text is n - m
        for pos in range((n - m) + 1):
            if pattern == text[pos:(pos+m)]:
                matched_positions.append(pos)
        return matched_positions

    @staticmethod
    def __finite_state_matching(text, transitions, pattern_length):
        """Do string matching with finite state string matching algorithm.

        Args
        ----
        text (str): The matching text
        transitions (dict): The transition functions of the FSM
        pattern_length (int): Number of characters in pattern

        Return
        ------
        list: Start positions of all pattern occurrences
        """
        occurence_positions = []
        n = len(text)
        # start state
        q = 0
        # Run the text through the FSM
        for i in range(n):
            q = transitions[(q, text[i])]
            # The accepting state is reached when the state number is equal
            # to the pattern length
            if q == pattern_length:
                occurence_positions.append(((i+1)-pattern_length))
        return occurence_positions

    @staticmethod
    def __compute_transitions(pattern, alphabet):
        """Compute transitions functions of finite state machine.

        Args
        ----
        pattern (str): The pattern accepted by the FSM
        alphabet (set): The alphabet of the FSM

        Return
        ------
        dict: Transition functions of the FSM
        """
        transitions = {}
        m = len(pattern)
        # Create transitions for each pattern element in each pattern position
        for q in range((m+1)):
            for element in list(alphabet):
                k = min((m+1), (q+2))
                k -= 1
                pattern_k = pattern[0:k]
                pattern_q_a = pattern[0:q] + element
                # Creating transition to next state if the current element
                # is accepted in the current position
                if pattern_q_a.endswith(pattern_k) is True:
                    transitions[(q, element)] = k
                    continue
                # If current element can't be accepted in current position
                # create transition back to a previous state or create loop
                while (pattern_q_a.endswith(pattern_k) is False):
                    if k > 0:
                        k -= 1
                        pattern_k = pattern[0:k]
                        if pattern_q_a.endswith(pattern_k) is True:
                            transitions[(q, element)] = k
                    else:
                        break
        return transitions
