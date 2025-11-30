draw = input().split()
draw_letter, draw_number = draw[0], draw[1]

ticket = input().split()
ticket_letter, ticket_number = ticket[0], ticket[1]

reward = 0

if draw_letter == ticket_letter and draw_number == ticket_number:
    reward = 1000000

elif draw_number == ticket_number and draw_letter != ticket_letter:
    reward = 100000

elif draw_letter == ticket_letter and ticket_number[-3:] == draw_number[-3:]:
    reward = 2000

elif draw_letter == ticket_letter and ticket_number[-2:] == draw_number[-2:]:
    reward = 1000

elif ticket_number[-3:] == draw_number[-3:] and draw_letter != ticket_letter:
    reward = 200

elif ticket_number[-2:] == draw_number[-2:] and draw_letter != ticket_letter:
    reward = 100

elif draw_letter == ticket_letter and draw_number != ticket_number:
    reward = 20

print(reward)
