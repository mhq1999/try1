'''question: for a lst a given list find the index of the max value in the lst in a recursive way
with O(logn) Time Complexity'''
def find_max_index(lst,start,end):
    n=end-start+1
    if(n==1):
        return start
    if (n==2):
       if(lst[start]>lst[end]):
           return start
       else:
           return end
    mid=(start+end)//2
    startval=find_max_index(lst,start,mid)
    endval=find_max_index(lst,mid,end)
    if lst[startval]>lst[endval]:
        return startval
    else:
        return endval