# Question 1
# Question Statement: Given a rectangular area R = [-4,4] x [-4,4] in the XY-plane, and a circle x^2 + y^2 = 4^2, find -
# i) All points that lies inside the circle
# ii) All points that lies outside the circle but inside R. 
# iii) All points that lies on the circle

def main():
    points = [[x,y] for x in range(-4,5) for y in range(-4,5)]
    radius_squared = 4**2
    inside_circle = []
    outside_circle = []
    on_circle = []
    for point in points:
        if function(point[0],point[1]) > radius_squared:
            outside_circle.append(point)
        elif function(point[0],point[1]) < radius_squared:
            inside_circle.append(point)
        else:
            on_circle.append(point)

    print(f"The integer points inside the circle are: {inside_circle}")
    print(f"The integer points outside the circle are: {outside_circle}")
    print(f"The integer points on the circle are:{on_circle}")

def function(x: float,y: float) -> float:
    f_val = x**2 + y**2
    return f_val

if __name__ == "__main__":
    main()