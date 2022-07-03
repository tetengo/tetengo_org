#! /usr/bin/env python3

import random
from typing import List, Tuple

background_list: List[Tuple[str, str, str]] = [
    ("10%", "30%", "ariake.jpg"),
    ("25%", "75%", "jigoku.jpg"),
    ("10%", "30%", "laputa.jpg"),
    ("25%", "75%", "liccakuma.jpg"),
    ("10%", "30%", "mogushi.jpg"),
    ("10%", "30%", "shower.jpg"),
    ("25%", "75%", "sl.jpg"),
    ("10%", "30%", "suika.jpg"),
    ("25%", "75%", "tram.jpg"),
    ("10%", "30%", "tsujun.jpg"),
]

stylesheet_template: str = """@charset "UTF-8";
@media only screen and (min-width:801px) {{
    :root {{
        --panel-background: linear-gradient(175deg, rgba(100%, 100%, 100%, {}), rgba(100%, 100%, 100%, {}));
    }}
    div#styleholder-pc {{
        background: var(--panel-background);
    }}
    section h2 {{
        background: var(--panel-background);
    }}
    div.grid {{
        background: var(--panel-background);
    }}
}}
body {{
    background-image: url("{}");
}}
"""


def main() -> None:
    background: Tuple[str, str, str] = select_background()
    print("Content-Type: text/css; charset=UTF-8\n")
    print(
        stylesheet_template.format(
            background[0], background[1], "background/" + background[2]
        )
    )


def select_background() -> Tuple[str, str, str]:
    return random.choice(background_list)


if __name__ == "__main__":
    main()
