import chess
import chess.engine
import chess.variant
import re
import math

config = [
    "option descriptor (type)              [default]",
    "player color      (0:white|1:black)   [0]        : ",
    "pgn file path     (string)            [game]     : ",
    "analysis limit    (time|depth|nodes)  [time]     : ",
    "time per move     (float)             [3]        : ",
    "depth per move    (int)               [12]       : ",
    "nodes per move    (int)               [200000]   : ",
    "choice engine     (string)            [ffish]    : "
]

print("""  
  ______       _  _______              
 |  ____(x)   | ||__   __|             
 | |__   _ ___| |__ | |_ __ __ _ _ __  
 |  __| | / __| '_ \| | '__/ _` | '_ \ 
 | |    | \__ \ | | | | | | (_| | |_) |
 |_|    |_|___/_| |_|_|_|  \__,_| .__/ 
                                | |    v1.0
                                |_| by Camul13""")

print(" - Config - ")
print(config[0])
player = int(input(config[1]) or "0")
PGNpath = "games\\"+(input(config[2]) or "game")+".pgn"
enginepath = ".\\engines\\"+(input(config[7]) or "ffish")+".exe"
intype = input(config[3]) or "time"
if (intype == "time"):
    limit = chess.engine.Limit(time=float(input(config[4]) or "3"))
elif (intype == "depth"):
    limit = chess.engine.Limit(depth=int(input(config[5]) or "12"))
elif (intype == "nodes"):
    limit = chess.engine.Limit(nodes=int(input(config[6]) or "200000"))
else:
    exit("ERROR: bad input: 'intype'")

def convert(x): #need to add castling
    if '=' in x:
        p=x[-1].lower()
        return x[:-2]+p

    return x[1:] if len(x) > 4 else x

##debug
# path="games\game.pgn"
# enginepath="engines/mvstockfish.exe"
# player=0
# limit=chess.engine.Limit(time=0.1)
try:
    raw = open(PGNpath, 'r').read()
except FileNotFoundError:
    exit("ERROR: 'FileNotFoundError': bad input: 'PGNpath'")
moves = list(map(convert, [move for sublist in list(map(lambda x: re.sub(r"( 1-0| 0-1| 1\/2-1\/2)", "", x).split(), re.split(
    "\n\d+\. ", re.split('\n\n', raw)[1])[1:])) for move in sublist]))
try:
    engine = chess.engine.SimpleEngine.popen_uci(enginepath)
except FileNotFoundError:
    exit("ERROR: 'FileNotFoundError': bad input: 'enginepath'")
board = chess.variant.AtomicBoard()
print("\n - Checking Game - ")
sus = [0, 0]  # top3, top5
for move in range(len(moves)):
    if (bool((move % 2) if player else ((move+1) % 2))):
        print("\n(", math.ceil((move+1)/2), '/', math.ceil(len(moves)/2), ')')
        info = engine.analyse(board, limit, multipv=5)
        score = [i['score'].white() for i in info]
        top = [str(i['pv'][0].uci()) for i in info]
        try:
            idx = top.index(moves[move])
        except ValueError:
            idx = 999
        print("eval:", str(score[0]))
        print("suggested moves:", top)
        print("played move:", moves[move])
        if (idx <= 3):
            sus[0] += 1
            sus[1] += 1
            print("Top 3")
        elif (idx <= 5):
            sus[1] += 1
            print("Top 5")
        else:
            print("Not top")
    board.push_san(moves[move])
print("\n - Result -")
print("Moves in top 3:", sus[0], "/", math.ceil(len(moves)/2))
print("Moves in top 5:", sus[1], "/", math.ceil(len(moves)/2))
engine.quit()

input("END")