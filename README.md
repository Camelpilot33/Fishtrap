# FishTrap
Program for catching stockfish cheaters in Atomic
## Limitations
 - Windows (Might work elsewhere)
 - Only [Chess.com](Chess.com) games tested
## Requirments
 - Windows 10 (Untested on other OS)
 - [Python 3.7+](https://www.python.org/downloads/)
 - [Python-Chess](https://pypi.org/project/chess/) > `pip install chess`
## Usage
 - Clone the repository or download the [release](https://github.com/Camelpilot33/Fishtrap/releases)
 - Find the [Chess.com](Chess.com) game, and click the `Download PGN` button:\
<img src="https://i.imgur.com/fgXaA65.png" width=200></img>
 - Move the PGN file to the `Fishtrap\games` directory, rename it to something shorter (default is `game.pgn`)
 - Run `main.py` > `python main.py`
 - Fill out the configuration:
   - `player color` takes a `0` or `1` with default `0`, `0` means white, `1` means black
   - `pgn file path` takes a `string` with default `game`, becomes `Fishtrap/games/<input>.pgn`
   - `choice engine` takes a `string` with default `ffish`, becomes `Fishtrap/engines/<input>.exe`, fairy-stockfish (ffish) and multi-variant stockfish (mvstockfish) come preinstalled
   - `analysis limit` takes a `string` with default `time`, sets the type of limit for the engine, `time`, `depth`, or `nodes`
   - `time per move` takes a `float` with default `3`, sets the time per step limit in seconds
   - `depth per move` takes an `int` with default `12`, sets the depth per step limit
   - `nodes per move` takes an `int` with default `200000`, sets the nodes per step limit
 - Wait until the all the steps end, sample step
```python
( 7 / 17 ) # Progress
eval: +100 # Eval in centipawns
suggested moves: ['a1a2', 'b1b2', 'c1c2', 'd1d2', 'e1e2'] # Top 5 engine moves, left to right, in UCI Protocol notation
played move: b1b2 # Move given in PGN file
Top 3 # Gives selector of move
```
 - Result given gives the moves in top 3 and top 5
   - Top engine line usually appears in top 3
## Comments
 - You can install any uci engine that can handle atomic, and some code adaption can do xboard ones
 - limiting time is very good for catching cheaters, but depth runs much faster (set to 12-19 for best results)
 - You can manually go back through the moves to look at the eval, as cheaters make "mistakes" purposefully when up material
 - Do not take this program extremely seriously