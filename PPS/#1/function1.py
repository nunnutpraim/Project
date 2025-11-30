def areaFn(w,h):
    return w*h

def volFn(w,h,l):
    return w*h*l

width = 12.5
height = 8.2
lenght = 10

area = areaFn(width,height)
print("Area = %7.2f square u."%area) #%7.2f = เลข 7 หลัก ทศนิยม 2 ตำแหน่ง %คือให้เห็นว่าเชื่อมกับอะไรอยู่
vol = volFn(width,height,lenght)
print(vol)