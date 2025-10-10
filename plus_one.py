class Solution(object):
    def plusOne(self, digits):
        mylist = []
        mystr = ""

        for i in digits:
            mystr = mystr + str(i)

        for item in str(int(mystr) + 1):
            mylist.append(int(item))
        
        return mylist