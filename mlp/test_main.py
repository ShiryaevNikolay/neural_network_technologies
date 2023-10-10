import numpy as np
from keras.utils import to_categorical
from func import to_category_dict

data = ["Test", "Test", "A", "Nessan", np.NaN, "LKDSFJ", "Nessan"]
set_element_data = [element for _, element in enumerate(list(dict.fromkeys(data)))]
set_index_data = [index for index, _ in enumerate(list(dict.fromkeys(data)))]
category_data = [[int(element) for element in list_data] for list_data in to_categorical(set_index_data)]
dict_data = dict(zip(set_element_data, category_data))
print(dict_data[np.NaN])
# print([[int(element) for element in list_data] for list_data in to_categorical(set_data)])
