class Solution:
    def maxDiff(self, num: int) -> int:
        #num = 123456
        #num = 9288

        lst = list(str(num))

        x = lst[0]
        other_x = 0
        flag = False

        a = []
        b = []

        j = 0
        a_x = 0
        flag_a = False
        if x == '9':
            while j < len(lst) and lst[j] == '9':
                j += 1
            if j < len(lst):
                a_x = lst[j]
                flag_a = True
                


        j = 0
        if x == '1':
            while j < len(lst) and (lst[j] == '0' or lst[j] == '1'):
                j += 1
            if j < len(lst):
                other_x = lst[j]
                flag = True


        i = 0
        while i < len(lst):
            if lst[i] == x:
                a.append('9')
            
            elif lst[i] == a_x:
                a.append('9')
            
            else:
                a.append(lst[i])
            
            if flag == True and lst[i] == other_x:
                b.append('0')
            
            elif int(x) >= 1 and lst[i] == x:
                b.append('1')
            
            else:
                b.append(lst[i])
            
            i += 1

        print(int(''.join(a)), " here is mx")
        print(int(''.join(b)), " here is mn")

        mx_diff = int(''.join(a)) - int(''.join(b))

        return mx_diff
                