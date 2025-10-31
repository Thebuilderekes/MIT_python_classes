## Elysa, ben and cindy are selling tickets
# ben sells 2 fewer than elysa
# cindy sells twice as many as elysa
# 10 total tickets by the three people
# how many did elsysa sell


# 1. Define the total tickets sold
TOTAL_TICKETS = 10

# 2. Set up the equation based on the variables:
# Let E = Tickets Elysa sold
# Ben sold: E - 2
# Cindy sold: 2 * E
# Total: E + (E - 2) + (2 * E) = 10

# 3. Simplify the equation algebraically:
# 4 * E - 2 = 10

# 4. Isolate the term with E:
# 4 * E = 10 + 2
# 4 * E = 12
RHS_Step1 = TOTAL_TICKETS + 2  # The right-hand side (RHS) after adding 2 to both sides

# 5. Solve for E:
# E = 12 / 4
E = RHS_Step1 / 4  # E is the number of tickets Elysa sold

# 6. Convert the result to an integer (although division by 4 yields an integer here)
elysa_tickets = int(E)

# 7. Calculate the tickets for Ben and Cindy for verification
ben_tickets = elysa_tickets - 2
cindy_tickets = 2 * elysa_tickets
total_check = elysa_tickets + ben_tickets + cindy_tickets

print(f"Based on the equation 4E = 12, Elysa sold: {elysa_tickets}")
print(
    f"Verification: {elysa_tickets} (Elysa) + {ben_tickets} (Ben) + {cindy_tickets} (Cindy) = {total_check} tickets total."
)
