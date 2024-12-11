def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
   #write your code here
   miles_per_gallon = float(input())
   miles_driven = float(input())
   dollars_per_gallon = float(input())
   driving_cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
   return driving_cost

if __name__ == '__main__':
    #print your costs here like example below
    #print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
   miles_per_gallon = float(input())
   dollars_per_gallon = float(input())

   x1 = (10 / miles_per_gallon) * dollars_per_gallon
   x2 = (50 / miles_per_gallon) * dollars_per_gallon
   x3 = (400 / miles_per_gallon) * dollars_per_gallon

   print(f'{x1:.2f}')
   print(f'{x2:.2f}')
   print(f'{x3:.2f}')