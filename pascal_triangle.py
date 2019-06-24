import sys


def beautify_list(list_object):
    beautified_string = ""
    max_len = 0
    """
    This function is used to beautify a list with 2 dimension for Pascal's Triangle
    """
    for i in list_object[-1]:
        max_len += len(str(i))
    max_len = max_len * 2
    for row in list_object:

        temp = ""
        for item in row:
#             if len(temp) < len(row)+1:
#                 temp += str(item)+" "
#             else:
            temp += str(item)+" "
        temp = temp.center(max_len, ' ')
        print(temp)

def draw_pascals(no_of_rows):
    zen = 1
    output_list = []
    """
    This function is used to generate a 2 dimensional list for Pascal's Triangle
    """
    for i in range(no_of_rows):
        j = 0
        output_list.append([])
        while (j <= i):
            if j == 0 or j == i:
                output_list[i].append(zen)
            else:           
                output_list[i].append(output_list[i-1][j]+output_list[i-1][j-1])
            j += 1
    beautify_list(output_list)


while True:
    try:
        user_entry = input("Enter number of rowz : ")
        if user_entry.lower() == "quit":
            break
#             sys.exit()
        user_entry = int(user_entry) 
        if user_entry > 0:
            draw_pascals(user_entry)
        else:
            print("Length should be greater than zero")
    except ValueError:
        print("Enter only numbers")
    except KeyboardInterrupt:
        print("\nThankzzz")
        sys.exit()
