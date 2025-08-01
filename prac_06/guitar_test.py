"""
CP1404/CP5632 Practical - Guitar test
Estimate: 25 minutes
Actual time: 30 minutes
"""

from prac_06.guitar import Guitar

# Test data
guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2 = Guitar("Another Guitar", 2013, 765.40)

# Expected age calculations (based on 2022)
print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

# Expected vintage status
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")
