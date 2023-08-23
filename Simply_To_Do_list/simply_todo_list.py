#To-Do List: 

#	1.	Define the Task Class:
#	•	Create a class named Task.
#	•	Define the __init__ method to initialize attributes like title, description, and due_date.

#	2.	Create the ToDoList Class:
#	•	Create a class named ToDoList.
#	•	Initialize an empty list (tasks) within the __init__ method to store tasks.

#	3.	Implement Methods for the ToDoList Class:
#	•	Define a method named add_task within the ToDoList class.
#	•	Implement the logic to add a task object to the tasks list.
#	•	Define a method named list_tasks to display all tasks.

#	4.	Implement Methods for the Task Class:
#	•	Define methods like mark_as_done and update_due_date within the Task class.

# 5.	Test the Classes:
#	•	Create instances of the ToDoList class.
#	•	Add tasks to the list, list them, and perform actions on tasks.

# ------------------------------------------------------

class Task:
	
	def __init__ (self,title,description, due_date):
		
		self.title = title
		self.description = description
		self.DueDate = due_date
		self.done = False
		
	def mark_as_done (self):
		self.done = True
	
	def update_due_date (self, new_date):
		self.DueDate = new_date
				
# ------------------------------------------------------

class ToDoList:
	def __init__ (self):
		self.task = []
	
	def add_task (self,new_task):
		self.task.append(new_task)
		return ("new task added")
	
	def list_tasks(self):
		for task in self.task:
			if task.done == True:
				status = "Done" 
			else:
				status = "Not Done"
			print(f"Title: {task.title} | Description: {task.description} | Due Date: {task.DueDate} | Status: {status}")
		

# ------------------------------------------------------
# ------------------------------------------------------

my_todo_list = ToDoList()

task1 = Task("Finish Project" , "Python To Do list program" , "2023-08-24")
task2 = Task("Buy groceries" , "Milk, bread, butter" , "2023-08-23")
task3 = Task("Prepare for Exam" , " Math, Algebra , Bio" , "2023-09-10")


# Add tasks to the ToDoList

my_todo_list.add_task(task1)
my_todo_list.add_task(task2)
my_todo_list.add_task(task3)

# List tasks

my_todo_list.list_tasks()

# Mark a task as done and update due date

task1.mark_as_done()

# hange due date of a task

task3.update_due_date("2023-08-30")

print("----------------------------------------------")

# List tasks again
my_todo_list.list_tasks()
