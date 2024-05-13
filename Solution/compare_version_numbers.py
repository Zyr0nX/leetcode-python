class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        revisions1 = version1.split(".")
        revisions2 = version2.split(".")

        p1 = 0
        p2 = 0

        while p1 < len(revisions1) and p2 < len(revisions2):
            if int(revisions1[p1]) < int(revisions2[p2]):
                return -1
            elif int(revisions1[p1]) > int(revisions2[p2]):
                return 1
            else:
                p1 += 1
                p2 += 1
        
        while p1 < len(revisions1):
            if int(revisions1[p1]) > 0:
                return 1
            p1 += 1
        
        while p2 < len(revisions2):
            if int(revisions2[p2]) > 0:
                return -1
            p2 += 1

        return 0