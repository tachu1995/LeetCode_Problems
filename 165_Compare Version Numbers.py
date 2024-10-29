class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        result = 0
        list_1 = version1.split(".")
        list_2 = version2.split(".")

        for i in range(max(len(list_1),len(list_2))):
            try: 
                num_1 = int(list_1[i])
            except:
                num_1 = 0
            try:
                num_2 = int(list_2[i])
            except:
                num_2 = 0
            
            result =  num_1 - num_2
            if result < 0: 
                return -1 
            elif result > 0: 
                return 1
        return result 
