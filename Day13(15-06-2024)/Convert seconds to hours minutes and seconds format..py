#Convert seconds to hours minutes and seconds format.
'''ip:7262 sec
op:2h:1m:2s'''

'''ip:500
op:0h:8m:20s'''

sec=int(input())
h=sec//3600
rsec=sec%3600
m=rsec//60
s=rsec%60
print(f"{h}h:{m}m:{s}s")

#or
def format_time(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return f"{hours}h:{minutes}m:{seconds}s"

print(format_time(int(input())))  #i/p:7262 o/p:2h:1m:2s
