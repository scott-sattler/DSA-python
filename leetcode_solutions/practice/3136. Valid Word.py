class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        for e in '@#$':
            if e in word:
                return False

        for e in 'aeiou':
            if e in word.lower():
                break
        else:
            return False

        for e in word.lower():
            if e.isalpha() and e not in 'aeiou':
                break
        else:
            return False

        return True
