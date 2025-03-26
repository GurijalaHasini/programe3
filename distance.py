import math

def cal_dist(x1,y1,x2,y2):
    """
    cal dist btw two points (x1,y1) and (x2,y2)
    :x1:x-coordinate of first point(float or int)
    :x2:x-coordinate of second point (float or int)
    :y1:y-coordinate of first point(float or int)
    :y2:y-coordinate of second point (float or int)
    """
    dist=math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist

a1=float(input("enter the value of x-coordinate"))
a2=float(input("enter the value of x-coordinate"))
b1=float(input("enter the value of y-coordinate"))
b2=float(input("enter the value of y-coordinate"))

res=cal_dist(a1,b1,a2,b2)
print(f"The distance is {res:.2f}")
