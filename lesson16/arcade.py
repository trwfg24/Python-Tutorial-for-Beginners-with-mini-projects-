import sys
from rps import rps
from guess_number import guess_number


def play_game(name="PlayerOne"):
    """
    Menu chính của Arcade. Người chơi chọn 1 trong các game hoặc 'x' để thoát.

    Thiết kế:
    - Nếu người chơi chọn 1: gọi game RPS
    - Nếu chọn 2: gọi game Guess My Number
    - Nếu chọn x: thoát chương trình
    """
    welcome_back = False

    while True:
        # Hiện menu và đọc lựa chọn
        playerchoice = input(
            '\nPlease choose a game: \n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade\n\n'
        )

        # Nếu đã vào menu ít nhất 1 lần, in lời chào quay lại
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        # Kiểm tra tính hợp lệ. Nếu nhập sai, gọi lại play_game để hiển thị menu lần nữa.
        # Ở đây dùng return play_game(name) (đệ quy) để tái hiện menu; có thể thay bằng continue.
        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return play_game(name)

        welcome_back = True

        if playerchoice == "1":
            # Gọi game Rock-Paper-Scissors
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            # Gọi game Guess My Number
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            # Thoát chương trình khi người dùng chọn 'x'
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade!")
    play_game(args.name)
