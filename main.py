import tkinter as tk
from PIL import Image, ImageTk


class Application(tk.Frame):
    # label Widgetにてpng画像を描画する関数
    def drawLabelPngImg(self):
        # ガベージコレクションが起こり、関数終了後、ローカル変数の場合に画像情報が自動消滅するのを防ぐため、global変数を利用する。
        # 画像の描画は、main関数内で展開される。 → ローカル変数だとmain関数実行時に画像情報が残っていない。 → グローバル変数を利用して、関数終了後も値参照できるようにしておく。
        # グローバル変数、ローカル変数とは? : https://itsakura.com/python-local-global#:~:text=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E5%A4%89%E6%95%B0%E3%81%AF%E9%96%A2%E6%95%B0%E3%81%AE,%E5%A4%89%E6%95%B0%E5%90%8D%E3%81%A7%E3%82%82%E5%8F%AF%E3%81%A7%E3%81%99%E3%80%82
        # ガベージコレクションとは? : https://ja.wikipedia.org/wiki/%E3%82%AC%E3%83%99%E3%83%BC%E3%82%B8%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3#:~:text=%E3%82%AC%E3%83%99%E3%83%BC%E3%82%B8%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%EF%BC%88%E8%8B%B1%3A%20garbage%20collection,%E3%83%9E%E3%83%83%E3%82%AB%E3%83%BC%E3%82%B7%E3%83%BC%E3%81%AB%E3%82%88%E3%81%A3%E3%81%A6%E7%99%BA%E6%98%8E%E3%81%95%E3%82%8C%E3%81%9F%E3%80%82
        global pngImg

        # (画像のパスをお好みでご入力ください。)
        # TkinterのWidgetで画像が扱える形へ変更する。
        pngImg = tk.PhotoImage(file="/path_to/xxx.png")

        # label Widgetを作成する。
        # width : 幅の設定
        # height : 高さの設定
        # image : 画像の設定を行う。
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(width=100, height=100, image=pngImg)

        # label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

    # canvas Widgetにてpng画像を描画する関数
    def drawCanvasPngImg(self):
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Canvasについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        canvas = tk.Canvas(height=100, width=100, bg="white")

        # canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        canvas.pack()

        # (画像のパスをお好みでご入力ください。)
        # TkinterのWidgetで画像が扱える形へ変更する。
        # canvas.photo内に画像情報が保存されるため、グローバル変数を宣言しなくてよくなる。
        canvas.photo = tk.PhotoImage(file="/path_to/xxx.png")

        # Canvasについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        # 第一引数 : x座標位置
        # 第二引数 : y座標位置
        # image : 画像の設定
        canvas.create_image(0, 0, image=canvas.photo)

    # label Widgetにてjpg画像を描画する関数

    def drawLabelJpgImg(self):
        # ガベージコレクションが起こり、関数終了後、ローカル変数の場合に画像情報が自動消滅するのを防ぐため、global変数を利用する。
        # 画像の描画は、main関数内で展開される。 → ローカル変数だとmain関数実行時に画像情報が残っていない。 → グローバル変数を利用して、関数終了後も値参照できるようにしておく。
        # グローバル変数、ローカル変数とは? : https://itsakura.com/python-local-global#:~:text=%E3%82%B0%E3%83%AD%E3%83%BC%E3%83%90%E3%83%AB%E5%A4%89%E6%95%B0%E3%81%AF%E9%96%A2%E6%95%B0%E3%81%AE,%E5%A4%89%E6%95%B0%E5%90%8D%E3%81%A7%E3%82%82%E5%8F%AF%E3%81%A7%E3%81%99%E3%80%82
        # ガベージコレクションとは? : https://ja.wikipedia.org/wiki/%E3%82%AC%E3%83%99%E3%83%BC%E3%82%B8%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3#:~:text=%E3%82%AC%E3%83%99%E3%83%BC%E3%82%B8%E3%82%B3%E3%83%AC%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%EF%BC%88%E8%8B%B1%3A%20garbage%20collection,%E3%83%9E%E3%83%83%E3%82%AB%E3%83%BC%E3%82%B7%E3%83%BC%E3%81%AB%E3%82%88%E3%81%A3%E3%81%A6%E7%99%BA%E6%98%8E%E3%81%95%E3%82%8C%E3%81%9F%E3%80%82
        global jpgImg

        # Tkinter8.6以降でも、標準Tkinterではjpg対応できないため、PILを利用する。
        # 画像に関する公式ドキュメント : https://docs.python.org/ja/3/library/tkinter.html#images
        # openコマンドについて : https://carp.cc.it-hiroshima.ac.jp/~tateyama/Lecture/AppEx/PythonImagePIL.html
        # (画像のパスをお好みでご入力ください。)
        img = Image.open('/path_to/xxx.jpg', 'r')

        # TkinterのWidgetで画像が扱える形へ変更する。
        jpgImg = ImageTk.PhotoImage(img)

        # label Widgetを作成する。
        # width : 幅の設定
        # height : 高さの設定
        # image : 画像の設定を行う。
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(width=100, height=100, image=jpgImg)

        # label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()

    # canvas Widgetにてjpg画像を描画する関数
    def drawCanvasJpgImg(self):
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Canvasについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        canvas = tk.Canvas(height=100, width=100, bg="white")

        # canvas Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        canvas.pack()

        # Tkinter8.6以降でも、標準Tkinterではjpg対応できないため、PILを利用する。
        # 画像に関する公式ドキュメント : https://docs.python.org/ja/3/library/tkinter.html#images
        # openコマンドについて : https://carp.cc.it-hiroshima.ac.jp/~tateyama/Lecture/AppEx/PythonImagePIL.html
        # (画像のパスをお好みでご入力ください。)
        img = Image.open('/path_to/xxx.jpg', 'r')

        # TkinterのWidgetで画像が扱える形へ変更する。
        # canvas.photo内に画像情報が保存されるため、グローバル変数を宣言しなくてよくなる。
        canvas.photo = ImageTk.PhotoImage(img)

        # Canvasについて : https://kuroro.blog/python/ANyM9WLpd0LSXRQAELOj/
        # 第一引数 : x座標位置
        # 第二引数 : y座標位置
        # image : 画像の設定
        canvas.create_image(0, 0, image=canvas.photo)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        self.drawLabelPngImg()
        self.drawCanvasPngImg()
        self.drawLabelJpgImg()
        self.drawCanvasJpgImg()


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
