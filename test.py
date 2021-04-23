# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg
# 
# # OPTIONAL1 : 
# 
# class MainWindow(qtw.QWidget): 
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Code goes here
# 
#         # Code ends here
#         self.show()
# 
# 
# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='Hello World')
#     sys.exit(app.exec_())



#class Process_desc():
#    def __init__(self):
#        self.desc = "These are the processes: "
#        print(self.desc)
#
#class Process1(Process_desc):
#    def __init__(self):
#        super().__init__()
#        print("This is the first Process")
#
#class Process2(Process_desc):
#    def __init__(self):
#        super().__init__()
#        print("This is the second Process")
#
#class Processes(Process2, Process1):
#    def __init__(self):
#        super().__init__()
#        print("end")
#
#job = Processes()

#class Class_1:
#   def __init__(self):
#       self.name = "Brian"
#
#   def first_function(self):
#           print("Hello there!")
#    
#    
#class Class_2(Class_1):
#    def __init__(self):
#        super().__init__()
#        self.age = 15
#
#    def second_function(self):
#        print("Hello Again!")
#
#
#class Class_3(Class_2):
#    pass
#    #def __init__(self):
#        #super().__init__()
#
#x = Class_3()
#x.first_function()
#print(x.name)

#class Base1:
#    def hello(self):
#        print("Hello!")
#    super().name()
#
#class Base2:
#    def name(self):
#        print("My name is brian!")
#
#class Combine(Base1, Base2):
#    pass
#
#full = Combine()
#full.hello()

#import uuid
#print('hello' + str(uuid.uuid4()))

#numbers = set()
#print(type(numbers))
#for num in numbers:
#    print(num)

import json
import os

#profile_names = set()

print("\nCommands: new | access | remove | quit")

# CREATING/VERIFYING SAVE FILE
if not os.path.isfile('saveTEST.json'):
    open("saveTEST.json", "a+")

# DISPLAYING EXISTING PROFILES
try:
    with open('saveTEST.json') as infile:
        profiles = json.load(infile)
        keys_list = []
        for key in profiles:
            keys_list.append(key)
        print("Available profiles: ", keys_list)
except:
    print('No Current Profiles')
    profiles = {}


# MAIN LOOP
while True:

    cmd = input("\nPlease enter Command: ")

    if cmd == "new":
        newName = input("Name: ")

        # PRE-EXISTING PROFILE CHECKER
        for name in profiles:
            while name == newName:
                print("Sorry, that profile already exists haha")
                newName = input("Name: ")
            

        newData = input("Data: ").split()
        #profile_names.add(newName)
        profiles[newName] = newData
        print(profiles)
        with open('saveTEST.txt', 'a') as f:
            f.write(str(profiles))

    elif cmd == 'access':
        profile_name = input("Please enter profile name: ")
        for name in profiles:
            if name == profile_name:
                print(profiles[profile_name])
        add_prompt = input("Add to Profile? (yes/no): ")
        if add_prompt == 'yes':
            additional_data = input("data: ")
            profiles[profile_name].append(additional_data)

    elif cmd == 'remove':
        pass

    elif cmd == 'quit':
        break

# UPDATES THE .JSON SAVE FILE
with open('saveTEST.json', 'w') as outfile:
    json.dump(profiles, outfile)
quit()
        #new_list = Profile(newName, newData)
