import tkinter as tk
import random

# 周易64卦的数据，包括卦象名字、卦象图形和爻辞
guas = [
    {
        "name": "乾",
        "image": "䷀䷁",
        "yao_ci": "元亨利贞。"
    },
    {
        "name": "坤",
        "image": "䷂䷃",
        "yao_ci": "元亨利牝马之贞。君子好逑，君子好逑。"
    },
    {
        "name": "屯",
        "image": "䷄䷅",
        "yao_ci": "元亨，贞元吉，有攸往，见凶，位正，有祟。"
    },
    {
        "name": "蒙",
        "image": "䷆䷇",
        "yao_ci": "亨。匪我求童蒙，童蒙求我。初筮告，再三渎，渎则不告。利贞。"
    },
    {
        "name": "需",
        "image": "䷈䷉",
        "yao_ci": "有孚，光亨，贞吉。利涉大川。"
    },
    {
        "name": "讼",
        "image": "䷊䷋",
        "yao_ci": "有孚窒惕，中吉，终凶。利见大人，不利涉大川。"
    },
    {
        "name": "师",
        "image": "䷌䷍",
        "yao_ci": "贞丈人，吉无咎。"
    },
    {
        "name": "比",
        "image": "䷎䷏",
        "yao_ci": "吉。"
    },
    {
        "name": "小畜",
        "image": "䷐䷑",
        "yao_ci": "亨。密云不雨，自我西郊。"
    },
    {
        "name": "履",
        "image": "䷒䷓",
        "yao_ci": "素履，往无咎。"
    },
    {
        "name": "泰",
        "image": "䷔䷕",
        "yao_ci": "小往大来，吉，亨。"
    },
    {
        "name": "否",
        "image": "䷖䷗",
        "yao_ci": "否之匪人，不利君子贞，大往小来。"
    },
    {
        "name": "同人",
        "image": "䷘䷙",
        "yao_ci": "同人于野，亨。利涉大川，利君子贞。"
    },
    {
        "name": "大有",
        "image": "䷚䷛",
        "yao_ci": "元亨。"
    },
    {
        "name": "谦",
        "image": "䷜䷝",
        "yao_ci": "亨，君子有终。"
    },
    {
        "name": "豫",
        "image": "䷞䷟",
        "yao_ci": "利建侯行师。"
    },
    {
        "name": "随",
        "image": "䷠䷡",
        "yao_ci": "元亨利贞，无咎。"
    },
    {
        "name": "蛊",
        "image": "䷢䷣",
        "yao_ci": "元亨利涉大川。先甲三日，后甲三日。"
    },
    {
        "name": "临",
        "image": "䷤䷥",
        "yao_ci": "元亨利贞。至于八月有凶。"
    },
    {
        "name": "观",
        "image": "䷦䷧",
        "yao_ci": "盥而不荐，有孚顒若。"
    },
    {
        "name": "噬嗑",
        "image": "䷨䷩",
        "yao_ci": "亨。利用狱。"
    },
    {
        "name": "贲",
        "image": "䷪䷫",
        "yao_ci": "亨。小利有攸往。"
    },
    {
        "name": "剥",
        "image": "䷬䷭",
        "yao_ci": "不利有攸往。"
    },
    {
        "name": "复",
        "image": "䷮䷯",
        "yao_ci": "亨。出入无疾，朋来无咎。反复其道，七日来复。利有攸往。"
    },
    {
        "name": "无妄",
        "image": "䷰䷱",
        "yao_ci": "元亨，利贞。其匪正有眚，不利有攸往。"
    },
    {
        "name": "大畜",
        "image": "䷲䷳",
        "yao_ci": "利贞，不家食吉，利涉大川。"
    },
    {
        "name": "颐",
        "image": "䷴䷵",
        "yao_ci": "贞吉。观颐，自求口实。"
    },
    {
        "name": "大过",
        "image": "䷶䷷",
        "yao_ci": "栋桡，利有攸往，亨。"
    },
    {
        "name": "坎",
        "image": "䷸䷹",
        "yao_ci": "习坎，有孚，维心亨，行有尚。"
    },
    {
        "name": "离",
        "image": "䷺䷻",
        "yao_ci": "利贞，亨。畜牝牛，吉。"
    },
    {
        "name": "咸",
        "image": "䷼䷽",
        "yao_ci": "亨，利贞，取女吉。"
    },
    {
        "name": "恒",
        "image": "䷾䷿",
        "yao_ci": "亨，小狐汔济，濡其尾，无攸利。"
    },
    {
        "name": "遯",
        "image": "䷸䷹",
        "yao_ci": "亨，小利贞。"
    },
    {
        "name": "大壮",
        "image": "䷃䷂",
        "yao_ci": "利贞。"
    },
    {
        "name": "晋",
        "image": "䷁䷀",
        "yao_ci": "康侯用锡马蕃庶，昼日三接。"
    },
    {
        "name": "明夷",
        "image": "䷀䷁",
        "yao_ci": "利艰贞。"
    },
    {
        "name": "家人",
        "image": "䷂䷃",
        "yao_ci": "利女贞。"
    },
    {
        "name": "睽",
        "image": "䷄䷅",
        "yao_ci": "小事吉。"
    },
    {
        "name": "蹇",
        "image": "䷆䷇",
        "yao_ci": "利西南，不利东北。利见大人，贞吉。"
    },
    {
        "name": "解",
        "image": "䷈䷉",
        "yao_ci": "利西南。无所往，其来复。"
    },
    {
        "name": "损",
        "image": "䷊䷋",
        "yao_ci": "有孚，元吉，无咎，可贞，利有攸往。曷之用？二簋可用享。"
    },
    {
        "name": "益",
        "image": "䷌䷍",
        "yao_ci": "利有攸往，利涉大川。"
    },
    {
        "name": "夬",
        "image": "䷎䷏",
        "yao_ci": "扬于王庭，孚号，有厉。告自邑，不利即戎，利有攸往。"
    },
    {
        "name": "姤",
        "image": "䷐䷑",
        "yao_ci": "女壮，勿用取女。"
    },
    {
        "name": "萃",
        "image": "䷒䷓",
        "yao_ci": "亨。王假有庙。利见大人。"
    },
    {
        "name": "升",
        "image": "䷔䷕",
        "yao_ci": "元亨，用见大人，勿恤，南征吉。"
    },
    {
        "name": "困",
        "image": "䷖䷗",
        "yao_ci": "亨，贞，大人吉，无咎，有言不信。"
    },
    {
        "name": "井",
        "image": "䷘䷙",
        "yao_ci": "改邑不改井，无丧无得，往来亡。"
    },
    {
        "name": "革",
        "image": "䷚䷛",
        "yao_ci": "己日乃孚，元亨利贞，悔亡。"
    },
    {
        "name": "鼎",
        "image": "䷜䷝",
        "yao_ci": "元吉，亨。"
    },
    {
        "name": "震",
        "image": "䷞䷟",
        "yao_ci": "亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。"
    },
    {
        "name": "艮",
        "image": "䷠䷡",
        "yao_ci": "艮其背，不获其身，行其庭，不见其人，无咎。"
    },
    {
        "name": "渐",
        "image": "䷢䷣",
        "yao_ci": "女归吉，利贞。"
    },
    {
        "name": "归妹",
        "image": "䷤䷥",
        "yao_ci": "征凶，无攸利。"
    },
    {
        "name": "丰",
        "image": "䷦䷧",
        "yao_ci": "亨。王假之，勿忧，宜日中。"
    },
    {
        "name": "旅",
        "image": "䷨䷩",
        "yao_ci": "小亨，旅贞吉。"
    },
    {
        "name": "巽",
        "image": "䷪䷫",
        "yao_ci": "小亨，利攸往，利见大人。"
    },
    {
        "name": "兑",
        "image": "䷬䷭",
        "yao_ci": "亨，利贞。"
    },
    {
        "name": "涣",
        "image": "䷮䷯",
        "yao_ci": "亨。王假有庙。利涉大川，利贞。"
    },
    {
        "name": "节",
        "image": "䷰䷱",
        "yao_ci": "亨，苦节不可贞。"
    },
    {
        "name": "中孚",
        "image": "䷲䷳",
        "yao_ci": "豚鱼，吉。利涉大川，利贞。"
    },
    {
        "name": "小过",
        "image": "䷴䷵",
        "yao_ci": "亨。利贞，可小事，不可大事。飞鸟遗之音，不宜上宜下，大吉。"
    },
    {
        "name": "既济",
        "image": "䷶䷷",
        "yao_ci": "亨。小利贞，初吉终乱。"
    },
    {
        "name": "未济",
        "image": "䷸䷹",
        "yao_ci": "亨，小狐汔济，濡其尾，无攸利。"
    }
]

def random_gua():
    gua = random.choice(guas)
    return gua


    
def show_gua():
    gua = random_gua()

    root = tk.Tk()
    root.title("卦象")

    label_name = tk.Label(root, text=gua["name"], font=("Arial", 16, "bold"))
    label_name.pack()

    label_image = tk.Label(root, text=gua["image"], font=("Arial", 40))
    label_image.pack()

    label_yao_ci = tk.Label(root, text=gua["yao_ci"], font=("Arial", 12))
    label_yao_ci.pack()

    root.mainloop()
    

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
# 创建主窗口
root = tk.Tk()
root.title("周易64卦")

# 设置窗口大小
window_width = 400
window_height = 300
center_window(root, window_width, window_height)

# 创建按钮
button = tk.Button(root, text="开始占卜", command=show_gua)
button.pack(pady=20)


tk.mainloop()
