def YesNo(answer):  #Allows the user to enter 'y', 'Y', or and case of 'yes' to return a 'Y' other wise returns 'N'
	if (answer.upper() == "Y") | (answer.upper() == "YES"):
		return "Y"
	else:
		return "N"

def WakeUp():  #This is the first third of the story
	print "It is a brisk, early morning.  The dew is dripping from the needles on the readwoods pittering on your tent.  Your eyes slowly blink open.  You are smelling the most wonderful mountain breakfast being made.  You mother asks if you want to eat or sleep in a while."
	answer = raw_input("Would you like to sleep in?  (y/n)")
	if YesNo(answer) == "Y":
		SleepIn()
	else:
		EatBreakfast()
	MorningActivity()
	
def SleepIn():  #Case: I slept in
	print
	print "Sleeping is a very important part of a young persons life.  You can eat anytime but precious moments in the morning only come once a day.  You fall back into a pleasant slumber only to be woken up once more by the howelling of your dad.  It's something about hiking..."

def EatBreakfast():  #Case:  I chose to eat Breakfast
	print
	print "You have wisely decided to get out of the bag and start your day.  Your father is sitting by the fire eating the most delicious looking plate. (You wonder if it really tastes as good as it looks)  Your sister is getting a cup of hot cocco.  She just put the marshmallows in.  You head over to make your plate of food but you mom has already made you a plate.  You are in luck.  Breakfast is even better than it looks."
	
def MorningActivity():  #This is the second choice in the story
	print
	print "(Loudly)  \"Time to take a hike!\"  This could be just the thing to make the best day ever.  Of course, who knows what's actually out there.  You could trip on a log, get bitten by a mosquito, eaten by a bear, who knows what could happen?  \"Don't be such a little scardy cat.  Your sister is practacly at the trail head by now.  Are you going or not?"
	answer = raw_input("Would you like to go hiking?  (y/n)")
	if YesNo(answer) == "Y":
		GoHiking()
	else:
		CleanCamp()
	AfternoonActivity()
		
def GoHiking():  #Case:  I chose to go hiking
	print
	print "You have decided to hit the trail with your dad and sister.  It is good to get out and stretch your legs.  You breath in the fresh mountain air.  The trail is shaded by the biggest trees you've ever seen.  As you hike along and the sun starts to rise, it starts to get warmer and warmer.  Just when everybody is about to call it quits and head back, you spot a small creek.  Everybody jumps in and has the most fabulous time.  Since the hike was mostly up hill, the hike back is a piece of cake.  As soon as you clear the woods into the campground, you see that lunch is already prepared."

def CleanCamp():  #Case:  I chose not to go hiking.
	print
	print "HIKING!?!?!?  You hate hiking!  There is no way you would ever set foot on a dirty, nasty, hot and sweaty hiking trail.  \"No, you guys go on without me.  I'll be OK.\"  You dad replies \"No problem.  We'll be back by lunch.  Have a great morning.\"  You are lucky you dodged that bullet.  The last time you were practically forced down that dusty trail of tears.  \"Hey honey, since you're not going on a hike today, would you mind helping clean up the camp site with me?\" calls out your mom.  How can you possibly tell her no?  You spend your morning cleaning camp and preping lunch.  Just as you finish making lunch, you see your dad and sister coming back from their hike.  They really look like they could use some refreshment.  You made a great choice."

def AfternoonActivity():  #This is the last decision
	print
	print "Lunch is wonderful after so much activity this morning.  You eat like you haven't had breakfast this morning.  After lunch everybody kicks back and enjoys the cool afternoon breeze that blows through the campground.  Your sister asks you dad if he thinks the fish are biting.  He replies that \"There's only one way to find out!  Grab your poles.  Let's go!\""
	answer = raw_input("Do you want to go fishing?  (y/n)")
	if YesNo(answer) == "Y":
		GoFishing()
	else:
		ReadBook()
	GoToBed()

def GoFishing():  #Case:  I choose to go fishing
	print
	print "\"Fishing sounds like a lot of fun\" you say.  You grab your pole and head down to the lake with your family.  You cast into the lake and wait a little while.  Oh lookie there, you got a bite.  Your whole family does so well, it looks like we're having a fish dinner tonight."

def ReadBook():  #Case:  I chose not to go fishing
	print
	print "You never liked fish anyway.  You would much rather read a good book.  So, that's exactly what you did.  Hopefully the rest of your family will be able to catch dinner tonight."
	
def GoToBed():  #This finilizes the program
	print
	print "Dinner never tasted so good.  After dinner everybody spent some time around a roaring campfire.  What a wonderfuld day.  Too bad we leave for reality tomorrow.  Oh well, we have one more night under the stars to enjoy."
		

WakeUp() #Initilized the running of the program