
def areaTriangle(base,height):
      '''
      objective: To Compute area of a Triangle 
      input parameters 
      length :base if the Triangle
      breadth:height of the Triangle
      approach:multiply base and height and 1/2
      return value :Area of the Triangle
      '''
      area = (1/2) * base * height
      return area
    
def main():
    '''
    objective : To compute area of a Rectangle
    user input :
    base: length if the Triangle
    height: breadth of the Triangle
    approach:
    '''
    base =int(input("enter base of Triangle "))
    height=int(input("enter height of Triangle "))
    print ("base of triangle : ",base)
    print ("height of Triangle : ",height)
    print ('id(base) ', id(base) )
    print ('id(height) ', id(height))
    print ('areaTriangle : ' ,areaTriangle(base,height))
    print ('End of output')

if __name__ == '__main__': 
     main()
      
 
print('End of program')    
    
    
    
