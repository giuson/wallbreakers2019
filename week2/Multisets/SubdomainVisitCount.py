#SUBDOMAIN VISIT COUNT
#https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output=[]
        d = {}
        for i in cpdomains:
            split = i.split(' ') #split count and domain

            domain_split = split[1].split('.')
            domain_len = len(domain_split)
            
            x=0
            for i in range(domain_len):
                domain = '.'.join(domain_split[x:])
                if domain in d:
                    value = d.get(domain)
                    newValue = int(value) + int(split[0])
                    d[domain] = newValue
                else:    
                    d[domain] = split[0]
                x+=1
            
        for k,v in d.items():
            output.append(str(v) + ' ' + str(k))
            
        return output