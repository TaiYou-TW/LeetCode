"""
related topic: array, hash table, string
time complexity: O(n)
space complexity: O(1)

用字串切割方式去切割字串，避免遍歷整串文字。

"""


class Solution:
    def applyRule(self, email: str) -> str:
        return self.applyDotRule(self.applyPlusRule(email))

    def applyDotRule(self, email: str) -> str:
        full_email = email.split("@")
        return full_email[0].replace(".", "") + "@" + full_email[1]

    def applyPlusRule(self, email: str) -> str:
        full_email = email.split("@")
        return full_email[0].split("+", 1)[0] + "@" + full_email[1]

    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            unique_emails.add(self.applyRule(email))
        return len(unique_emails)
