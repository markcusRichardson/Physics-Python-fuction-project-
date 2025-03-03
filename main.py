# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_and_c(f_temp):
  Temp_c = (f_temp - 32) * 5/9
  return Temp_c

f100_in_celsius = f_and_c(100)

def c_and_f(c_temp):
  Temp_f = c_temp * (9/5) + 32

  return Temp_f

c0_in_fahrenheit = c_and_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)#

print("The GE train supplies " + str(train_force) + " Newtons of foprce")

def get_energy(mass):
  c = 3*10**8
  return c * mass

bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

get_work = lambda mass, acceleration, distance: mass * acceleration * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")