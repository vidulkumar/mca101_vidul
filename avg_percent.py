def result(hindi,english,maths,science,maximum):
    '''
    objective : calculate percentage and average
    approach  : by using mats operators
    input     : hindi,english,maths,science,maximum passed by main()
    '''
    total = int(hindi+english+maths+science)
    avg   = total/4
    percent = total/maximum*100
    print('average of marks is ',avg)
    print('percentage of marks is ',percent,'%')
     
def main():
    '''
    objective : To calculate percentage of marks and avg
    user input : maximum marks , marks in hindi , Eng , math , sci
    approach: by calling result function
    '''
    hindi = int(input('marks in hindi'))
    english = int(input('marks in english'))
    maths = int(input('marks in maths'))
    science = int(input('marks in science'))
    maximum = int(input('maximum marks '))
    result(hindi,english,maths,science,maximum)
if __name__ == '__main__': 
     main()

