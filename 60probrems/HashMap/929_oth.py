from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for i in emails:
            local, domain = i.split("@")
            # print(local, domain)
            if "." in local:
                local = local.replace(".","")
            if "+" in local:
                local = local[:local.index("+")]
            seen.add(local + "@" + domain)
        return len(seen)

input = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
obj = Solution()
print(obj.numUniqueEmails(input))