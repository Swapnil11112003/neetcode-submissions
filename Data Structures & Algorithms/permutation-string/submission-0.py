class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        target_map = Counter(s1)
        
        current_window = Counter(s2[:n1])

        if current_window == target_map:
            return True

        for i in range(n1, n2):
            char_in = s2[i]
            char_out = s2[i - n1]

            current_window[char_in] += 1
            
            if current_window[char_out] == 1:
                del current_window[char_out] 
            else:
                current_window[char_out] -= 1

            if current_window == target_map:
                return True

        return False


        


            


        