# Bài học 07: Dictionary và Set trong Python

## Mô tả tổng quan

File `dict_set.py` này là một bài học toàn diện về hai cấu trúc dữ liệu quan trọng trong Python: **Dictionary (Từ điển)** và **Set (Tập hợp)**. Bài học được chia thành hai phần chính với các ví dụ thực tế và minh họa chi tiết.

## Phần 1: Dictionary (Từ điển)

### 1.1 Tạo Dictionary

```python
# Cách 1: Sử dụng dấu ngoặc nhọn {}
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

# Cách 2: Sử dụng hàm dict()
band2 = dict(vocals="Plant", guitar='Page')
```

**Kiến thức:** Dictionary lưu trữ dữ liệu dưới dạng cặp key-value (khóa-giá trị).

### 1.2 Thuộc tính cơ bản

```python
print(type(band))  # <class 'dict'>
print(len(band))   # Số lượng cặp key-value
```

**Kiến thức:** Dictionary có type là `dict` và có thể đếm số phần tử bằng `len()`.

### 1.3 Truy cập dữ liệu

```python
# Truy cập trực tiếp
print(band["vocals"])

# Truy cập an toàn với get()
print(band.get('guitar'))
```

**Kiến thức:**

- `dict[key]` sẽ báo lỗi nếu key không tồn tại
- `dict.get(key)` trả về `None` nếu key không tồn tại

### 1.4 Xem thông tin Dictionary

```python
print(band.keys())    # Tất cả các key
print(band.values())  # Tất cả các value
print(band.items())   # Các cặp (key, value) dưới dạng tuple
```

### 1.5 Kiểm tra key tồn tại

```python
print('guitar' in band)    # True
print('triangle' in band)  # False
```

### 1.6 Thay đổi và cập nhật

```python
# Thay đổi giá trị
band['vocals'] = 'coverdale'

# Cập nhật nhiều cặp key-value
band.update({'bass': 'JPJ'})
```

### 1.7 Xóa phần tử

```python
# Xóa và trả về giá trị
removed_value = band.pop('bass')

# Xóa và trả về cặp key-value cuối cùng
last_item = band.popitem()  # Trả về tuple

# Xóa bằng del
del band['drums']

# Xóa tất cả
band.clear()

# Xóa toàn bộ dictionary
del band
```

### 1.8 Sao chép Dictionary

```python
# SAI: Tạo tham chiếu (reference)
# band2 = band

# ĐÚNG: Sao chép độc lập
band2 = band.copy()
band3 = dict(band)
```

**Kiến thức quan trọng:** Gán trực tiếp chỉ tạo tham chiếu, không tạo bản sao mới.

### 1.9 Dictionary lồng nhau

```python
member1 = {
    'name': 'Plant',
    'instrument': 'vocals'
}

band = {
    "member1": member1,
    'member2': member2
}

# Truy cập dữ liệu lồng
print(band['member1']['name'])
```

## Phần 2: Set (Tập hợp)

### 2.1 Tạo Set

```python
# Cách 1: Sử dụng dấu ngoặc nhọn {}
nums = {1, 2, 3, 4}

# Cách 2: Sử dụng hàm set()
nums2 = set((1, 2, 3, 4))
```

### 2.2 Thuộc tính đặc biệt của Set

```python
# Không cho phép phần tử trùng lặp
nums = {1, 2, 2, 3}  # Kết quả: {1, 2, 3}

# True = 1, False = 0 trong Set
nums = {1, True, 2, False, 3, 4, 0}  # Kết quả: {False, 1, 2, 3, 4}
```

**Kiến thức quan trọng:**

- Set tự động loại bỏ phần tử trùng lặp
- `True` được coi như `1`, `False` được coi như `0`

### 2.3 Kiểm tra phần tử

```python
print(2 in nums)  # True/False
```

**Lưu ý:** Không thể truy cập phần tử trong Set bằng index vì Set không có thứ tự.

### 2.4 Thêm phần tử

```python
# Thêm một phần tử
nums.add(8)

# Thêm nhiều phần tử từ iterable khác
morenums = {5, 6, 7}
nums.update(morenums)
```

**Kiến thức:** `update()` có thể nhận list, tuple, dictionary, hoặc set khác.

### 2.5 Các phép toán Set

#### 2.5.1 Union (Hợp)

```python
one = {1, 2, 3}
two = {5, 6, 7}
result = one.union(two)  # Tạo set mới chứa tất cả phần tử
```

#### 2.5.2 Intersection (Giao)

```python
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)  # Giữ lại chỉ các phần tử chung
```

#### 2.5.3 Symmetric Difference (Hiệu đối xứng)

```python
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)  # Giữ lại phần tử không chung
```

## Kiến thức trọng tâm

### Dictionary

1. **Mutable (có thể thay đổi)**: Có thể thêm, sửa, xóa sau khi tạo
2. **Ordered (có thứ tự)**: Từ Python 3.7+ duy trì thứ tự chèn
3. **Key phải immutable**: string, number, tuple (không được list, dict)
4. **Fast lookup**: Tra cứu theo key rất nhanh O(1)

### Set

1. **Mutable**: Có thể thêm, xóa phần tử
2. **Unordered**: Không có thứ tự cố định
3. **Unique elements**: Mỗi phần tử chỉ xuất hiện một lần
4. **Fast membership test**: Kiểm tra phần tử có trong set rất nhanh

## Các lỗi thường gặp trong code

1. **Dictionary nested**: Có lỗi chính tả `'intrument'` thay vì `'instrument'`
2. **Dictionary nested**: Có lỗi chính tả `"memeber1"` thay vì `"member1"`

## Ứng dụng thực tế

### Dictionary phù hợp cho:

- Lưu trữ thông tin người dùng (name, age, email)
- Cấu hình ứng dụng
- Cache dữ liệu
- Đếm tần suất xuất hiện

### Set phù hợp cho:

- Loại bỏ phần tử trùng lặp
- Kiểm tra membership nhanh
- Các phép toán tập hợp (giao, hợp, hiệu)
- Lưu trữ các ID duy nhất
