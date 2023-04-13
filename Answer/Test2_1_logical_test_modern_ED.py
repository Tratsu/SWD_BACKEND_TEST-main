def converter(number):  
    #Create array for thai language
    norm    = [
        "", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"
        ]
    deca    = [
        "", "สิบ", "ยี่สิบ", "สามสิบ", "สี่สิบ", "ห้าสิบ", "หกสิบ", "เจ็ดสิบ", "แปดสิบ", "เก้าสิบ"
        ]
    mOver   = [
        "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"
        ]
    
    text = ""
    #Covert in range hundred to million
    for x in range(5, 0, -1):
        temp    =   number // (10 ** ( 1 + x ))
        text    +=  norm[temp] 
        if temp != 0:
            text    +=  mOver[x-1]
        number  %=  (10 ** ( 1 + x ))
    #ED only coming when tens not equal to0
    if number == 1:
        text    +=  norm[1]
        return text
    #Convert the rest    
    temp    =   number // (10)
    text    +=  deca[temp]
    temp    =   number % 10
    #Check for the last 1 // Special case
    if temp != 1:
        text    +=  norm[temp]
    else:   
        text    +=  "เอ็ด"
        
    return text
    
    
while(1):
    num = int(input("Input : ")) # 0 <= input < 10,000,000
    #Legal input ?
    if num < 0 | num >= (10 ** 7): 
        print(" Input must be greater than or equal to 0 and less than 10 million. ")
        break
    if num == 0:
        print("ศูนย์")
    else:
        print(converter(num))
