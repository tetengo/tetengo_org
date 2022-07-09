#! /usr/bin/env python3

import random
from typing import List, Tuple

background_list: List[Tuple[str, str, str]] = [
    (
        "ichigo.jpg",
        "linear-gradient(120deg, rgba(255, 64, 96, 20%), rgba(255, 64, 96, 40%))",
        "Pixabay and Einladung_zum_Essen",
    ),
    (
        "mikan.jpg",
        "linear-gradient(120deg, rgba(255, 128, 32, 20%), rgba(255, 128, 32, 40%))",
        "Pixabay and pixel2013",
    ),
    (
        "nashi.jpg",
        "linear-gradient(120deg, rgba(160, 160, 32, 10%), rgba(160, 160, 32, 30%))",
        "food.foto",
    ),
    (
        "suika.jpg",
        "linear-gradient(120deg, rgba(128, 208, 255, 30%), rgba(128, 208, 255, 50%))",
        "Pixabay and grantour",
    ),
]

stylesheet_template: str = """@charset "UTF-8";
header {{
    background-image: url("{}");
}}

article dt {{
    background: {};
}}

p#background-provider:after {{
    content: "{}";
}}
"""


def main() -> None:
    background: Tuple[str, str, str] = select_background()
    print("Content-Type: text/css; charset=UTF-8\n")
    print(
        stylesheet_template.format(
            "background/" + background[0], background[1], background[2]
        )
    )


def select_background() -> Tuple[str, str, str]:
    return random.choice(background_list)


if __name__ == "__main__":
    main()
