# wrong

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        stack = {}
        for i in range(len(emails)):
            for j in range(len(emails[i])):
                # print(input[i][j])
                # print(input[i])
                # print(input[i][j])
                if emails[i][j] == '.':
                    stack['.'] = j
                elif emails[i][j] == '+':
                    stack['+'] = j
                elif emails[i][j] == '@':
                    stack['@'] = j
                
                if stack['+'] < stack['@']:

                print(stack)
            print("")
        return 

input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
obj = Solution()
print(obj.numUniqueEmails(input))