import datetime
import Main


if __name__ == '__main__':
    chose = input("1 - 1МБ, 2 - 10МБ, 3 - 100МБ:   ")
    if chose == "1":
        file = open("D:/Python/CryptoLab/Test/test_1MB.txt", 'r')
        input_text = file.read()
        start_time = datetime.datetime.now()
        Main.sha1_Function(input_text)
        end_time = datetime.datetime.now()
        print("Время вычислений = ", (end_time - start_time))
    if chose == "2":
        file = open("D:/Python/CryptoLab/Test/test_10MB.txt", 'r')
        input_text = file.read()
        start_time = datetime.datetime.now()
        Main.sha1_Function(input_text)
        end_time = datetime.datetime.now()
        print("Время вычислений = ", (end_time - start_time))
    if chose == "3":
        file = open("D:/Python/CryptoLab/Test/test_100MB.txt", 'r')
        input_text = file.read()
        start_time = datetime.datetime.now()
        Main.sha1_Function(input_text)
        end_time = datetime.datetime.now()
        print("Время вычислений = ", (end_time - start_time))
