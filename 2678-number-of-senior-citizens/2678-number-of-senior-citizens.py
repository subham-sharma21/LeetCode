class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
       
        for entry in details:
            if len(entry) == 15:
                if((int(entry[11]) * 10 + int(entry[12]))>60): # age>:
                    count += 1
        return count   
                

        