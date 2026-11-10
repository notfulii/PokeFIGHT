# PokeFIGHT - Legal notice and credits

## Disclaimer

PokeFIGHT is an **unofficial, non-commercial fan project** made as a university assignment.
It is free, it is not sold, and it has no ads or donations.

PokeFIGHT is **not affiliated with, endorsed, sponsored or approved by** Nintendo, The Pokémon Company, Creatures Inc. or GAME FREAK inc.

Pokémon, the Pokémon character names, sprites, cries and related artwork are trademarks and/or copyrights of
Nintendo, Creatures Inc. and GAME FREAK inc. © 1995-2026 Nintendo / Creatures Inc. / GAME FREAK inc.
All rights to that material belong to their owners. No copyright infringement is intended.

If a rights holder asks for any material to be removed, it will be removed.

## What is original

The source code (all `.py` files) was written for this project.

## Third-party material

| Material | Where it comes from | License / owner |
| --- | --- | --- |
| Pokémon data (stats, moves, types) | [PokéAPI](https://pokeapi.co) | PokéAPI code is BSD-3-Clause; the data describes Nintendo's games |
| Pokémon sprites, GIFs and cries | Downloaded at runtime from PokéAPI's [sprites](https://github.com/PokeAPI/sprites) and [cries](https://github.com/PokeAPI/cries) repositories | © Nintendo / Creatures Inc. / GAME FREAK inc. |
| Music: "Battle in the winter" (menu) | jobromedia - [OpenGameArt](https://opengameart.org/content/battle-in-the-winter) | CC0 |
| Music: "8-Bit Battle Loop" | Wolfgang_ - [OpenGameArt](https://opengameart.org/content/8-bit-battle-loop) | CC0 |
| Music: "8-Bit Victory Loop" | Wolfgang_ - [OpenGameArt](https://opengameart.org/content/8-bit-victory-loop) | CC0 |
| Font `Minecraft.ttf` | Fan-made font (not by Mojang) | Check the license on the site it was downloaded from |
| Menu backgrounds in `assets/backgrounds/` | Pokémon wallpapers and fan art found online | Belong to their original artists / Nintendo |

## How the assets are handled

The Pokémon images, GIFs and cries are **not included** in the source code: the game downloads them from PokéAPI
the first time it runs and keeps them in the local `assets/sprites/` and `assets/sounds/` folders.
