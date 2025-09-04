# Lesson 16 - Arcade Project

## Tổng quan Project

Project `lesson16` là một mini-arcade gồm 2 trò chơi đơn giản được viết bằng Python, sử dụng pattern closure và command-line interface.

## Cấu trúc Files

### `arcade.py` - Menu Chính

- **Chức năng**: Điểm entry chính của ứng dụng, cung cấp menu để người dùng chọn game
- **Import**: `sys`, `rps`, `guess_number`
- **Hàm chính**: `play_game(name="PlayerOne")`
- **Luồng hoạt động**:
  1. Hiển thị menu với 3 lựa chọn: `1` (RPS), `2` (Guess Number), `x` (thoát)
  2. Kiểm tra input hợp lệ, nếu không hợp lệ gọi đệ quy `play_game(name)`
  3. Với lựa chọn `1`: tạo closure `rps(name)` và gọi hàm trả về
  4. Với lựa chọn `2`: tạo closure `guess_number(name)` và gọi hàm trả về
  5. Với lựa chọn `x`: gọi `sys.exit()` để thoát chương trình

### `rps.py` - Rock Paper Scissors Game

- **Pattern**: Closure factory function
- **Hàm chính**: `rps(name="PlayerOne")` → trả về `play_rps()`
- **Biến closure**: `game_count`, `player_wins`, `python_wins`
- **Cấu trúc**:

  ```python
  def rps(name):
      # Biến đóng lưu trạng thái
      game_count = 0
      player_wins = 0
      python_wins = 0

      def play_rps():
          # Enum để mapping số → tên
          class RPS(Enum): ROCK=1, PAPER=2, SCISSORS=3

          # Input validation với đệ quy
          # Random choice cho máy
          # Logic thắng thua: Rock>Scissors, Paper>Rock, Scissors>Paper
          # Update counters và hiển thị thống kê
          # Hỏi chơi lại hoặc thoát với sys.exit()

      return play_rps
  ```

### `guess_number.py` - Guess My Number Game

- **Pattern**: Closure factory function tương tự `rps.py`
- **Hàm chính**: `guess_number(name="PlayerOne")` → trả về `play_guess_number()`
- **Biến closure**: `game_count`, `player_wins`
- **Logic game**: Người chơi đoán số 1/2/3, nếu trùng với `random.choice("123")` thì thắng
- **Thống kê**: Hiển thị số ván, số thắng và tỷ lệ thắng (percentage)

## Luồng Thực Thi Chính

```
1. python arcade.py -n <name>
   │
   ├─ argparse phân tích tham số -n/--name (required)
   │
   ├─ play_game(name) được gọi
   │  │
   │  ├─ Hiển thị menu trong vòng lặp while True
   │  │
   │  ├─ Input validation với đệ quy nếu sai
   │  │
   │  └─ Chọn game:
   │     ├─ "1": rock_paper_scissors = rps(name); rock_paper_scissors()
   │     ├─ "2": guess_my_number = guess_number(name); guess_my_number()
   │     └─ "x": sys.exit()
   │
   └─ Game loop trong mỗi game:
      ├─ Input validation (đệ quy)
      ├─ Random generation cho máy
      ├─ Decide winner logic
      ├─ Update statistics
      ├─ Display results
      └─ Ask play again (Y/Q) → sys.exit() nếu Q
```

## Chi Tiết Kỹ Thuật

### Pattern Closure

- Mỗi game function (`rps`, `guess_number`) tạo closure chứa:
  - Tên người chơi (`name`)
  - Biến thống kê (`game_count`, `player_wins`, etc.)
  - Hàm thực thi (`play_*`) có quyền truy cập `nonlocal`

### Input Validation

- Sử dụng đệ quy để lặp prompt khi input không hợp lệ
- Pattern: `if invalid_input: return function_call()`

### Random Logic

- `random.choice("123")` để máy chọn ngẫu nhiên
- Convert string to int để so sánh logic

### Exit Behavior

- Tất cả game đều dùng `sys.exit()` khi quit
- Điều này dừng toàn bộ process, không quay về menu arcade

### Statistics Tracking

- Sử dụng biến `nonlocal` trong closure để cập nhật counters
- RPS: track cả `player_wins` và `python_wins`
- Guess Number: chỉ track `player_wins` và tính percentage
