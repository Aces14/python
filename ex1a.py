from turtle import *
color('hot pink', 'light blue')
begin_fill()
while True:
    forward(200)
    left(160)
    if abs(pos()) < 1:
        break
end_fill()
done()
