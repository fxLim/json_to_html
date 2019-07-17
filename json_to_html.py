import json


def doctype(key,value):
    str = "<!"+key+" "+value+">"
    return str


def lang(key,value):
    str = '<html lang="'+value+'">'
    return str

def to_html(key, value):
    str = '<'+key+'>'+value+'</'+key+'>'
    return str


def convert_body(output_file, json, count):
    for key, value in json.items():
        is_dict = type(value) == dict
        if is_dict:
            convert_body(value, count+1)
        else:
            output_file.write(count * '\t' + to_html(key, value)+'\n')


def convert_head(output_file, json, count):
    for key,value in json.items():
        if key == 'meta':
            for metaKey, metaValue in value.items():
                if metaKey == 'charset':
                    string_charset = count*'\t'+'<meta charset="'+metaValue+'">'+'\n'
                elif metaKey == 'viewport':
                    string_viewport = count * '\t' + '<meta name="'+metaKey+'" content="' + metaValue['width']
                    string_viewport +=', initial-scale=' + str(metaValue['initial-scale'])+'">\n'
        else:
            string_other =count*'\t'+to_html(key, value)+'\n'
    output_file.write(string_charset+string_other+string_viewport)


def convert_json():
    json_data = json.load(open('input.json', 'r'))
    output_file = open('output.html', 'w')
    for key, value in json_data.items():
        if key == 'body':
            output_file.write('<body>' + '\n')
            convert_body(output_file, json_data[key], 1)
            output_file.write('</body>'+'\n')
        elif key == 'head':
            output_file.write('<head>' + '\n')
            convert_head(output_file, json_data[key], 1)
            output_file.write('</head>'+'\n')
        else:
            if key == 'doctype':
                output_file.write(doctype(key, value)+'\n')
            elif key == 'language':
                output_file.write(lang(key, value)+'\n')
            else:
                print("Mapping for "+key+" not defined")
    output_file.write('</html>')


convert_json()