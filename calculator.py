# #创建可视界面导入tkinker模块的所有内容，标准GUI库，创建可视界面
# from tkinter import *
# import math
# from math import factorial
#
# #self.result = StringVar()
# #self.equation = StringVar()
#
#
# # 全局变量
# global variable
# #
# variable = ""
#
# #class Cal(object):
# def Click(numbers):
#     global variable
#     variable = variable + str(numbers)
#     text_input.set(variable)
#
# #清除运算
# def ClearDisplay():
#     global variable
#     variable=""
#     text_input.set("0")
#
# #等于运算
# def Equal():
#     global variable
#     sumup = eval(str(variable))
#     text_input.set(sumup)
#
# #空格函数
# def BackSpace():
#    global variable
#    len_variable = len(str(variable))
#    variable = str(variable)[:len_variable-1]
#    text_input.set(variable)
#
# #log函数
# def Log():
#     global variable
#     variable = str(math.log(eval(variable)))
#     text_input.set(variable)
#
# def Lg():
#     global variable
#     variable = str(math.log10(eval(variable)))
#     text_input.set(variable)
#
#
# #阶乘
# def Factorial():
#     global variable
#     variable = math.factorial(eval(variable))
#     text_input.set(variable)
#
# #开方
# def Square():
#     global variable
#     variable = math.sqrt(eval(variable))
#     text_input.set(variable)
#
# def Sin():
#     global variable
#     variable = str(round(math.sin(eval(variable) * math.pi / 180.0), 2))
#     text_input.set(variable)
#
#
# def Cos():
#     global variable
#     variable = str(round(math.cos(eval(variable) * math.pi / 180.0), 2))
#     text_input.set(variable)
#
#
# def Tan():
#     global variable
#     variable = str(round(math.tan(eval(variable) * math.pi / 180.0), 2))
#     text_input.set(variable)
#
#
# def Cot():
#     global variable
#     variable = str(round((1 / (math.tan(eval(variable) * math.pi / 180.0))), 2))
#     text_input.set(variable)
#
#
#
#
#
#
# # 创建窗口对象?
# calculator = Tk()
# # 命名
# calculator.title('简易计算器')
#
# # stringVar是tkinter库内部定义的字符串变量类型，在这里用于管理部件上面的字符，跟踪变量值的变化，可以随时显示在界面上
# text_input = StringVar()
# # Entry(输入框)组件通常用于获取用户的输入文本；bd是borderwidth单元格边框宽度,bg是文本框颜色，fg是字体颜色，textvariable，，，，，justify指定文本框里的文字对齐方式是右边;
# # grid是布局管理器，将父窗口网格划线，将控件放在其中的单元格中，row，column用来设置控件所在单元格的坐标；columnspan合并8列
#
#
# Input_box = Entry(calculator, fg="black", bg='powderblue', bd=10, textvariable=text_input, insertwidth=4,justify='right').grid(columnspan=8)
# # ipadx:水平方向内边距，ipady:竖直方向内边距，padx:水平方向外边距，pady:竖直方向外边距,按钮的大小
#
#
#
# Button7 = Button(calculator, fg="black", padx=16, pady=16, text='7', command=lambda: Click(7)).grid(row=1, column=1)
# Button8 = Button(calculator, fg="black", padx=16, pady=16, text='8', command=lambda: Click(8)).grid(row=1, column=2)
# Button9 = Button(calculator, fg="black", padx=16, pady=16, text='9', command=lambda: Click(9)).grid(row=1, column=3)
# Addition = Button(calculator, fg="black", padx=16, pady=16, text='+', command=lambda: Click("+")).grid(row=1, column=4)
# Button4 = Button(calculator, fg="black", padx=16, pady=16, text='4', command=lambda: Click(4)).grid(row=2, column=1)
# Button5 = Button(calculator, fg="black", padx=16, pady=16, text='5', command=lambda: Click(5)).grid(row=2, column=2)
# Button6 = Button(calculator, fg="black", padx=16, pady=16, text='6', command=lambda: Click(6)).grid(row=2, column=3)
# Subtraction = Button(calculator, fg="black", padx=16, pady=16, text='-', command=lambda: Click("-")).grid(row=2, column=4)
# Button1 = Button(calculator, fg="black", padx=16, pady=16, text='1', command=lambda: Click(1)).grid(row=3, column=1)
# Button2 = Button(calculator, fg="black", padx=16, pady=16, text='2', command=lambda: Click(2)).grid(row=3, column=2)
# Button3 = Button(calculator, fg="black", padx=16, pady=16, text='3', command=lambda: Click(3)).grid(row=3, column=3)
# Multiply = Button(calculator, fg="black", padx=16, pady=16, text='*', command=lambda: Click("*")).grid(row=3, column=4)
# Devision = Button(calculator, fg="black", padx=16, pady=16, text='/', command=lambda: Click("/")).grid(row=4, column=1)
# Clear = Button(calculator, fg="black", padx=16, pady=16, text='C', command=lambda: ClearDisplay()).grid(row=5, column=2)
# Equals = Button(calculator, fg="black", padx=16, pady=16, text='=', command=lambda: Equal()).grid(row=4, column=3)
# Delivery = Button(calculator, fg="black", padx=16, pady=16, text='%', command=lambda: Click("%")).grid(row=4, column=4)
# _Square = Button(calculator, fg="black", padx=16, pady=16, text='√', command=lambda:Square() ).grid(row=5, column=1)
# Button0 = Button(calculator, fg="black", padx=16, pady=16, text='0', command=lambda: Click('0')).grid(row=4, column=2)
# decimal_point = Button(calculator, fg="black", padx=16, pady=16, text='.', command=lambda: Click(".")).grid(row=5, column=3)
# backspace = Button(calculator, fg="black", padx=16, pady=16, text='<-', command=lambda: BackSpace()).grid(row=5, column=4)
# _factorial = Button(calculator,fg="black", padx=16, pady=16, text='!', command=lambda: Factorial()).grid(row=5, column=5)
# Buttoncos = Button(calculator, fg="black", padx=16, pady=16, text='cos', command=lambda: Cos()).grid(row=2, column=6)
# Right_bracket = Button(calculator, fg="black", padx=16, pady=16, text='(', command=lambda: Click('(')).grid(row=3,column=5)
# Buttontan = Button(calculator, fg="black", padx=16, pady=16, text='tan', command=lambda: Tan()).grid(row=3, column=6)
# Buttonsin = Button(calculator, fg="black", padx=16, pady=16, text='sin', command=lambda: Sin()).grid(row=1, column=6)
# Left_bracket = Button(calculator, fg="black", padx=16, pady=16, text=')', command=lambda: Click(')')).grid(row=4,column=5)
# log = Button(calculator, fg="black", padx=16, pady=16, text='ln', command=lambda: Log()).grid(row=1, column=5)
# log10 = Button(calculator, fg="black", padx=16, pady=16, text='lg ', command=lambda: Lg()).grid(row=2, column=5)
#
#
# #进入消息循环
# calculator.mainloop()

# import math
# from tkinter import *  # 导入tkinter库的所有内容
#
# # 全局变量
# global variable
# variable = ""
# #程序的入口
# if __name__ == "__main__":
#     root = Tk()
#
# class Cal():
#     def __init__(self, calculator):
#         self.calculator = calculator
#         self.calculator.title('简易计算器')
#         self.calculator.resizable(width=True, height=True)  # 设置窗口可拉伸
#
#         self.text_input = StringVar()
#         self.equation = StringVar()
#         self.text_input.set("0")
#         self.equation.set("0")
#
#         self.Input_box = Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.text_input,insertwidth=2, justify='right').grid(columnspan=7)
#         self.show_result_eq = Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.equation,insertwidth=2, justify='right').grid(columnspan=7)
#
#         # 第二行
#         # 按钮的command参数，是回调函数，lambda函数是为了可以传参数给回调函数
#         self.Buttonsin = Button(self.calculator, bg='powderblue', fg="black",padx=15,pady=3, text='sin',command=lambda: self.Sin()).grid(row=2, column=1)
#         self.Clear = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='AC',command=lambda: self.ClearDisplay()).grid(row=2, column=2)
#         self.backspace = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='←',command=lambda: self.BackSpace()).grid(row=2, column=3)
#         self.Devision = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='/',command=lambda: self.Click("/")).grid(row=2, column=4)
#         self.square = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='√',command=lambda: self.Pow()).grid(row=2, column=5)
#         self.factorial = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='n!',command=lambda: self.Factorial()).grid(row=2, column=6)
#
#         # 第三行
#         self.Buttoncos = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='cos',command=lambda: self.Cos()).grid(row=3, column=1)
#         self.Button7 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='7',command=lambda: self.Click(7)).grid(row=3, column=2)
#         self.Button8 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='8',command=lambda: self.Click(8)).grid(row=3, column=3)
#         self.Button9 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='9',command=lambda: self.Click(9)).grid(row=3, column=4)
#         self.Multiply = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='*',command=lambda: self.Click("*")).grid(row=3, column=5)
#         self.Delivery = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='%',command=lambda: self.Click("%")).grid(row=3, column=6)
#
#         # self.reciprocal = Button(calculator, fg="black", padx=4,  pady=4, text='1/x', command=lambda: Reciprocal()).grid(row=3, column=5)
#
#         # 第四行
#         self.Buttontan = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='tan',command=lambda: self.Tan()).grid(row=4, column=1)
#         self.Button4 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='4',command=lambda: self.Click(4)).grid(row=4, column=2)
#         self.Button5 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='5',command=lambda: self.Click(5)).grid(row=4, column=3)
#         self.Button6 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='6',command=lambda: self.Click(6)).grid(row=4, column=4)
#         self.Subtraction = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='-',command=lambda: self.Click("-")).grid(row=4, column=5)  # 减
#         self.Left_bracket = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='(',command=lambda: self.Click('(')).grid(row=4, column=6)
#
#         # 第五行
#         self.ln = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='ln',command=lambda: self.Ln()).grid(row=5, column=1)  # 取对数
#         self.Button1 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='1',command=lambda: self.Click(1)).grid(row=5, column=2)
#         self.Button2 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='2',command=lambda: self.Click(2)).grid(row=5, column=3)
#         self.Button3 = Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='3',command=lambda: self.Click(3)).grid(row=5, column=4)
#         self.Addition = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='+',command=lambda: self.Click("+")).grid(row=5, column=5)
#         self.Right_bracket = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text=')',command=lambda: self.Click(')')).grid(row=5, column=6)
#
#         # 第六行
#         self.lg = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='lg',command=lambda: self.Lg()).grid(row=6, column=1)
#         # Buttoncot = Button(calculator, bg='powderblue', fg="black", padx=4,  pady=4, text='cot', command=lambda: Cot()).grid(row=6, column=2)
#         self.Button0 = Button(self.calculator, bg='orange', fg="black", padx=65, pady=3, text='0',command=lambda: self.Click(0)).grid(row=6, columnspan=6)
#         self.decimal_point = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='.',command=lambda: self.Click(".")).grid(row=6, column=5)
#         self.Equals = Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='=',command=lambda: self.EqualsInput()).grid(row=6, column=6)
#         # self.Buttonpi = Button(self.calculator, bg='orange', fg="black", padx=4,  pady=4, text='π',command=lambda: self.Click('π')).grid(row=6, column=6)
#
#     def Click(self, numbers):
#         global variable
#         variable = variable + str(numbers)
#         self.text_input.set(variable)
#
#     #
#     def ClearDisplay(self):
#         global variable
#         variable = ""
#         self.text_input.set("0")
#         self.equation.set("0")
#
#     def EqualsInput(self):
#         global variable
#         try:
#             sumup = eval(str(variable))
#             self.equation.set(sumup)
#         except (SyntaxError, ZeroDivisionError, NameError):  # 找不到变量名会出现NameError
#             self.equation.set('Error!')
#
#     def BackSpace(self):
#         global variable
#         len_variable = len(str(variable))
#         variable = str(variable)[:len_variable - 1]
#         self.text_input.set(variable)
#
#     def Lg(self):
#         global variable
#         try:
#             self.text_input.set('lg({})'.format(variable))
#             variable = str(math.log10(eval(variable)))
#             self.equation.set(variable)
#         except ValueError:
#             self.equation.set('Error!')
#
#     def Ln(self):
#         global variable
#         try:
#             self.text_input.set('ln({})'.format(variable))
#             variable = str(math.log(eval(variable)))
#             self.equation.set(variable)
#         except ValueError:
#             self.equation.set('Error!')
#
#     def Pow(self):
#         global variable
#         self.text_input.set('√{}'.format(variable))
#         variable = str(math.sqrt(eval(variable)))
#         self.equation.set(variable)
#
#     def Factorial(self):
#         global variable
#         self.text_input.set('{}!'.format(variable))
#         variable = str(math.factorial(eval(variable)))
#         self.equation.set(variable)
#
#     def Sin(self):
#         global variable
#         self.text_input.set('sin({})'.format(variable))
#         variable = str(round(math.sin(eval(variable) * math.pi / 180.0),2))
#         self.equation.set(variable)
#
#     def Cos(self):
#         global variable
#         self.text_input.set('cos({})'.format(variable))
#         variable = str(round(math.cos(eval(variable) * math.pi / 180.0),2))
#         self.equation.set(variable)
#
#     def Tan(self):
#         global variable
#         self.text_input.set('tan({})'.format(variable))
#         variable = str(round(math.tan(eval(variable) * math.pi / 180.0),2))
#         self.equation.set(variable)
#
#     #def qucheng():
#         #global variable
#         #variable=str(variable+1)
#
# my_cal = Cal(root)#实例化
# root.mainloop()#进入消息循环




import math
#from tkinter import *
import tkinter as tk


global variable
variable = ""

class Cal:
    def __init__(self, calculator):
        self.calculator = calculator
        self.calculator.title('简易计算器')
        self.calculator.resizable(width=True, height=True)  # 设置窗口可拉伸
        self.calculator = tk.Frame(root)
        self.calculator.pack()
        self.text_input = tk.StringVar()
        self.equation = tk.StringVar()

        self.text_input.set("0")
        self.equation.set(" ")

        self.Input_box =tk.Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.text_input,
                               insertwidth=2, justify='right').grid(columnspan=7)
        self.show_result_eq =tk.Entry(self.calculator, fg="black", bg='powderblue', bd=10, textvariable=self.equation,
                                    insertwidth=2, justify='right').grid(columnspan=7)


        # 第二行
        self.Buttonsin = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='sin',
                                command=lambda: self.Click('sin')).grid(row=2, column=1)
        self.Clear = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='AC',
                            command=lambda: self.ClearDisplay()).grid(row=2, column=2)
        self.backspace = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='←',
                                command=lambda: self.BackSpace()).grid(row=2, column=3)
        self.Devision = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='/',
                               command=lambda: self.Click("/")).grid(row=2, column=4)

        self.factorial = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='n!',
                                command=lambda: self.Factorial()).grid(row=2, column=5)
        self.Buttonpi = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='π',
                                  command=lambda: self.Click('π')).grid(row=2, column=6)

        # 第三行
        self.Buttoncos = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='cos',
                                command=lambda: self.Click('cos')).grid(row=3, column=1)
        self.Button7 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='7',
                              command=lambda: self.Click(7)).grid(row=3, column=2)
        self.Button8 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='8',
                              command=lambda: self.Click(8)).grid(row=3, column=3)
        self.Button9 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='9',
                              command=lambda: self.Click(9)).grid(row=3, column=4)
        self.Multiply = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='*',
                               command=lambda: self.Click("*")).grid(row=3, column=5)
        self.Delivery = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='%',
                               command=lambda: self.Click("%")).grid(row=3, column=6)


        # 第四行
        self.Buttontan = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='tan',
                                command=lambda: self.Click('tan')).grid(row=4, column=1)
        self.Button4 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='4',
                              command=lambda: self.Click(4)).grid(row=4, column=2)
        self.Button5 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='5',
                              command=lambda: self.Click(5)).grid(row=4, column=3)
        self.Button6 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='6',
                              command=lambda: self.Click(6)).grid(row=4, column=4)
        self.Subtraction = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='-',
                                  command=lambda: self.Click("-")).grid(row=4, column=5)  # 减
        self.Left_bracket = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='(',
                                   command=lambda: self.Click('(')).grid(row=4, column=6)

        # 第五行
        self.comma = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text=',',
                         command=lambda: self.Click(',')).grid(row=5, column=1)
        self.Button1 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='1',
                              command=lambda: self.Click(1)).grid(row=5, column=2)
        self.Button2 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='2',
                              command=lambda: self.Click(2)).grid(row=5, column=3)
        self.Button3 = tk.Button(self.calculator, bg='orange', fg="black", padx=15, pady=3, text='3',
                              command=lambda: self.Click(3)).grid(row=5, column=4)
        self.Addition = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='+',
                               command=lambda: self.Click("+")).grid(row=5, column=5)
        self.Right_bracket = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text=')',
                                    command=lambda: self.Click(')')).grid(row=5, column=6)

        # 第六行
        self.log = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='log',
                         command=lambda: self.Click('log')).grid(row=6, column=1)
        self.Button0 = tk.Button(self.calculator, bg='orange', fg="black",height=3,width=3,text='0',
                              command=lambda: self.Click(0)).grid(row=6, column=2)
        self.decimal_point = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='.',
                                    command=lambda: self.Click(".")).grid(row=6, column=3)
        self.Equals = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='=',
                             command=lambda: self.Run()).grid(row=6, column=4)
        # 第七行

        self.Button_pow = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='pow',
                               command=lambda: self.Click('pow')).grid(row=7, column=5)
        self.Button_up_ceil = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='up_ceil',
                                 command=lambda: self.Click('up_ceil')).grid(row=7, column=4)
        self.Button_down_floor = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='down_floor',
                               command=lambda: self.Click('down_floor')).grid(row=7, column=3)
        self.Button_round = tk.Button(self.calculator, bg='powderblue', fg="black", padx=15, pady=3, text='round',
                                  command=lambda: self.Click('round')).grid(row=7, column=2)


    def Click(self, numbers):
        global variable
        variable = variable + str(numbers)
        self.text_input.set(variable)

    def Run(self):
        global variable
        elements = self.text_input.get()
        if elements[0] == 'l':
            try:
                elements = elements.replace('log(', '')
                elements = elements.replace(')', '')
                arr = elements.split(',')
                variable = str('%.4f' % math.log(eval(arr[0]), eval(arr[1])))
                self.equation.set(variable)
            except ValueError:
                self.equation.set('Error!')
        elif elements[0] == 's':
            elements = elements.replace('sin(', '')
            elements = elements.replace(')', '')
            rep = math.pi
            elements = elements.replace('π', str(rep))
            variable = '%.4f' % math.sin(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'c':
            elements = elements.replace('cos(', '')
            elements = elements.replace(')', '')
            rep = math.pi
            elements = elements.replace('π', str(rep))
            variable = '%.4f' % math.cos(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 't':
            elements = elements.replace('tan(', '')
            elements = elements.replace(')', '')
            rep = math.pi
            elements = elements.replace('π', str(rep))
            variable = '%.4f' % math.tan(eval(elements))
            self.equation.set(str(variable))

        elif elements[0] == 'p':
            elements = elements.replace('pow(', '')
            elements = elements.replace(')', '')
            arg = elements.split(',')
            variable = '%.4f' % pow(eval(arg[0]), eval(arg[1]))
            self.equation.set(str(variable))
        elif elements[0] == 'u':
            elements = elements.replace('up_ceil(', '')
            elements = elements.replace(')', '')
            variable = '%.4f' % math.ceil(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'd':
            elements = elements.replace('down_floor(', '')
            elements = elements.replace(')', '')
            variable = '%.4f' % math.floor(eval(elements))
            self.equation.set(str(variable))
        elif elements[0] == 'r':
            elements = elements.replace('round(', '')
            elements = elements.replace(')', '')
            variable = '%.4f' % round(eval(elements))
            self.equation.set(str(variable))


        # elif elements.index('asin') == 0:
        #     elements = elements.replace('asin(', '')
        #     elements = elements.replace(')', '')
        #     variable = '%.4f' % math.asin(eval(elements))
        #     self.equation.set(str(variable))
        #
        # elif elements.index('acos') == 0:
        #     elements = elements.replace('acos(', '')
        #     elements = elements.replace(')', '')
        #     variable = '%.4f' % math.acos(eval(elements))
        #     self.equation.set(str(variable))
        # elif elements.index('atan') == 0:
        #     elements = elements.replace('atan(', '')
        #     elements = elements.replace(')', '')
        #     variable = '%.4f' % math.atan(eval(elements))
        #     self.equation.set(str(variable))
        # elif elements.index('acot') == 0:
        #     elements = elements.replace('acot(', '')
        #     elements = elements.replace(')', '')
        #     variable = '%.4f' % math.acot(eval(elements))
        #     self.equation.set(str(variable))
        else:
            try:
                sumup = '%.4f' % eval(elements)  # 保留四位小数
                self.equation.set(str(sumup))
            except (ZeroDivisionError, SyntaxError, ValueError):  # 其他除0错误，或语法错误和值错误返回Error
                self.equation.set(str('Error!'))




    #
    def ClearDisplay(self):
        global variable
        variable = ""
        self.text_input.set("0")
        self.equation.set("0")


    def BackSpace(self):
        global variable
        len_variable = len(str(variable))
        variable = str(variable)[:len_variable - 1]
        self.text_input.set(variable)


    def Factorial(self):
        global variable
        self.text_input.set('{}!'.format(variable))
        variable = str(math.factorial(eval(variable)))
        self.equation.set(variable)



# 程序的入口
if __name__ == "__main__":
    root = tk.Tk()

    # calculator= tk.Frame(root)
    # calculator.pack()

    root.geometry('800x600')
    my_cal = Cal(root)  # 实例化

    root.mainloop()  # 进入消息循环
