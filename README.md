# Emoji Garden Script for twitter bot

Emoji garden is a procedural script for growing gardens of emojis

the garden starts as soil then seedlings germinate and mature into plants or flowers which then wilt and return to the earth from which they came.

running the save_to_file.py will generate text files for each stage of the gardens development for an entire cycle

## Example Output

    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫

    🟫 🟫 🌱 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🌱
    🟫 🌱 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫

    🟫 🟫 🌱 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🌱 🟫 🌱 🟫 🌱
    🌱 🌱 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫

    🟫 🟫 🌷 🟫 🟫
    🟫 🌱 🟫 🟫 🟫
    🌱 🌱 🌿 🌱 🌱
    🌱 🌾 🌱 🟫 🟫
    🟫 🌱 🟫 🟫 🟫

    🌱 🟫 🌷 🟫 🌱
    🟫 🌱 🌱 🟫 🌱
    🌹 🌱 🌿 🌷 🌺
    🌹 🌾 🌱 🌱 🟫
    🟫 🌸 🌱 🌱 🌱

    🌿 🌱 🌷 🟫 🌼
    🌱 🌿 🌾 🟫 🌱
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌱 🟫
    🟫 🌸 🌷 🌱 🌱

    🌿 🌱 🌷 🟫 🌼
    🌱 🌿 🌾 🟫 🌱
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌱 🟫
    🌱 🌸 🌷 🌱 🌱

    🌿 🌹 🌷 🌱 🌼
    🌱 🌿 🌾 🌱 🌻
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌸 🌱
    🌿 🌸 🌷 🌸 🌹

    🌿 🌹 🌷 🌱 🌼
    🌹 🌿 🌾 🌼 🌻
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌸 🌱
    🌿 🌸 🌷 🌸 🌹

    🌿 🌹 🌷 🌺 🌼
    🌹 🌿 🌾 🌼 🌻
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌸 🌹
    🌿 🌸 🌷 🌸 🌹

    🌿 🌹 🌷 🌺 🌼
    🌹 🌿 🌾 🌼 🌻
    🌹 🌿 🌿 🌷 🌺
    🌹 🌾 🌷 🌸 🌹
    🌿 🌸 🌷 🌸 🌹

    🌿 🌹 🌷 🌺 🌼
    🌹 🌿 🌾 🌼 🌻
    🥀 🌿 🍂 🥀 🥀
    🌹 🍂 🌷 🌸 🌹
    🌿 🌸 🌷 🌸 🌹

    🍂 🌹 🥀 🌺 🌼
    🌹 🌿 🌾 🌼 🌻
    🟫 🍂 🟫 🟫 🥀
    🌹 🍂 🥀 🌸 🌹
    🌿 🌸 🥀 🌸 🌹

    🍂 🌹 🥀 🌺 🌼
    🌹 🌿 🍂 🌼 🌻
    🟫 🍂 🟫 🟫 🥀
    🥀 🍂 🥀 🌸 🌹
    🌿 🌸 🥀 🌸 🌹

    🟫 🌹 🥀 🌺 🌼
    🌹 🌿 🍂 🌼 🌻
    🟫 🟫 🟫 🟫 🟫
    🥀 🟫 🟫 🌸 🌹
    🌿 🥀 🟫 🌸 🌹

    🟫 🌹 🟫 🌺 🥀
    🥀 🍂 🍂 🌼 🌻
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🌸 🌹
    🍂 🥀 🟫 🥀 🌹

    🟫 🌹 🟫 🥀 🥀
    🥀 🍂 🟫 🌼 🌻
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🥀 🥀
    🍂 🥀 🟫 🥀 🌹

    🟫 🥀 🟫 🥀 🥀
    🥀 🍂 🟫 🌼 🥀
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🥀 🥀
    🟫 🟫 🟫 🥀 🥀

    🟫 🥀 🟫 🟫 🟫
    🟫 🟫 🟫 🥀 🥀
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🥀
    🟫 🟫 🟫 🟫 🥀

    🟫 🥀 🟫 🟫 🟫
    🟫 🟫 🟫 🥀 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🥀

    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🥀 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫

    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
    🟫 🟫 🟫 🟫 🟫
