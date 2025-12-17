import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])

arr1 = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])

word = arr1[0,0,0]+arr1[2,0,0]+arr1[2,0,0]

print(word)

mat = np.arange(1,10).reshape(3,3)
print(mat)

arr2 = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])

print(arr2[1,1])
print(arr2[-1])
print(arr2[:,:2])
arr2[0,2]=300
print(arr2)
print(arr2[2,1])
print(arr2[:,1])