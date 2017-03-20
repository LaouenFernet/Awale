# TODO: Comparer temps d'éxécution Negabeta/Negamax
# TODO: Nombre de coup
from evaluation import *
from game import Game
from negabeta_player import NegabetaPlayer

rep = [[] for _ in range(10)]
for i in range(1, 11):
    for j in range(1, 11):
        game = Game(NegabetaPlayer(i, evaluation2), NegabetaPlayer(j, evaluation2), debug=False)
        game.new_game()
        rep[i - 1].append(game.moves_count)
    print(i)
print(rep)