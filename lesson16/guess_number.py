import sys
import random


def guess_number(name="PlayerOne"):
    """
    Khởi tạo game 'Guess My Number'.
    Hàm trả về một hàm nội bộ `play_guess_number` để khi gọi sẽ bắt đầu vòng chơi.

    Tham số:
        name (str): tên người chơi (dùng để in thông báo cá nhân hoá)
    """

    # Biến đóng giữ trạng thái của closure (được chia sẻ giữa các lần chơi)
    game_count = 0
    player_wins = 0

    def play_guess_number():
        """
        Hàm thực thi vòng chơi tương tác.
        Sử dụng `nonlocal` để sửa/reset các biến trong scope bao quanh (closure).
        """

        # Cho phép truy cập và sửa biến `name` và `player_wins` từ scope ngoài
        nonlocal name
        nonlocal player_wins

        # Yêu cầu người chơi nhập dự đoán (dưới dạng chuỗi)
        playerchoice = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2 or 3. \n\n"
        )

        # Kiểm tra tính hợp lệ: chỉ chấp nhận string '1','2','3'
        if playerchoice not in ["1", "2", "3"]:
            # Nếu nhập không hợp lệ, in hướng dẫn và gọi lại hàm để người chơi thử lại.
            # Ở đây dùng đệ quy; với bài tập nhỏ này là chấp nhận được nhưng có thể thay bằng loop.
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        # Máy chọn ngẫu nhiên một ký tự trong chuỗi '123'
        computerchoice = random.choice("123")

        # In lựa chọn của cả hai bên (để minh bạch kết quả)
        print(f"\n{name}, you chose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        # Chuyển chuỗi sang số nguyên để dễ so sánh sau này
        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            """
            Quyết định người thắng trong ván hiện tại.
            Trả về một chuỗi thông báo kết quả.
            Nếu người chơi đoán đúng (player == computer) thì tăng `player_wins`.
            """

            nonlocal name
            nonlocal player_wins

            if player == computer:
                # Người chơi đoán trùng => thắng
                player_wins += 1
                return f"{name}, you win!"
            else:
                # Người chơi đoán sai => thua. Ở variant này không lưu thắng của máy.
                return f"Sorry, {name}. Better luck next time."

        # Lưu kết quả từ hàm quyết định
        game_result = decide_winner(player, computer)

        # In kết quả ván
        print(game_result)

        # Cập nhật số ván đã chơi (sử dụng nonlocal trước khi gán)
        nonlocal game_count
        game_count += 1

        # In các thống kê cơ bản: tổng ván, số thắng của người chơi và tỷ lệ thắng
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        # Hỏi người chơi có muốn chơi tiếp không
        print(f"\nPlay again, {name}?")

        # Vòng lặp đảm bảo chỉ nhận 'y' hoặc 'q' (không phân biệt hoa/ thường)
        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                # Nếu không hợp lệ thì tiếp tục yêu cầu nhập
                continue
            else:
                break

        if playagain.lower() == "y":
            # Chơi lại: gọi lại chính hàm này (đệ quy) để bắt đầu ván mới
            return play_guess_number()
        else:
            # Người chơi muốn thoát: in lời cảm ơn
            print("Thank you for playing!\n")
            # Nếu file đang chạy trực tiếp, thoát process bằng sys.exit để dừng chương trình
            # Nếu module được import (ví dụ arcade.py), chỉ return để caller tiếp tục điều khiển.
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else:
                return

    # Trả về hàm thực thi; caller sẽ gọi hàm này để bắt đầu game
    return play_guess_number


if __name__ == "__main__":
    # Chỉ import argparse khi chạy file trực tiếp (nhỏ gọn khi import module)
    import argparse

    # Tạo parser để lấy tham số tên người chơi từ CLI
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

    # Tạo closure cho game với tên đã cung cấp và gọi hàm trả về để bắt đầu chơi.
    guess_my_number = guess_number(args.name)
    # Lưu ý: cần gọi hàm bằng dấu () để thực sự khởi động vòng chơi.
    guess_my_number()
