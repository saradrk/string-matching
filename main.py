# Sara Derakhshani, 01.02.21
# Programmierung 1: Projekt
# Test: String-Matching-Tool


from string_matcher import StringMatcher


def main(search_pattern, text):
    SM = StringMatcher()
    return SM.match(search_pattern, text)


if __name__ == '__main__':
    print(main('', 'ababc'))