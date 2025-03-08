#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: march 4 2025
# This program calculates and displays the surface
# area and volume of a pentagon prism
# Get input needed
print(
    "Welcome!, this program calculates the surface area and volume"
    "of a pentagonal prism. Please enter the required values below"
)
b = float(input("Enter the side length of the pentagonal base (b): "))
a = float(input("Enter the apothem of the pentagonal base (a): "))
h = float(input("Enter the height of the prism (h): "))

# Calculate Surface Area with formula
surface_area = (5 / 2) * a * b + 5 * b * h

# Calculate Volume with formula
volume = (5 / 2) * a * b * h

# Display results
print("\nHere We Have Our Results!")
print(f"Surface Area: {surface_area:.2f} square units")
print(f"Volume: {volume:.2f} cubic units")
