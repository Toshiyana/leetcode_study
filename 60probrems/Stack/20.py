class Solution:
    def isValid(self, s: str) -> bool:
      if len(s)%2 != 0:
        return False

      dic = {'(':')','{':'}','[':']'}
      stack = list()

      for i, c in enumerate(s):
        # print(i, c)
        if s[i] in dic: # verify only left-bracket
          stack.append(s[i]) # add only left-bracket
          # print('a')
        else:
          # print('b')
          if len(stack) != 0 and dic[stack[-1]] == s[i]:
            stack.pop() # remove a last element
          else:
            return False

          print(stack)

      if len(stack) == 0:
        return True

#s = '()[]{}'
s = '([)]{}'
# s = '([]){}'


# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s)%2!=0:
#             return False
        
#         stack = list()

#         dic = {'(':')','{':'}','[':']'}
        
#         for i, c in enumerate(s):
#             if s[i] in dic:
#                 stack.append(s[i])
#             else:
#                 if len(stack)!=0 and dic[stack[-1]] == s[i]:
#                     stack.pop()
#                 else:
#                     return False
#         if stack:
#             return False
#         else:
#             return True