# 注意，chinese_labels里面的映射关系是：（ID：汉字）
import pickle


def get_label_dict(pkl_file_path):
    f = open(pkl_file_path, 'rb')
    label_dict = pickle.load(f)
    f.close()
    return label_dict


def set_label_dict(pkl_file_path, dict):
    pickle_name_file = open(pkl_file_path, 'wb')
    pickle.dump(dict, pickle_name_file, 0)
    pickle_name_file.close()


def read_txt(txt_file_path):
    f = open(txt_file_path, 'rb')
    content = f.read()
    f.close()
    return bytes.decode(content)

if __name__ == "__main__":

    content = read_txt('./所有汉字.txt')
    content = content.replace("\r\n","")
    print(len(content))


    # 将汉字的label读入，得到（ID：汉字）的映射表label_dict
    label_dict = get_label_dict('./chinese_labels_new')

    char_list = []  # 汉字列表
    value_list = []  # label列表
    for (value, chars) in label_dict.items():
        #print(value, chars)
        char_list.append(chars)
        value_list.append(value)

    index = 1
    for word in content:
        if word in char_list:
            print(word,end="，")
        else:
            label_dict[len(value_list) + index] = word
            index = index +1
    print()
    print(len(label_dict))

    set_label_dict('./chinese_labels_all', label_dict)
