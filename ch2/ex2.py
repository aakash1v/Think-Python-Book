"""
Practice using the Python interpreter as a calculator:
1. The volume of a sphere with radius r is 4/3πr3. What is the volume of a sphere with
radius 5?
>>> r = 5
>>> 4/3 *3.14 *r**2
104.66666666666666

2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
Shipping costs $3 for the first copy and 75 cents for each additional copy. What is
the total wholesale cost for 60 copies?
>>> (24.95*.4)+ (3.75*60)
234.98

3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then
3 miles at tempo (7:12 per mile) and 1 mile at an easy pace again, what time do I
get home for breakfast?
"""
sec =1
min = 60*sec
hour = 60*min
time = 6*hour + 52*min   
time_at_easy_pace = 2*(8*min +15*sec)
time_at_tempo = 3*(7*min + 12*sec)
total_time = time_at_easy_pace+time_at_tempo
finish_min = total_time/60
# print(finish_min)

"6:52 + 38 min"
print("Time at he come for breakfast = ","7:30" )


