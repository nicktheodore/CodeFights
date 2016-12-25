def brAIlle(message):

    # Dictionary of braille characters
    braille_ch = {
     "#        ":'a',
     "#  #     ":'b',
     '# #      ':'c',
     '# #  #   ':'d',
     '#    #   ':'e',
     '# ##     ':'f',
     '# ## #   ':'g',
     '#  # #   ':'h',
     '  ##     ':'i',
     '  ## #   ':'j',
     '#     #  ':'k',
     '#  #  #  ':'l',
     '# #   #  ':'m',
     '# #  ##  ':'n',
     '#    ##  ':'o',
     '# ##  #  ':'p',
     '# ## ##  ':'q',
     '#  # ##  ':'r',
     '  ##  #  ':'s',
     '  ## ##  ':'t',
     '#     # #':'u',
     '#  #  # #':'v',
     '  ## #  #':'w',
     '# #   # #':'x',
     '# #  ## #':'y',
     '#    ## #':'z',
     '  #  ## #':'#'
    }

    braille_num = {
     "#        ":'1',
     "#  #     ":'2',
     '# #      ':'3',
     '# #  #   ':'4',
     '#    #   ':'5',
     '# ##     ':'6',
     '# ## #   ':'7',
     '#  # #   ':'8',
     '  ##     ':'9',
     '  ## #   ':'0',
     '  #  ## #':'#'
     }

    ch_dig = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5',
        'f': '6',
        'g': '7',
        'h': '8',
        'i': '9',
        'j': '0',
        '#': ''

    }

    # Keeps only the first 3 lines of original message, allowing others to be added in sequence
    # without changing the line count.Ellipsis
    adj_message = message[:3]

    # Adjustment algorithms to
    if len(message) < 3:
        return "[?]"

    # Cases up from 4 to 6 then greater
    elif len(message) == 4:
        for i_one in range(3, len(message), 3):
            adj_message[0] += message[i_one]

        print("Step 1: ", adj_message)

    elif len(message) == 5:
        for i_one in range(3, len(message), 3):
            adj_message[0] += message[i_one]
        for i_two in range(4, len(message), 3):
            adj_message[1] += message[i_two]

        print("Step 1: ", adj_message)

    elif len(message) >= 6:
        for i_one in range(3, len(message), 3):
            adj_message[0] += message[i_one]
        for i_two in range(4, len(message), 3):
            adj_message[1] += message[i_two]
        for i_three in range(5, len(message), 3):
            adj_message[2] += message[i_three]

        print("Step 1: ", adj_message)

    ## For readability in the console
    print(2 * '\n')
    print("Step 1 readable: ", '\n')
    print('\n'.join(adj_message))
    print(2 * '\n')

    ########################################################
    longest = max(len(adj_message[0]), len(adj_message[1]), len(adj_message[2]))
    for i in range(len(adj_message)):
        if len(adj_message[i]) < longest:
            spaces_added = int(longest - len(adj_message[i])) * " "
            adj_message[i] += spaces_added
    print("Step 2:", '\n')
    print('\n'.join(adj_message))
    print(len(adj_message), adj_message)

    print(len(adj_message[0]), len(adj_message[1]), len(adj_message[2]))
    ########################################################
    new_output = ""
    space_columns_str = ""
    for i in range(len(adj_message)):
        for j in range(len(adj_message[i])):
            if (j+1) % 4 == 0 and j != 0:
                space_columns_str += adj_message[i][j]
            else:
                new_output += adj_message[i][j]

    print("Step 3: ", '\n')
    print(new_output)
    print(len(new_output))
    print('\n')


    print(space_columns_str)
    #print(len(space_columns))




    space_columns = [space_columns_str[i:i+3] for i in range(0, len(space_columns_str), 3)]
    list_output = [new_output[i:i+3] for i in range(0, len(new_output), 3)]

    print("Step 4: ", '\n')
    print(list_output)
    print(len(list_output))
    #print(space_columns)


    # Cuts off extra (ex10)
    #for i in range(3):
    #    if len(list_output)%3 != 0:
    #        list_output.pop()

    print(list_output)

    list_output_ordered = []
    space_columns_ordered = []

    for i in range(int(len(list_output)/3)):
        list_output_ordered.append(list_output[i::int(len(list_output)/3)])

    for i in range(int(len(space_columns_str)/3)):
        space_columns_ordered.append(space_columns_str[i::int(len(space_columns_str)/3)])



    print("Step 5: ", '\n')
    print(list_output_ordered)
    print(space_columns_ordered)



    joined = []

    for i in range(len(list_output_ordered)):
        joined.append(''.join(list_output_ordered[i]))

    print("Step 5: ", '\n')
    print(joined)

    ## Build the dictionary, search for letters with conditions for spaces
    ## and invalids, create the final string.

    for i in range(len(space_columns_ordered)):
        if '#' in space_columns_ordered[i]:
            print(i)
            joined[i] = '#########'
            joined[i+1] = '#########'

    output_string = ""
    for i in range(len(joined)):
        if joined[i] in braille_ch.keys():
            output_string += braille_ch[joined[i]]

        if joined[i] not in braille_ch.keys():
            output_string += '?'

        if (joined[i][1] or joined[i][4] or joined[i][7]) == '#':
            output_string += '?'

    print(joined)
    print(output_string)

    ## Regex to identify and condense multiple [?] symbols, and identify numbers.
    rgx_null = r"[?]+"
    rgx_digits = r"(#[a-j]+#?)"

    digits_list = re.findall(rgx_digits, output_string)
    digits_string = ""

    for i in range(len(digits_list)):
        for j in range(len(digits_list[i])):
            digits_string += ch_dig[digits_list[i][j]]

        digits_list[i] = digits_string


    print(digits_string, digits_list)

    output_string = re.sub(rgx_null, r"[?]", output_string)

    for i in range(len(digits_list)):
        output_string = re.sub(rgx_digits, digits_list[i], output_string)

    print(output_string)

    return output_string
