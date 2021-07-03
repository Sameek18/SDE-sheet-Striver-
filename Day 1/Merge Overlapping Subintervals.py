#brute force approach

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #sort the list
    intervals.sort(key=lambda x:x[0])
    i=0
    while i<len(intervals)-1:
        #check if second interval lies in the first interval
        if intervals[i][1]>=intervals[i+1][0]:
            intervals[i]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]
            intervals.pop(i+1)

        else:
            i+=1

    return intervals



            
        
