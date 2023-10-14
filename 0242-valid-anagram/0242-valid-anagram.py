class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)

        s_list.sort()
        t_list.sort()

        print(s_list)
        print(t_list)

        count = 0
        

        while len(s_list) == len(t_list):
            for i in range(len(s_list)):
                if s_list[i] == t_list[i]:
                    i+=1
                    # return True
                else:
                    return False
            return True

        