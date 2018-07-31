from methodss.primary_function import input_output
from methodss.typos.typo_keyboard.typo_keyboard import typo_keyboard

class test_typo_keyboard(object):
    def __init__(self, name="test_typo_keyboard"):
        self.name = name





# ------------------------------- this is your part ----------------------------------



#create instance of test
inst_test=test_typo_keyboard()

#load data set
dataset = input_output.read_write.read_csv_dataset("../datasets/test.csv")

#apply method
instance_typo=typo_keyboard()
new_dataset=instance_typo.typo_keyboard(dataset,20)

#write to output
input_output.read_write.write_csv_dataset("/home/milad/Desktop/error-generator/New structure/outputs/{}.csv".format(inst_test.name), new_dataset)
