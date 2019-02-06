import math

'''def area(base,height):
	""" (number, number) -> number
	prints the area of triangle with given base and height
	>>>area(2,4)
	4.0
	>>area(4,5)
	10
	"""	
	#print("Area of Triangle : ",base * height /2)
        return base * height /2
'''

def peremeter(s1,s2,s3):
	permtr = s1 + s2 + s3;
	return permtr
	#print("Peremeter of triangle :",permtr)

#__name__ = __man__


def semiperemeter(s1,s2,s3):
	return peremeter(s1,s2,s3)/2
	"""
	(number, number, number) -> Floar
	returns the semeperemeter of the triangle with sides of 
	side1, side2 and side3.	
	"""
	"""
        if __name__ == '__main__':
                base = int(input("Please enter the base of triangle\t"))
                height= int(input("Please enter the height of triangle\t"))

                side1=int(input("please enter the side 1"))
                side2=int(input("please enter the side 2"))
                side3=int(input("please enter the side 3"))


                area(base,height)
                peremeter(side1,side2,side3)
                semiperemeter(side1,side2,side3)
	"""

def area_hero(side1, side2, side3):
        
        """
        (number,number,number) ->Float
        Return the area of triangle with sides of length
        side1, side2, side3.

        >>>area_hero(3,4,5)
        6.0
        >>>area_hero(10.5,6,9.3)
        27.731
        """
        semi= semiperemeter(side1, side2, side3)
        area=math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
        return area
        
