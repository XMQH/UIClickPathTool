from tkinter import *
import pyperclip


def ui_window(uipath):
    var = StringVar()
    var.set(uipath)
    root = Tk()
    root.title('UI点击路径')
    root.geometry('500x500')  # 这里的乘号不是 * ，而是小写英文字母 x
    lb_title = Label(root, text="当前点击按钮路径", anchor=NW)
    lb_title.grid(row=0)
    lb_uipath = Label(root, textvariable=var, anchor=NW)
    lb_uipath.grid(row=1)

    def get_uipath():
        path = lb_uipath.cget("text")
        # copies all the data the user has copied
        return pyperclip.copy(path)

    copy_button = Button(root, text="复制", anchor=NW, command=get_uipath)
    copy_button.grid(row=3)
    lb_button_path = Label(root, text="按钮路径", anchor=NW)
    lb_button_path.grid(row=4)
    # 创建滚动条
    s = Scrollbar(root)
    s.grid(column=0)
    # 将 selectmode 设置为多选模式，并为Listbox控件添加滚动条
    listbox1 = Listbox(root, selectmode=MULTIPLE, height=5, yscrollcommand=s.set)
    # i 表示索引值，item 表示值，根据索引值的位置依次插入
    for i, item in enumerate(range(1, 50)):
        listbox1.insert(i, item)
    listbox1.grid(row=5)
    # 设置滚动条，使用 yview使其在垂直方向上滚动 Listbox 组件的内容，通过绑定 Scollbar 组件的 command 参数实现
    s.config(command=listbox1.yview)
    # 使用匿名函数,创建删除函数，点击删除按钮，会删除选项
    bt = Button(root, text='删除', command=lambda x=listbox1: x.delete(ACTIVE))
    # 将按钮放置在底部
    bt.grid(row=6)

    root.mainloop()
