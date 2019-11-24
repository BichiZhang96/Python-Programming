#question 1, convert the Celsius temperature to the corresponding Fahrenheit temperture
print ("Please enter a Celsius temperature : ")
celsius_tem = input()  #get the Celsius temperature
celsius_tem = float(celsius_tem ) #change the input into a float number rather than a list
fahrenheit_tem = 1.8 * celsius_tem + 32 #convert the Celsius temperature to the corresponding Fahrenheit temperture
print ("The corresponding fahrenheit temperature is :" , fahrenheit_tem)

#question 2, show the total wholesale cost for 40 copies
num = input ("Please input the number of copies : ")
num = int (num)
cover_price = 25 #the cover price of a book
discount = 0.1 #the discount of the book
ship_cost1 = 2 * 5 #the shipping cost for the first five copies
ship_cost2 = 2.75 * (num - 5) #the shipping cost for all rest of copies
total_price = cover_price *(1 - discount) * num + ship_cost1 + ship_cost2 #get the total cost of 40 copies
print ("The total wholesale cost for 40 copies is : " , total_price)

#question 3, show the time I get home for breakfast
start_time = [7 , 32 , 0] #store the start time in a list
speed1 = [0 , 8 , 15] #store the speed in a list
speed2 = [0 , 7 , 12] #store the speed in a list
arrive_time = [ start_time [i] + speed1 [i] * 1 + speed2 [i] * 3 for i in range(0,len(start_time))] #calculate the result of adding three lists
arrive_time [1] = arrive_time [1] + arrive_time [2] //60 #get the correct minute for second
arrive_time [2] = arrive_time [2] % 60 #get the correct second
arrive_time [0] = arrive_time [0] + arrive_time [1] //60 #get the correct hour
arrive_time [1] = arrive_time [1] % 60 #get the correct minute
print ( "The arriving time is : " , arrive_time [0] ,"hh:" , arrive_time [1] , "min:" , arrive_time [2] , "sec")

#question 4, show the average pace and average speed in miles per hour
distance_kilo = 10 #the distance in kilometer
distance_mile = distance_kilo * 0.6213712 #convert the distance to mile
time = [ 1 , 5 , 42] #store the time in a list
time_hour = time [0]  + time [1] / 60 + time [2] / 3600 #express time in hours
time_minute = time [0] *60 + time [1]  + time [2] / 60 #express time in minutes
average_pace = time_minute / distance_mile #calculate the average pace in minutes
average_pace = [ average_pace//1 , average_pace % 1 * 60] #calculate the seconds
average_speed = distance_mile / time_hour #calculate the average speed
print ("The average pace is : " , average_pace [0] , "minutes" , average_pace [1] , "seconds per mile." )
print ("The average speed is : " , average_speed , " miles per hour")
