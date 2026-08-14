class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split("@")

            if "+" in local:
                local = local[:local.index("+")]
            local = local.replace(".","")

            actualmail = local +"@" + domain
            unique.add(actualmail)
        return len(unique)       

