def findMax(array):
    max = array[0] # max ham qochonki if shart bajarilsa o'zgaradi 
    max_index = 0   # bu index if shaertr bajarilsa o'zgaradi 
    for n in range(1,len(array)):
        if array[n]>max:
            max = array[n]
            max_index = n
    return max_index

def selectSort(array):
    newArray = []
    for n in range(len(array)): 
        max_index = findMax(array)
        newArray.append(array.pop(max_index))
    return newArray

if __name__ == '__main__':
    array = [3, 4, 1, 6, 10, 20, 9, 8, 21,19]
    newArray = selectSort(array)
    print(newArray)


while True:
     try:
         
        x = int(input("Please enter a number: "))
        break
    
     except ValueError:
         
       print("Oops!  That was no valid number.  Try again...")    



