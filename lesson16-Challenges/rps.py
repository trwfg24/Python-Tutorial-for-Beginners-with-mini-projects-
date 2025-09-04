import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    """Create a Rock-Paper-Scissors game closure configured with `name`.

    Trả về hàm `play_rps()` để caller gọi khi muốn bắt đầu trò chơi.
    """

    # Thống kê trò chơi (lưu trong closure)
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        """Hàm nội thực hiện vòng chơi RPS tương tác với người dùng."""

        # Cho phép sửa biến ở scope bao ngoài (closure)
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        # Enum để biểu diễn các lựa chọn thay vì dùng số trực tiếp
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # Yêu cầu người chơi nhập lựa chọn
        playerchoice = input(
            f"\n{name}, Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n"
        )

        # Nếu input không hợp lệ, yêu cầu nhập lại (đệ quy)
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, You must enter 1, 2 or 3.")
            return play_rps()

        # Chuyển chuỗi sang số để so sánh
        player = int(playerchoice)

        # Bảo vệ: nếu số ngoài 1..3, thoát chương trình
        if player < 1 or player > 3:
            sys.exit("You must enter 1,2, or 3.")

        # Máy chọn ngẫu nhiên một trong '1','2','3'
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # In lựa chọn bằng tên (sử dụng Enum để chuyển số -> tên)
        print(f"\n{name}You chose {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        # Hàm quyết định thắng thua cho 1 ván
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            # Quy tắc thắng: Rock(1) > Scissors(3), Paper(2) > Rock(1), Scissors(3) > Paper(2)
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name},You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name},You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name},You win!"
            elif player == computer:
                return "😊Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python win!\nSorry, {name}"

        # Lấy kết quả và in
        game_result = decide_winner(player, computer)
        print(game_result)

        # Cập nhật số ván đã chơi và in thống kê
        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins:  {python_wins}")

        # Hỏi người chơi có muốn chơi tiếp không
        print(f"\nPlay agains, {name}?")
        while True:
            playgain = input("\nY for Yes or \nQ to Quit\n")
            if playgain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playgain.lower() == "y":
            return play_rps()
        else:
            print("Thank you for playing!\n")
            sys.exit(f"Bye! {name} 👌")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}")
            else:
                return

    return play_rps


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
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
