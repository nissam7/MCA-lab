color_names=input("Enter comma-seperated color names:")
colors=color_names.split(",")
colors=[color.strip() for color in colors]
if len(colors)>=2:
	print("first color:",colors[0])
	print("last color:",colors[-1])
else:
	print("please enter at least two color names.")

