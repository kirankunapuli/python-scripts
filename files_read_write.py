txt = open('files_sample_data.txt')

txt_again = txt.read()

target = open('files_sample_output.txt', 'w')

target.write(txt_again)

target.close()

