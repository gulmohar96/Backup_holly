# f = 100
# w = 100
# s = 100
# for global_time in range(1,1000):
#     print('current global time',global_time)
#     print('f before f -1',f)
#     f = f - 1
#     print('f after f-1',f)
#     if f < 80:
#         print('f after condition check',f)
#         #oven
#         #global_time  = global_time + 10
#         print('current global time, after condition check',global_time)
#
#         #for oven_use_time in range(0,new_global_time):
#         f = f + 60
#         s = s - 5
#         w = w - 5
#
#         #print('f',f,'w',w,'s',s)
#         if f > 100:
#             f = 100
#
#
#         new_global_time = global_time + 20
#         print('new_global_time',new_global_time)
#         break
# print('f',f,'w',w,'s',s)
# for global_time in range(new_global_time + 1 ,1000):
#     print('new timer',global_time)
#
#
#         #print(global_time)
#     #print(global_time)f = 100
# w = 100
# s = 100
# for global_time in range(1,1000):
#     print('current global time',global_time)
#     print('f before f -1',f)
#     f = f - 1
#     print('f after f-1',f)
#     if f < 80:
#         print('f after condition check',f)
#         #oven
#         #global_time  = global_time + 10
#         print('current global time, after condition check',global_time)
#
#         #for oven_use_time in range(0,new_global_time):
#         f = f + 60
#         s = s - 5
#         w = w - 5
#
#         #print('f',f,'w',w,'s',s)
#         if f > 100:
#             f = 100
#
#
#         new_global_time = global_time + 20
#         print('new_global_time',new_global_time)
#         break
# print('f',f,'w',w,'s',s)
# for global_time in range(new_global_time + 1 ,1000):
#     print('new timer',global_time)
#
#
#         #print(global_time)
#     #print(global_time)

##____________TEST 2__________##

# Initial Fuel Levels
food = 100
water = 100
sleep = 100
nap_hours = []

# Time steps of teh day, also controls th  speed of the simulation
day_time = range(1, 8600);  # FIX WITH TIME STEPS IN NUMPY


for global_time in day_time:
    #print('current time', global_time)
    food -= 1
    water -= 1
    sleep -= 1

##_________FORCED ROUTINE_________##

#Sleep

    if global_time < 361: #Morning nap 12 am to 6 am
        nap_hours.append(global_time)

print(len(nap_hours))
print(nap_hours)


for i in range(1,10):
    print('woo')
