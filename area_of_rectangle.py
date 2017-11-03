
def areaRectangle(length,breadth):
      '''
      objective: To Compute area of a rectangle 
      input parameters 
      length : length if the rectangle
      breadth: breadth of the rectangle
      approach: multiply length and breadth of the rectangle
      return value : Area of the rectangle
      '''
      area = length * breadth
      return area
    
def main():
    '''
    objective : To compute area of a Rectangle
    user input :
    length: length if the rectangle
    breadth: breadth of the rectangle
    approach:
    '''
    length = int(input())
    breadth= int(input())
    print(areaRectangle(length,breadth))
    print ('End of output')

if __name__ == '__main__': 
     main()
      
 
print('End of program')  
