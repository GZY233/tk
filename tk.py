import tkinter as tk
import random
import screeninfo

RANDOM_TEXTS = [
    "今天也要保持好心情呀～",
    "记得多喝水，补充水分！",
    "适当休息，效率更高哦～",
    "窗外的天气好像很不错！",
    "别忘记今天的小目标呀～",
    "累了就停下来喘口气吧",
    "你已经很棒啦，继续加油！",
    "偶尔摸鱼也是正常的～",
    "今晚可以早点休息哦",
    "明天又是新的一天！",
    "保持好心情",
    "期待下一次见面",
    '好好爱自己',
    "别熬夜",
    "天冷了记得多穿衣服",
    "我想你了",
    "顺顺利利",
    "今天过的开心吗"
]


total_windows = 0
max_windows = 200

def get_random_color():
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    return f"#{r:02x}{g:02x}{b:02x}"
def create_window(index, round_num):
    global total_windows
    if total_windows >= max_windows:
        return
    screen = screeninfo.get_monitors()[0]
    screen_width = screen.width
    screen_height = screen.height
    win_width, win_height = 260, 90

    x = random.randint(50, screen_width - win_width - 50)
    y = random.randint(50, screen_height - win_height - 50)

    window = tk.Toplevel()
    window.title(f"第{round_num}轮 - 提示{index + 1}（总{total_windows + 1}/{max_windows}）")
    window.config(bg=get_random_color())
    window.geometry(f"{win_width}x{win_height}+{x}+{y}")

    text = random.choice(RANDOM_TEXTS)
    tk.Label(
        window, text=text,
        font=("微软雅黑", 15),
        bg=window["bg"],
        padx=10, pady=10
    ).pack()
    total_windows += 1
    if index + 1 < 5:
        root.after(100, create_window, index + 1, round_num)
    else:
        if total_windows < max_windows:
            root.after(200, start_next_round, round_num + 1)
def start_next_round(round_num=1):
    create_window(0, round_num)
root = tk.Tk()
root.withdraw()

start_next_round()

root.mainloop()