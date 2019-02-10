# coding=utf-8 
# @Time :2019/2/10 11:13

from MyQR import myqr

myqr.run(
    words='http://www.4399.com',
    picture='Sources/sinister_smile.png',
    save_name='artistic.png',
    colorized=True,
)

myqr.run(
    words='http://www.7k7k.com',
    picture='Sources/gakki.gif',
    colorized=True,
    save_name='Animated.gif'
)