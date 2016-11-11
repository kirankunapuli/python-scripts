txt = open('files_sample_data.txt')

txt_again = txt.read()

txt_rev = txt_again[::-1]

print(txt_rev)
