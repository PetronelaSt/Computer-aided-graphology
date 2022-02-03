from PIL import Image
from keras.preprocessing import image
from keras.models import load_model
from Croping import Crop_from_dir_to
import os, os.path

# write dir with scans
imgInputDir = "Input_img/"
imgCharsDir = "Output_img/"
# select person sken
personDir = imgCharsDir + "o01/"
# do not change
imagePath = ""

def get_prediction(model, img_file):
    test_image = image.load_img(img_file)
    test_image = image.img_to_array(test_image)
    test_image.resize(1, 28, 28, 1)
    # print(test_image.shape)
    prediction = model.predict(test_image)
    return prediction.argmax(-1)


def A():
    print("A")
    prediction = get_prediction(load_model('models/cnn_model_abig.h5'), imagePath)
    get_characteristics_for_A(prediction[0])


def a():
    print("a")
    prediction = get_prediction(load_model('models/cnn_model_a.h5'), imagePath)
    get_characteristics(prediction[0])


def B():
    print("B")


def b():
    print("b")


def Cc():
    print("C/c")


def D():
    print("D")


def d():
    print("d")
    prediction = get_prediction(load_model('models/cnn_model_d.h5'), imagePath)
    get_characteristics_for_d(prediction[0])


def E():
    print("E")


def e():
    print("e")


def F():
    print("F")


def f():
    print("f")


def G():
    print("G")


def g():
    print("g")


def H():
    print("H")


def h():
    print("h")


def I():
    print("I")


def i():
    print("i")


def J():
    print("J")


def j():
    print("j")


def Kk():
    print("K/k")


def L():
    print("L")


def l():
    print("l")


def M():
    print("M")


def m():
    print("m")
    prediction = get_prediction(load_model('models/cnn_model_m.h5'), imagePath)
    get_characteristics_for_m(prediction[0])


def N():
    print("N")


def n():
    print("n")


def Oo():
    print("O/o")


def Pp():
    print("P/p")


def Q():
    print("Q")


def q():
    print("q")


def R():
    print("R")


def r():
    print("r")


def Ss():
    print("S/s")


def T():
    print("T")


def t():
    print("t")
    prediction = get_prediction(load_model('models/cnn_model_t.h5'), imagePath)
    get_characteristics_for_t(prediction[0])


def Uu():
    print("U/u")


def Vv():
    print("V/v")


def Ww():
    print("W/w")


def Xx():
    print("X/x")


def Yy():
    print("Y/y")


def Zz():
    print("Z/z")


def get_characteristics_for_A(argument):
    switcher = {
        # Labels for A
        1: "Neistý človek",
        2: "Stabilný a sebavedomý človek"
    }
    print(switcher.get(argument, "Pre toto písmeno neexistuje charakteristika."))


def get_characteristics(argument):
    switcher = {
        # Labels for a
        1: "Introvert",
        2: "Extrovert, Komunikatívny človek",
        3: "Láskavý človek",
        4: "Rezervovaný človek",
        5: "Vytrvalý človek",
        6: "Láskavý introvert",
        7: "Rezervovaný introvert",
        8: "Vytrvalý introvert",
        9: "Láskavý extrovert",
        10: "Rezervovaný extrovert",
        11: "Vytrvalý extrovert"
    }
    print(switcher.get(argument, "Pre toto písmeno neexistuje charakteristika."))


def get_characteristics_for_d(argument):
    switcher = {
        # for d
        1: "Človek s limitovanými ideálmi",
        2: "Idealistický, intelektuálny, veriaci sebavedomý a úprimný človek",
        3: "Vysoko intelektuálny človek"

    }
    print(switcher.get(argument, "Pre toto písmeno neexistuje charakteristika."))


def get_characteristics_for_m(argument):
    switcher = {
        # for m
        1: "Skromná osoba s nedostatkom sebadôvery",
        2: "Človek v rovnovahe osobnosti, má dobrú sebaúctu",
        3: "Sebavedomý človek, niekedy až egocentrický",
        4: "Človek vnímajúci svoju hodnotu na základe rodiny a vzťahov",
        5: "Človek posudzujúci svoju hodnotu na základe okolia"
    }
    print(switcher.get(argument, "Pre toto písmeno neexistuje charakteristika."))


def get_characteristics_for_t(argument):
    switcher = {
        # for t
        1: "Hanblivý človek s problémamy dôverovať",
        2: "Racionálny človek so sebareflexiou",
        3: "Vášnivý človek"
    }
    print(switcher.get(argument, "Pre toto písmeno neexistuje charakteristika."))


def get_letter(argument):
    switcher = {
        1: A,
        2: a,
        3: B,
        4: b,
        5: Cc,
        6: D,
        7: d,
        8: E,
        9: e,
        10: F,
        11: f,
        12: G,
        13: g,
        14: H,
        15: h,
        16: I,
        17: i,
        18: J,
        19: j,
        20: Kk,
        21: L,
        22: l,
        23: M,
        24: m,
        25: N,
        26: n,
        27: Oo,
        28: Pp,
        29: Q,
        30: q,
        31: R,
        32: r,
        33: Ss,
        34: T,
        35: t,
        36: Uu,
        37: Vv,
        38: Ww,
        39: Xx,
        40: Yy,
        41: Zz
    }
    func = switcher.get(argument, "Nie je písmenom.")
    func()


if __name__ == "__main__":
    print("Preprocessing ...")
    Crop_from_dir_to(imgInputDir, imgCharsDir)

    imgIn_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png"]

    for file in os.listdir(personDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        imgIn_path_list.append(os.path.join(personDir, file))

    # loop through image_path_list to open each image
    for imagePath in imgIn_path_list:
        print("Starting prediction for: " + imagePath)
        letter = get_prediction(load_model('models/cnn_model_all.h5'), imagePath)
        # print(letter[0])
        get_letter(letter[0])
