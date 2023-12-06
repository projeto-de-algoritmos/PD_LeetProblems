class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)
        n = len(words)

        def backTrack(start, letter_counter):
          if start == n:
            return 0
            
          ans = 0
          for i in range (start,n):
              temp_counter = copy.deepcopy(letter_counter)
              word = words[i]
              word_score = 0
              isValid = True

              for c in word:
                  if c in temp_counter and temp_counter[c] > 0:
                      temp_counter[c] -= 1
                      word_score += score[ord(c) - ord('a')]
                  else:
                      isValid = False
                      break
          
              if isValid:
                  ans = max(ans,backTrack(i+1, temp_counter) + word_score)
          return ans
        return backTrack(0,counter)