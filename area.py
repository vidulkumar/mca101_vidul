import sys
sys.path.append('/home/administrator/desktop/MCA101')
import areaall
'''
objective : compute are of rectangle or triangle or square
            by presenting a menu to user 
approach : by importing file containing required funtion(areaRectangle,areaTriangle,areaSquare)
user inputs : length - length of rectangle
              breadth - breadth of rectangle
                  or
              base - base of triangle
              height- height of triangle
                 or
              side - side of square

output : prints the area of rectangle or triangle or square

'''

              

def main():
    print("-----------menu-------------")
    print('1.compute area of rectangle ')
    print('2.compute area of Triangle ')
    print('3.compute area of square    ')
    choice=int(input('Enter your choice '))
    if(choice==1):
        length = int(input('enter length '))
        breadth= int(input('enter breadth '))
        
        print('area of triangle : ' , areaall.areaRectangle(length,breadth)) 
    elif(choice==2):
        base = int(input('enter base'))
        height = int(input('enter height'))
        print('area of Rectangle : ' , areaall.areaTriangle(base,height))
    elif(choice==3):
        side= int(input('enter side of square '))
        print('area of square : ', areaall.areaSquare(side) )
        
    else :
        print('NO SUCH OPTION')

       

if __name__=='__main__':
    main()
        
