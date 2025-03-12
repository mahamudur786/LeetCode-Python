#3. Longest Substring Without Repeating Characters
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

#Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #non Optimal
        # n = len(s)
        # maxi = 0
        # start = 0  # Start of the sliding window
        # myDict = defaultdict(int)

        # for i in range(n):
        #     myDict[s[i]] += 1
            
        #     # If the character is repeated, move the start of the window
        #     while myDict[s[i]] > 1:
        #         myDict[s[start]] -= 1
        #         start += 1

        #     # Update the result for the maximum length of the substring without repeating characters
        #     maxi = max(maxi, i - start + 1)

        # return maxi

        ##This is optimal
        n = len(s)
        maxi = 0
        start = 0  # Start of the sliding window
        char_count = [0] * 128  # Array to track the count of characters (ASCII size)

        for i in range(n):
            # Increment the count of the current character
            char_count[ord(s[i])] += 1
            
            # If the character appears more than once, move the start of the window
            while char_count[ord(s[i])] > 1:
                char_count[ord(s[start])] -= 1
                start += 1

            # Update the result for the maximum length of the substring without repeating characters
            maxi = max(maxi, i - start + 1)

        return maxi
