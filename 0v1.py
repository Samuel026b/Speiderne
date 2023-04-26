### Game in development! Why did I start to code when there aren't any clear rules?!



import subprocess
import random
import sys


## Just prepairing for the game.

class Territory:
  def __init__(self, card):
    self.card = card
    self.vis = False

class Expedition:
  def __init__(self, exp, pl, coord):
    self.e = exp
    self.p = pl
    self.c = coord
    self.m = False

class Protest(Exception):
  ...

while True:
  PLAYERS = input("Players: ")
  try:
    int(PLAYERS)
  except ValueError:
    print("Give a value. ")
  else:
    PLAYERS = int(PLAYERS)
    player_value = True
    if PLAYERS > 1:
      break

kastebunke = []

playernames = []
if input("Names (y/n): ") in ("yes", "y", "ye", "es", "s", "e", "ys"):
  for player in range(PLAYERS):
    while True:
      playernames.append(input(f"{player + 1}) "))
      dcheck = []
      DuplicationError = False
      for name in playernames:
        if name.lower() in dcheck:
          DuplicationError = True
          break
        else:
          dcheck.append(name.lower())
      if DuplicationError:
        print("Name already used!")
      else:
        break
else:
  for player in range(PLAYERS):
    playernames.append(f"Player{player + 1}")

main_deck = []
sorts = ["♣", "♠", "♥", "♦"]
values = ["2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "10", "J ", "Q ", "K ", "A "]
def shuffle_cards(cardli):
  x = 0
  y = 0
  while y < len(values):
    cardli.append(sorts[x] + values[y])
    x += 1
    if x == len(sorts):
      x = 0
      y += 1
  random.shuffle(cardli)
shuffle_cards(main_deck)
undiscovered = [["   ", "   ", "   ", "   ", "   ", "   "], ["   "], ["   "], ["   "], ["   ", "   ", "   ", "   ", "   ", "   "]]
y = 1
x = 0
while y < 4:
  card = main_deck.pop(0)
  ter = Territory(card)
  undiscovered[y].append(ter)
  x += 1
  if x > 3:
      undiscovered[y].append("   ")
      y += 1
      x = 0
ch = []
for number in range(5):
  card = main_deck.pop(0)
  ch.append(card)
playerhand = []
for player in range(PLAYERS):
  playerhand.append([])
  for number in range(5):
      card = main_deck.pop(0)
      if main_deck == False:
        shuffle_cards(main_deck)
      playerhand[-1].append(card)

points = []
expeditions = []
for player in playernames:
  points.append([])
  expeditions.append(0)


## The game

def posmos(coordinate):
  down = True
  up = True
  right = True
  left = True
  try:
    if isinstance(undiscovered[int(list(coordinate)[0]) + 1][int(list(coordinate)[1])], Territory) == False and undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) - 1].vis == True:
      down = False
  except IndexError:
    down = False
  except AttributeError:
    down = False
  try:
    if isinstance(undiscovered[int(list(coordinate)[0]) - 1][int(list(coordinate)[1])], Territory) == False and undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) - 1].vis == True:
      up = False
  except IndexError:
    up = False
  except AttributeError:
    up = False
  try:
    if isinstance(undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) + 1], Territory) == False and undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) - 1].vis == True:
        right = False
  except IndexError:
    right = False
  except AttributeError:
    right = False
  try:
    if isinstance(undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) - 1], Territory) == False and undiscovered[int(list(coordinate)[0])][int(list(coordinate)[1]) - 1].vis == True:
        left = False
  except IndexError:
    left = False
  except AttributeError:
    left = False
  if down == False and up == False and right == False and left == False:
    return False
  else:
    return True

expco = []
situation = ""
valid_places = ["01", "02", "03", "04", "10", "20", "30", "15", "25", "35", "41", "42", "43", "44"]
print("It is recommended that your terminal window is at least 30 symbols long. If your terminal is too low, your cards may not hide correctly.")
print('For all possible commands, type "help"')
turn = 0
pastcom = None
while True:
  try:
    movexp = True
    if turn == PLAYERS:
      turn = 0
    if len(main_deck) < 3:
      if kastebunke > 2:
        random.shuffle(kastebunke)
        main_deck.extend(kastebunke)
        kastebunke = []
      else:
        shuffle_cards(main_deck)
    for item in valid_places:
      if not posmos(item):
        valid_places.remove(item)
    for item in expco:
      if item.e == False or not not not not not posmos(item.c):
        undiscovered[int(list(item.c)[0])].pop(int(list(item.c)[1]))
        undiscovered[int(list(item.c)[0])].insert(int(list(item.c)[1]), "   ")
        if situation == "\033[1mpirates\033[0m) ":
          ExpSunk = True
        expco.remove(item)
    command = input(f"{situation}{playernames[turn]} >>> ")
    command = command.lower()
    if pastcom == "md":
      for line in range(len(playerhand[turn]) + 2 + PLAYERS):
        print("\033[A", end="")
        print(" " * 25)
        print("\033[A", end="")
      print(f"{situation}{playernames[turn]} >>> {command}")
    if command in ("quit", "exit"):
      if input("Are you sure you want to quit (y/n)? ") in ("yes", "y", "ye", "es", "s", "e", "ys"):
        sys.exit("Game Interrupted")
    if command == "help":
      print('"md": show your deck and how many cards each opponent has.')
      print('"map": show map.')
      print('"ch": see the cards, where you could choose which one to take.')
      print('"p": show how many points each player has.')
      print('"exp": show information (owner, cards, coordinates) about all expeditions.')
    if command == "md":
      for card in playerhand[turn]:
        print(f"\033[47m\033[30m\033[1m{card}\033[0m ({playerhand[turn].index(card) + 1})")
      print("")
      for player in playernames:
        if playernames.index(player) == turn:
          print(f"{player}: {len(playerhand[turn])} •")
        else:
          print(f"{player}: {len(playerhand[playernames.index(player)])}")
    if command == "map":
      print("   0.  1.  2.  3.  4.  5.")
      i = 0
      while i < 5:
        print(f"{i}.", end=" ")
        for card in undiscovered[i]:
          if isinstance(card, Territory):
            if card.vis == True:
              print(f"\033[47m\033[30m\033[1m{card.card}\033[0m", end=" ")
            else:
              print("\033[47m\033[30m\033[1m?? \033[0m", end=" ")
          else:
            if isinstance(card, Expedition):
              print(f"{len(card.e)}{list(card.e[-1])[0]}", end="  ")
            else:
              print(card, end=" ")
        print("")
        i += 1
    if command == "ch":
      for card in ch:
        print(f"\033[47m\033[30m\033[1m{card}\033[0m", end=" ")
      print("")
      print("(1) (2) (3) (4) (5)")
    if command == "p":
      print(" " * (len(playernames[turn]) + 2), end="")
      i = 1
      for point in points[turn]:
        print(f"({i})", end=" ")
        i += 1
      print("")
      print(f"{playernames[turn]}: ", end="")
      for point in points[turn]:
        print(f"\033[47m\033[30m\033[1m{point}\033[0m", end=" ")
      print("")
      print("")
      for player in playernames:
        if playernames.index(player) == turn:
          ...
        else:
          print(f"{player}: ", end="")
          for point in points[playernames.index(player)]:
            print(f"\033[47m\033[30m\033[1m{point.card}\033[0m", end=" ")
          print("")
    if command == "exp":
      print(expco)
      if expco:
        for exps in expco:
          print("")
          print(f"Owner: {exps.p}")
          print(f'Coordinates: "{exps.c}"')
          print("Cards:")
          for cards in exps.e:
            print(f"\033[47m\033[30m\033[1m{cards}\033[0m ({exps.e.index(cards) + 1})")
        print("")
      else:
        print("No expeditions built yet.")
    if command == "thr":
      if kastebunke:
        for cards in kastebunke:
          print(f"\033[47m\033[30m\033[1m{cards}\033[0m")
      else:
        print("No throwed cards.")
    if command == "sink exp" and situation == "\033[1mstorm\033[0m) ":
      here = undiscovered[int(list(splitcom[0])[0])].pop(int(list(splitcom[0])[1]))
      undiscovered[int(list(splitcom[0])[0])].insert(int(list(splitcom[0])[1]), "   ")
      expco.remove(here)
      situation = ""
    if len(command) >= 8 and len(command) < 11 and not not not situation:
      try:
        cont = True
        splitcom = command.split(" ")
        if len(splitcom) != 4:
          cont = False
        for item in splitcom:
          try:
            int(item)
          except ValueError:
            cont = False
            break
        try:
          if len(splitcom[3]) != 2:
            cont = False
        except ValueError:
          cont = False
        if cont:
          expedition = []
          try:
            i = 0
            expedition.append(playerhand[turn][int(splitcom[i]) - 1])
            while i < 2:
              lsc = list(playerhand[turn][int(splitcom[i]) - 1])[0]
              i += 1
              if lsc != list(playerhand[turn][int(splitcom[i]) - 1])[0]:
                raise Protest()
              else:
                expedition.append(playerhand[turn][int(splitcom[i]) - 1])
          except Protest:
            print("Illegal: sort must be the same as the other cards.")
          else:
            if splitcom[3] in (valid_places):
              if isinstance(undiscovered[int(list(splitcom[3])[0])][int(list(splitcom[3])[1])], Expedition):
                print("Illegal: space occupied")
              else:
                undiscovered[int(list(splitcom[3])[0])].pop(int(list(splitcom[3])[1]))
                undiscovered[int(list(splitcom[3])[0])].insert(int(list(splitcom[3])[1]), Expedition(expedition, playernames[turn], splitcom[3]))
                expco.append(Expedition(expedition, playernames[turn], splitcom[3]))
                playerhand[turn].pop(int(splitcom[0]) - 1)
                playerhand[turn].pop(int(splitcom[1]) - 2)
                playerhand[turn].pop(int(splitcom[2]) - 3)
                turn += 1
                for line in range(600):
                  print("")
                subprocess.call(["mplayer", "Downloads/Pausesignal.mp3"])
                for line in range(600):
                  print("")
            else:
              print("Illegal: expedition must be placed on a valid place.")
      except IndexError:
        ...
    try:
      if situation == "\033[1mstorm\033[0m) ":
        splitresp = command.split(" ")
        i = 0
        tfe = 1
        tfh = 0
        tfp = 0
        while i < 3:
          src0 = list(splitresp[i])
          src0.pop(0)
          src0 = "".join(src0)
          src0 = int(src0)
          if list(splitresp[i])[0] == "e":
            used_card = undiscovered[int(list(splitcom[0])[0])][int(list(splitcom[0])[1])].e.pop(src0 - tfe)
            kastebunke.append(used_card)
            tfe += 1
            cont = True
          else:
            chcv = list(challenge[0])
            chcv.pop(0)
            chcv = "".join(chcv)
            chcv = values.index(chcv)
            if list(splitresp[i])[0] == "h":
              tfh += 1
              used_card = playerhand[turn].pop(src0 - tfh)
            if list(splitresp[i])[0] == "p":
              tfp += 1
              used_card = points[turn].pop(src0 - tfp)
            used_card = list(used_card)
            used_card.pop(0)
            used_card = "".join(used_card)
            used_card = values.index(used_card)
            if used_card > chcv:
              kastebunke.append(challenge[0])
              kastebunke.append(used_card)
              challenge.pop(0)
            else:
              if list(splitresp[i])[0] == "h":
                playerhand[turn].insert(int(src0) - tfh, used_card)
              if list(splitresp[i])[0] == "p":
                points[turn].insert(int(src0) - tfh, used_card)
              print("Illegal: if your card is not from your expedition, the value of your card must be equal or greater than the card you are defending against.")
              cont = False
              break
            cont = True
          i += 1
      else:
        cont = False
    except (IndexError, ValueError):
      cont = False
    if situation == "\033[1mpirates\033[0m) ":
      try:
        if ExpSunk:
          source = playerhand[turn]
        else:
          source = undiscovered[int(list(splitcom[0])[0])][int(list(splitcom[0])[1])].e
        i = int(command)
        response.append(values.index("".join(list(source.pop(i - 1))[1:])))
        chcv = values.index("".join(list(challenge[0])[1:]))
        if sum(response) > chcv:
          situation = ""
          if not ExpSunk:
            cont = True
      except (IndexError, ValueError):
        cont = False
    if (len(command) == 5 and (list(command).count("-") == 1 or list(command).count(" ") == 1)) and bool(situation) == False and movexp == True:
      if list(command).count(" ") == 1:
        splitcom = command.split(" ")
      if list(command).count("-") == 1:
        splitcom = command.split("-")
      if (int(splitcom[1]) - 10 == int(splitcom[0]) or int(splitcom[1]) + 10 == int(splitcom[0]) or int(splitcom[1]) - 1 == int(splitcom[0]) or int(splitcom[1]) + 1 == int(splitcom[0])) and isinstance(undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])], Territory) and undiscovered[int(list(splitcom[0])[0])][int(list(splitcom[0])[1])].p == playernames[turn]:
        if list(undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card)[0] == "♣":
          challenge = [undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card]
          print(f"\033[47m\033[30m\033[1m{challenge[-1]}\033[0m", end=" ")
          for n in range(2):
            challenge.append(main_deck[0])
            main_deck.pop(0)
            print(f"\033[47m\033[30m\033[1m{challenge[-1]}\033[0m", end=" ")
          print("")
          print('Storm! Type where you take your card from before the card index:')
          print('  "h": from your hand;')
          print('  "p": from your points;')
          print('  "e": from your expedition.')
          print("The cards should be in the same order as there were shown you! If you can't save your expedition, type " + '"sink exp".')
          print("(First card is the territory)")
          undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].vis = True
          situation = "\033[1mstorm\033[0m) "
        if list(undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card)[0] == "♠":
          cont = True
          print("Calm sea! Nothing to worry about - you just get one point.")
        if list(undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card)[0] == "♥":
          challenge = [undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card]
          print(f"\033[47m\033[30m\033[1m{challenge[-1]}\033[0m")
          situation = "\033[1mpirates\033[0m) "
          print("Pirates! Type the index of the card from the expedition to use it. If you use more than one, separate them by a space.")
          response = []
          tfe = 1
          ExpSunk = False
        if list(undiscovered[int(list(splitcom[1])[0])][int(list(splitcom[1])[1])].card)[0] == "♦":
          cont = True
          print("Treasure! You get 2 bonus cards from the main deck.")
          for i in range(2):
            take = main_deck.pop(0)
            playerhand[turn].append(take)
      else:
        print("Illegal: expedition can only move to bordering territories.")
    if cont == True:
      movexp = undiscovered[int(list(splitcom[0])[0])].pop(int(list(splitcom[0])[1]))
      undiscovered[int(list(splitcom[0])[0])].insert(int(list(splitcom[0])[1]), "   ")
      point = undiscovered[int(list(splitcom[1])[0])].pop(int(list(splitcom[1])[1]))
      undiscovered[int(list(splitcom[1])[0])].insert(int(list(splitcom[1])[1]), movexp)
      points[turn].append(point)
      situation = ""
      movexp = False
      turn += 1
      for line in range(600):
        print("")
      subprocess.call(["mplayer", "Downloads/Pausesignal.mp3"])
      for line in range(600):
        print("")
    if command in ("take 2", "take2"):
      for n in range(2):
        take = main_deck.pop(0)
        playerhand[turn].append(take)
      turn += 1
      for line in range(600):
        print("")
      subprocess.call(["mplayer", "Downloads/Pausesignal.mp3"])
      for line in range(600):
        print("")
    if len(command) == 9:
      try:
        splitcom = command.split(" ")
        splitcom[2] = int(splitcom[2]) - 1
        if splitcom[0] != "take" or splitcom[1] != "ch":
          raise ValueError()
        playerhand[turn].append(ch.pop(splitcom[2]))
        ch.insert(splitcom[2], main_deck.pop(0))
        turn += 1
        for line in range(600):
          print("")
        subprocess.call(["mplayer", "Downloads/Pausesignal.mp3"])
        for line in range(600):
          print("")
      except (ValueError, IndexError):
        pass
    pastcom = command
  except KeyboardInterrupt:
    print("")
    if input("Are you sure you want to quit (y/n)? ") in ("yes", "y", "ye", "es", "s", "e", "ys"):
      sys.exit("Game Interrupted")