#area cal and cal how much use paint
import math
input_h_user = float(input("Enter hight: "))
input_w_user = float(input("Enter whight: "))
input_c_user = float(input("Enter covrage: "))

def paint_cal(h,w,c):
    area = h*w
    paint = math.ceil(area/c)
    print(f"Need number of paint cans is {paint}")
paint_cal(input_h_user,input_w_user, input_c_user)    

