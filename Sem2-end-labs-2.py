# author: LM (AMDG) 1/19/22
#sort Numbers
def solution(nums):# naming function
    return sorted(nums or []) #using sort function which sorts numbers in place

solution([1, 2, 4, 5, 6, 8, 7, 3] == [1, 2, 3, 4, 5, 6, 7, 8])