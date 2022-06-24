import os
import pypandoc

def convert_data(file, file_format='html'):
    #output_filename = os.path.splitext(file)[0] + '.' + file_format
    index_point = file.rfind('.')
    print(index_point)
    print(file[:index_point])
    output_filename = file.replace(file[index_point:], '.' + file_format)
    print(output_filename)
    output = pypandoc.convert_file(file, file_format, outputfile=output_filename)
    assert output == "", "Error converting file"

convert_data('readme.html', 'rst')