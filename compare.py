import sys
import json


def read_file(file_dir):
    with open(file_dir) as file_in:
        return json.load(file_in)


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prRed(skk): print("\033[91m {}\033[00m".format(skk), end='', sep ='')


def main():
    my_results_dir = sys.argv[1]
    correct_results_dir = sys.argv[2]

    my_results = read_file(my_results_dir)
    correct_results = read_file(correct_results_dir)

    my_results_arr = list(my_results.values())
    correct_results_arr = list(correct_results.values())

    error_sum = 0
    all_sum = 0

    for index in range(len(my_results_arr)):
        is_OK = True
        i_prev = 0
        print(list(my_results.keys())[index], end='')
        for i in range(len(my_results_arr[index])):
            all_sum += correct_results_arr[index][i]
            if my_results_arr[index][i] != correct_results_arr[index][i]:
                if is_OK == True:
                    prRed("NOK\t")
                    print("[", end='')
                is_OK = False
                for print_index in range(i_prev, i):
                    print(my_results_arr[index][print_index], ", ", end='', sep='')
                prRed(my_results_arr[index][i])
                print("(", correct_results_arr[index][i], "), ", end='', sep='')
                error_sum += abs(correct_results_arr[index][i] - my_results_arr[index][i])
                i_prev = i + 1
        if not is_OK:
            for print_index in range(i_prev, 15):
                print(my_results_arr[index][print_index], ", ", end='', sep='')
        if not is_OK:
            print("]", end='')
            print("")
        else:
            prGreen("100% OK")

    print("\n\nLiczba błędów: ", end='')
    prRed(error_sum)
    print("\nLiczba żelków: ", end='')
    prGreen(all_sum)
    print("Skuteczność programu: ", end='')
    prGreen(round((all_sum-error_sum)/all_sum, 3))


if __name__ == '__main__':
    main()