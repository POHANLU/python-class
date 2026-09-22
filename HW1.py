# HW1.py
# 檔案開啟與讀寫練習
# 這個範例會先自動建立 example.txt，然後讀取內容、再追加一行內容

from pathlib import Path


def main():
    filename = "example.txt"

    # 如果檔案不存在，就先建立它
    if not Path(filename).exists():
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Hello Python!\n")
            file.write("這是檔案讀寫練習。\n")
        print(f"已建立 {filename}")

    # 讀取檔案內容
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("=== 檔案內容 ===")
        print(content)

    # 追加內容到檔案尾端
    with open(filename, "a", encoding="utf-8") as file:
        file.write("這是追加的內容。\n")

    print("\n已在檔案尾端追加資料。")


if __name__ == "__main__":
    main()

# 補充說明：
# open("檔名", "r") = 讀取檔案
# open("檔名", "w") = 寫入檔案（會覆蓋原內容）
# open("檔名", "a") = 追加內容到檔案最後
# encoding="utf-8" = 讓中文可以正常讀寫
