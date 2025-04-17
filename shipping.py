weight = 4.8

#Ground Shipping
print("Ground Shipping")
if weight <= 2:
  cost_1 = 1.5 * weight + 20
  print("$" + str(cost_1)) 
elif weight >2 or weight <=6:
  cost_2 = 3*weight+20
  print("$"+str(cost_2))
elif weight > 6 or weight <=10:
  cost_3 = 4*weight + 20
  print("$"+ str(cost_3))
else:
  cost_4 = 4.75 *weight +20
  print("$"+str(cost_4))

#Premium Ground Shipping
cost_ground_premium = 125
print("Ground Shipping Premium")
print("$"+ str(cost_ground_premium))

#Drone Shipping
print("Drone Shipping")
if weight <= 2:
  cost_1 = 4.5 * weight + 0
  print("$" + str(cost_1)) 
elif weight >2 or weight <=6:
  cost_2 = 9.0*weight+0
  print("$"+str(cost_2))
elif weight > 6 or weight <=10:
  cost_3 = 12.0*weight + 0
  print("$"+ str(cost_3))
else:
  cost_4 = 14.25 *weight +0
  print("$"+str(cost_4))
