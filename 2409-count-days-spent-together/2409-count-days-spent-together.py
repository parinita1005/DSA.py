class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice,arriveBob)
        end = min(leaveAlice,leaveBob)

        if start>end:
            return 0

        months = [31,28,31,30,31,30,31,31,30,31,30,31]

        def convert(date):#converts date into its day number in the year. like 16  august for 08-16.

         m,d = map(int,date.split("-"))
        #Suppose date = "08-16".
# - date.split("-") → ["08", "16"]
# - map(int, ...) converts both strings into integers.
# - m = 8 (month)
# - d =  16 (day)
         return sum(months[:m-1])+d
        return convert(end)-convert(start)+1

    
        




       
        