
from error_generator.api.error_generator_api import Error_Generator
from error_generator.strategies.typos.typo_butterfingers.typo_butterfingers import Typo_Butterfingers

from error_generator.strategies.utilities.list_selected import List_selected
from error_generator.strategies.utilities.input_output import Read_Write

class Test_Typo_butterfingers(object):
    def __init__(self, name="test_typo_butterfingers"):
        self.name = name





# ------------------------------- this is test part ----------------------------------


dataset,dataframe = Read_Write.read_csv_dataset("../datasets/test.csv")

mymethod=Typo_Butterfingers()


myselector=List_selected()


mygen=Error_Generator()
new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=20,dataset=dataset,mute_column=[])


# #create instance of test
inst_test=Test_Typo_butterfingers()


#write to output
Read_Write.write_csv_dataset("../outputs/{}.csv".format(inst_test.name), new_dataset)

