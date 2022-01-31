class Sol(object):
    def numUniqueEmails(self,emails):
        updated_emails=[]
        for email in emails:
            index_of_at=email.find('@')
            if index_of_at==-1:
                continue

            loc,dom=email[0:index_of_at],email[index_of_at+1:]
            index_of_plus=email.find('+')
            if index_of_plus != -1:
                loc=email[0:index_of_plus]
            loc="".join(list(filter(lambda a: a != '.', loc)))
            updated_emails.append(loc+dom)
        return (len(set(updated_emails)))

if __name__ == '__main__':
    p = Sol()
    print(p.numUniqueEmails(emails = ["a","test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
