# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# String-Matching-Tool

# Notes:
# - Fall leerer String für finite state method implementieren (pos 0 fehlt)
# - Keine Positionen -> Return None???


class StringMatcher:

    methods = ['naive', 'finite-state']

    def __init__(self, method='naive'):
        if method not in self.methods:
            raise NotImplementedError
        self.method = method

    def match(self, pattern, text, case_sensitive=True):
        if case_sensitive is False:
            pattern = pattern.lower()
            text = text.lower()
        if self.method == 'naive':
            return self.__naive_matching(pattern, text)
        elif self.method == 'finite-state':
            return self.__finite_state_matching(text,
                                                self.__compute_transitions(pattern,
                                                                           set(text)
                                                                           ),
                                                len(pattern)
                                                )

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

    @staticmethod
    def __finite_state_matching(text, transitions, m):
        occurence_positions = []
        n = len(text)
        q = 0
        for i in range(n):
            q = transitions[(q, text[i])]
            if q == m:
                occurence_positions.append(((i+1)-m))
        return occurence_positions

    @staticmethod
    def __compute_transitions(pattern, alphabet):
        transitions = {}
        m = len(pattern)
        for q in range((m+1)):
            for element in list(alphabet):
                k = min((m+1), (q+2))
                k -= 1
                pattern_k = pattern[0:k]
                pattern_q_a = pattern[0:q] + element
                if pattern_q_a.endswith(pattern_k) is True:
                    transitions[(q, element)] = k
                    continue
                while (pattern_q_a.endswith(pattern_k) is False):
                    if k > 0:
                        k -= 1
                        pattern_k = pattern[0:k]
                        if pattern_q_a.endswith(pattern_k) is True:
                            transitions[(q, element)] = k
                    else:
                        break
        return transitions
