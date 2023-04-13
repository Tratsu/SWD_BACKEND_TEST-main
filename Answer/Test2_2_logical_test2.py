#
#Convert Arabic Number to Roman Number.
#เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
#โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000
#
#*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
#ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).
#
def toRoman(number):
    romanRef = {
        1000    : 'M'   ,
         900    : 'CM'  , 500   : 'D', 400  : 'CD', 100 : 'C', 
          90    : 'XC'  ,  50   : 'L',  40  : 'XL',  10 : 'X',
           9    : 'IX'  ,   5   : 'V',   4  : 'IV',   1 : 'I'
    }
    
    romanText = ''
#REMOVE & ADD
    for arabic, roman in romanRef.items():
        while number    >= arabic:      #Keep doing until can't
            number      -= arabic       #Take value out equal to raman value that going to be add
            romanText   += roman        #Add roman number to text variable
           
    return romanText
#Main loop
while(1):
    num = int(input('Number from 0 to 1000 >> '))
    #Legal input ?
    if num > 1000 | num < 0:
        break
    print(toRoman(num))