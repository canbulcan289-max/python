import json

todolist={"isim":"can"
      }


    
def remove():
   with open("todolist.json","r",encoding="utf-8") as file:
      delete_list=json.load(file)
   remove_key=input("Enter the number of task you want to remove:")
   if remove_key in delete_list:
      delete_list.pop(remove_key)
   with open("todolist.json","w",encoding="utf-8") as file:
      json.dump(delete_list,file,indent=4)

with open("todolist.json","r",encoding="utf-8") as file:
   new_list=json.load(file)
   print(new_list)