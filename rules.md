# Speiderne
- a card game by Samuel Brox.

It's a game where you will start expeditions, fight pirates, find treasures, and, eventually, building your own ferries; and all with the use of only a 52-card deck, a pen and some paper! (Magic, isn't it?)

Players: greater than 1.

What you need: 1 deck of playing cards without jokers, a pen and a piece of paper to write down points on (if you are more than 3, it is recommended you use more than 1 deck).
Values of card: 2 is lowest, A is highest.

[0. Goal](#goal)

[1. Discoverer](#discover)

[- 1.1. Before you start](#beforestart)

[- 1.2. Your turn](#turn)

[- 1.3. Draw cards](#cards)

[- 1.4. Make ready an expedition](#makexp)

[- 1.5. Move an expedition](#movexp)

[- - 1.5.1. ♣ - Storm](#storm)

[- - 1.5.2. ♠ - Windless](#windless)

[- - 1.5.3. ♥ - Pirates](#pirates)

[- - 1.5.4. ♦ - Treasure](#treasure)


## Goal<a name="goal"></a>
The game consists of two stages: 1 - Discoverer (not yet implemented), 2 - Ferries. The goal is to get the most points, which you get by the number of discovered regions, and later, for number of passangers.
# Discoverer<a name="discover"></a>
## Before you start<a name="beforestart"></a>
Make a 3⨯4 area with the value hidden: each of those cards represent an undiscovered region. Then give out 5 cards to each player. Lay out another 3 cards, which will be the "insurance" with the card values shown. The rest of the cards are placed with the values hidden, and will be the "main deck". If, at one point in the game, the main deck is out of cards, you should shuffle the discard and refill with that. When you have decided who goes first, you're ready to play.
## Your turn<a name="turn"></a>
On your turn you can do one of these following things:
1. Draw cards
2. Make ready an expedition
3. Move an expedition
After that, the turn passes to the next player.
## Draw cards<a name="cards"></a>
You could draw:
1. 2 cards from the main deck
2. 1 card from the insurance, unless on your last turn you lost an expedition, in which case you could take 2 cards (that's why it's called "insurance")
## Make ready an expedition<a name="makexp"></a>
Take 3 cards of the same sort from your hand and put it on besides a region, on a place not occupied. That will be your expedition. Don't forget passing the turn to the next player! <a name="fund"></a>After moving this expedition for the first time, it has to be funded at the end of each turn by any card from the owner's hand (that means throwing that card to the discard pile). If this is not done, one card from the expedition is trown away instead.
## Move an expedition<a name="movexp"></a>
Choose a bordering region (up, down, left or right) and, if the region is undiscovered, show the value. If the region is discoveres, skip these instructions entirely. Based on the value, different things could happen. After that, if there is any expedition left, it is placed on top of the newly discovered region; the turn passes to the next player.
### ♣ - Storm<a name="storm"></a>
If there's not enough resources to save the expedition, it might get sunk! There's 2 cards that define the strength of the storm and that you need to defend against: the storm-card itself and 1 card from the main deck. On each of these cards you should throw something higher than it from your hand. For each card you can't defend against, you take one card away from your expedition. All the used cards (what you defended with from your hand, what you took away from your expedition, the one from the main deck, however, not the storm-card itself) are thrown away to the discard pile. Only if the expedition sunk is the storm-card thrown away to the discard pile and replaced with a card from the main deck, with the value hidden; however, if the expedition only sunk because of the lack of [funding](#fund), you still get the point.
### ♠ - Windless<a name="windless"></a>
What a pity: no wind! You will have to fund this expedition with 2 cards, instead of 1 this turn.
### ♥ - Pirates<a name="pirates"></a>
We encounter an island! And then we see pirates... These pirates plunder your expedition: they won't stop until they get enough. Take cards from the expedition until the sum of the cards is more than the value of the pirate-card. These cards go to the discard pile. Same as the storm, the used cards (what you took away from your expedition, however, not the pirate-card itself) are thrown away to the discard pile. Only if the expedition sunk is the pirate-card thrown away to the discard pile and replaced with a card from the main deck, with the value hidden; however, if the expedition only sunk because of the lack of [funding](#fund), you still get the point.
### ♦ - Treasure<a name="treasure"></a>
An island! Seems like there should be treasure here... However, that doesn't always end well. If the island is too big (value of the treasure-card is more than 5), you loose a part of your expedition (throw a card to the discard pile). But you get your treasure, though! (take one card from the main deck)
