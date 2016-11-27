import os

cars=os.listdir("cars")
types=os.listdir("type")
tracks=os.listdir("tracks")

f = open('carlist.htm','w')
f.write("""
<html>
	<head>
		<style>
		img
		{
			margin: -32px -64px -16px -64px;
		}
		</style>
	</head>
<body>
""")

newc=oldc=""
count=0
 
for c in cars:
	newc=c[0:3] #car model
	num=c[5:6] #livery number
	
	
	if(newc!=oldc): #if new car, make a car title
		# f.write("</div>")
		# f.write("<div class=\"col-sm-4\"> " )
		f.write("<h2>" +  newc + "</h2>\n")
	# f.write("<h3>Livery " +  num + "</h3>\n") #livery title
	# f.write("""<div class = "crop" >""" )
	f.write("""<img src="cars/""" +  c + """"</img>\n""") #put the car pic in
	# f.write("</div>")
	oldc=newc #variable for if new car
	# count+=1
f.write("</body></html>\n")
f.close()
# dir(a)

----

f = open('tracklist.htm','w')
f.write("""
<html>
	<head>
		<style>
		img
		{
			margin: 0px 128px;
		}
		</style>
	</head>
<body>
""")

newc=oldc=""
count=0
 
for t in tracks:
	# newc=c[0:3] #car model
	# num=c[5:6] #livery number
	
	
	if(newc!=oldc): #if new car, make a car title
		# f.write("</div>")
		# f.write("<div class=\"col-sm-4\"> " )
		f.write("<h2>" +  newc + "</h2>\n")
	# f.write("<h3>Livery " +  num + "</h3>\n") #livery title
	# f.write("""<div class = "crop" >""" )
	f.write("""<img src="cars/""" +  c + """"</img>\n""") #put the car pic in
	# f.write("</div>")
	oldc=newc #variable for if new car
	# count+=1
f.write("</body></html>\n")
f.close()

---
"""
Car comments
207 I think a pure grey/silver/whiet suits the car best, similar with the 307.
the 55 impreza looks best with t he classic blue + magenta highlits
att should be silver/grey
aqp is missing the classic quattro livery (white + yellow/silver highlights)
cc2 all liveriues look ok, but i prefer the red/ywllow one
cc4 teh red & white lievryioes look ok, perha[s the red 1 is better
cli the cliio looks best with yellow, but white is fine too 
cor similar ^, but yellow, or wite, but not both
cr34 best with disctincietv red lievry
exige, since its lotus, best with a WARM yellow, not cool yellow 
new stratos best with classical lancia colors (green/red on top ofo white)
gt4 i'm glad they have the classic (green/red on top ofo white) for this
me9 1st livery is best, but mb it could be better. cool colors dont really suit the evo, cuz the mitsubisih logo is red. dseems they were ghving fun with the plates.
n12, blue+green livery exists, but not t=withj the districntive crux star pattern. Recall the US cover has the gold subaru on the front (with less logos). Was that cover made 1st, or the gold livery?
pajeros should be mainlly red. the green highlights on 1 livery mkes it looks like a stratos
rdw like the logo, car shoulc be green. redf doesn't fit
 suzuki swift should be yellow, just like those car ads
 lacia stratos has red & green livery, but not quite in the classic shape
 
 tacoma 1st yellow lovery looks ok ispz
 toureg should be blue, like the red bulill videos
 triton like pajero, should be red
 xsara should be red, but it looks different ot the cover of the CMR04 gAme what hppened to mah lights?
"""