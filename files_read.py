txt = open('files_sample_data.txt')

txt_again = txt.read()

txt_list = txt_again.split('\n')

txt_list.reverse()

print(txt_list)

# txt_again.reverse()

# print(txt_again)

