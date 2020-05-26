"""
Every true traveler must know how to do 3 things: fix the fire, find the water
and extract useful information from the nature around him. Programming won't help
you with the fire and water, but when it comes to the information extraction - it
might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time
of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds
to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means
that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle
is 180 degrees. If the input will be the time of the night (before 6:00 AM or
after 6:00 PM), your function should return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.
"""

from datetime import timedelta

def sun_angle(time):
    (h,m) = time.split(':')
    if '06:00' <= time <= '18:00':
        delta_sec = (timedelta(hours=int(h), minutes=int(m)) \
                     - timedelta(hours=6,minutes=0)).seconds
        delta_min = delta_sec//60
        angle = 0.25*delta_min      # 180° -- 720min
        return round(angle,2)
    else:
        return "I don't see the sun!"

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
