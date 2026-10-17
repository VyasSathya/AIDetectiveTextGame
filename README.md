# AI Detective Text Game

Two Python command-line mystery prototypes explore suspect dialogue, clue collection, and accusations. The game implementations use local rules and predefined story content; the separate API experiment is not required to play.

## Try the prototypes

Install Python 3, then run these commands from the repository root. The game modules use the Python standard library and do not require an API key.

```sh
# Suspect simulation, notebook, and a ten-interrogation turn limit
python static/main.py -run

# A predefined investigation: Murder at Summit Lodge
python dynamic/game.py
```

Follow the numbered choices in the terminal. In the static prototype, interrogate suspects, review the notebook, cross names off the list, and choose **Solve the crime**. In the dynamic prototype, investigate locations, talk to characters, review clues, and accuse a suspect.

For the static command's help:

```sh
python static/main.py -help
```

## Explore the code

| Area | Entry point | What to read |
| --- | --- | --- |
| Suspect simulation | [static/main.py](static/main.py) | [Agent behavior](static/agent.py), [dialogue](static/dialogue.py), [notebook and verdict](static/storyteller.py) |
| Predefined mystery | [dynamic/game.py](dynamic/game.py) | [World and investigation](dynamic/game_world.py), [characters](dynamic/character.py), [clues](dynamic/clue.py) |

The static prototype creates helpful and misleading agents, simulates three units of world activity, and records confirmed and questionable clues separately. Its culprit is configured in `Storyteller`; this is an experiment in game structure rather than an inference model.

## Separate API experiment

[ratelimittest.py](ratelimittest.py) sends a request to the OpenAI Chat Completions API and prints rate-limit response headers. It imports `openai` and `requests`, reads `OPENAI_API_KEY` from the environment, and can incur API usage charges when run. Its model identifier and API behavior may need updating. No dependency versions are pinned, and this script is independent of the games.

## Project status

These are small terminal prototypes with separate implementations. Input handling and story logic are exploratory; no packaged application, visual demo, or automated test suite is included.

## License

This repository does not currently include a license. A public repository alone does not grant permission to reuse its code.
