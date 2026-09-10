
print("Hello")
# My first Python program
# This prints a personal introduction

print("=" * 40)  # Prints a line of 40 equal signs
print("Personal Introduction")
print("=" * 40)
# personal details stored as variables 
first_name = "Maria"
last_name = "Rodriguez"
age = 30
city = "New York"
favorite_language = "Python"
occupation = "AI Software Engineer" # added little extra information
# Display the introduction 
print("Name:" , first_name, last_name)
print("Age:" , age)
print("City:" , city)
print("Favorite Language:" , favorite_language)
print("Occupation:" , occupation) 
print("=" * 40) 
# f-strings let you embed expressions inside string literals, using curly braces {}.
print(f"\n{first_name} {last_name} is a {age}-year-old {occupation} from {city}.")
print(f"Her favorite programming language is {favorite_language}.")