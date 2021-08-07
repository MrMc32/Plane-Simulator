import turtle, random

WinX = int(input("Resolution of the screen on X: "))
WinY = int(input("Resolution of the screen on Y: "))
List_Of_Airports = []
List_Of_Planes = []
Active_Routes = []
List_Of_Positions = []
Speed = 0.1
HowManyPlanesToSpawn = 1

class Program:
	def __init__(self):
		self.main()

	def main(self):
		global HowManyPlanesToSpawn
		self.CreateWindow(WinX, WinY)
		self.CreateAirports(int(input("How many airports: ")))
		for Airport in List_Of_Airports:
			HowManyPlanesToSpawn += 1
		self.UpdateWindow()

	def MoveMultiplePlanes(self):
		global Speed
		IDE = 0
		for Plane in List_Of_Planes:
			Plane.forward(Speed)
			self.CheckArrival(IDE)
			IDE += 1

	def UpdateSpeed(self):
		global Speed
		HowManyPlanes = int(len(List_Of_Planes))
		Speed = 0.1 * HowManyPlanes

	def CheckArrival(self, ID):
		Plane = List_Of_Planes[ID]
		Positions = List_Of_Positions[ID]
		PosX = Positions[0]
		PosY = Positions[1]
		if Plane.distance(PosX, PosY) <= 2:
			List_Of_Planes.pop(ID)
			List_Of_Positions.pop(ID)
			Plane.hideturtle()

	def PreparePlane(self, PosX, PosY, ID):
		Plane = List_Of_Planes[ID]
		Plane.setheading(Plane.towards(PosX, PosY))
		List_Of_Positions.append([PosX, PosY])

	def CreatePlane(self, PosX, PosY):
		Plane = turtle.Turtle()
		Plane.hideturtle()
		Plane.color("white")
		Plane.shapesize(1.2, 1)
		Plane.pencolor("black")
		Plane.pensize(4)
		Plane.penup()
		Plane.goto(PosX, PosY)
		Plane.showturtle()
		Plane.pendown()
		List_Of_Planes.append(Plane)

	def CreateRoute(self):
		Route = turtle.Turtle()
		Route.hideturtle()
		Route.penup()
		Route.color("red")
		Airport_Start = random.randint(0, len(List_Of_Airports) -1)
		Airport_End = random.randint(0, len(List_Of_Airports)-1)
		while Airport_Start == Airport_End:
			Airport_Start = random.randint(0, len(List_Of_Airports)-1)
			Airport_End = random.randint(0, len(List_Of_Airports)-1)
		Airport_Start = List_Of_Airports[Airport_Start]
		Airport_End = List_Of_Airports[Airport_End]
		Route.goto(Airport_Start.xcor(), Airport_Start.ycor())
		Route.pensize(1.5)
		Route.pendown()
		Route.setheading(Route.towards(Airport_End.xcor(), Airport_End.ycor()))
		Route.forward(Route.distance(Airport_End.xcor(), Airport_End.ycor()))
		Active_Routes.append([Airport_Start, Airport_End])

	def CreateAirports(self, HowMany):
		for i in range(HowMany):
			Random_LocationX = random.randint(-WinX/2, WinX/2)
			Random_LocationY = random.randint(-WinY/2, WinY/2)
			for Airport in List_Of_Airports:
				if Airport.distance(Random_LocationX, Random_LocationY) <= 200:
					while Airport.distance(Random_LocationX, Random_LocationY) <= 200:
						Random_LocationX = random.randint(-WinX/2, WinX/2)
						Random_LocationY = random.randint(-WinY/2, WinY/2)
			self.CreateAirport(Random_LocationX, Random_LocationY)

	def CreateAirport(self, PosX, PosY):
		Airport = turtle.Turtle()
		Airport.hideturtle()
		Airport.penup()
		Airport.color("midnight blue")
		Airport.setheading(Airport.towards(PosX, PosY))
		Airport.forward(Airport.distance(PosX, PosY))
		Airport.shape("circle")
		Airport.shapesize(2, 2)
		Airport.showturtle()
		List_Of_Airports.append(Airport)

	def CreateWindow(self, SizeX, SizeY):
		Screen = turtle.Screen()
		Screen.setup(SizeX, SizeY)
		Screen.bgcolor("black")

	def UpdateWindow(self):
		global Finished_Routes
		while True:
			AIE = 0
			Chance = random.randint(int(-500/HowManyPlanesToSpawn), int(500/HowManyPlanesToSpawn))
			if Chance == 0:
				self.CreateRoute()
				ID = int(len(Active_Routes) - 1)
				Route = Active_Routes[ID]
				Airport_Start = Route[0]
				Airport_End = Route[1]
				self.CreatePlane(Airport_Start.xcor(), Airport_Start.ycor())
				self.PreparePlane(Airport_End.xcor(), Airport_End.ycor(), len(List_Of_Planes)-1)
				self.UpdateSpeed()
			self.MoveMultiplePlanes()
			for Plane in List_Of_Planes:
				self.CheckArrival(AIE)
				AIE += 1
			turtle.Screen().update()

if __name__ == "__main__":
	Program()