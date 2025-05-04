# Part 1  - Features of python

1. **Easy to Learn and Read**
   Python has a clean and readable syntax that looks like plain English, making it beginner-friendly.

2. **Interpreted Language**
   Python code runs line by line, so you don’t need to compile it before execution.

3. **Dynamically Typed**
   You don’t have to declare variable types; Python figures them out while the program runs.

4. **Object-Oriented**
   Python supports classes and objects, making it easier to structure large and reusable code.

5. **Large Standard Library**
   Python includes a wide range of built-in modules and tools, saving time for developers.

6. **Cross-Platform Compatibility**
   Python works the same on Windows, Mac, or Linux without needing code changes.

7. **Extensive Community Support**
   Python has a huge global community, so it’s easy to find help, tutorials, and libraries.

8. **Support for Multiple Programming Paradigms**
   Python supports object-oriented, procedural, and functional programming styles.

9. **Ideal for Rapid Development**
   With fewer lines of code, Python allows you to build and test applications quickly.

10. **Used in Many Fields**
    Python is widely used in web development, data science, AI, automation, and more.

# Part 2 - Python Concepts

## Example 1

> Today we’re going to explore how to use Python collections—like **lists, sets, dictionaries, and tuples**—to build a real-world mini project: an **Employee Management and Attendance Tracker**.
>
> In any real company or system, employees are identified by **unique employee IDs**—like E001, E002, and so on. Using IDs makes it easy to track employees even if some of them have the same name.
>
> So, we’ll use a **dictionary** where each key is an employee ID, and the value is another dictionary that stores the employee’s **name**, **department**, and their **attendance record**.
>
> Attendance will be tracked as a **list of dates**—one list per employee—so we can easily add new attendance entries as days go by.
>
> To get a list of all the departments in our company, we use a **set**. A set automatically removes duplicates, which helps us get only the **unique departments** from all employee records.
>
> Now, let’s say we want to find all employees named “Alice.” Since we’re using IDs, we simply scan through the values and collect all IDs where the name is “Alice.” We can do this neatly using a **list comprehension**.
>
> Similarly, if we want to find out who was present on a specific day, like May 2nd, we loop through the attendance lists and pick out the matching employees. Again, this is a perfect place to use a list comprehension.
>
> To store **company holidays**, we use a **tuple**—which is a type of collection that cannot be changed after it’s created. This ensures the holiday list stays safe and unmodified.
>
> So in this small and practical program, we’ve used:
>
> * **Lists** to store daily attendance per employee,
> * **Dictionaries** to store detailed employee records using IDs,
> * **Sets** to find unique departments,
> * **Tuples** to store fixed holidays,
> * and **List comprehensions** to filter and extract data quickly.
>
> This is a great example of how Python collections help us build simple systems that feel close to real life.
>
> Thanks for following along—and keep practicing by solving more everyday problems with Python!
> 
## Example 2

The scenario simulates a basic ATM machine where the user can repeatedly choose actions (check balance, deposit money, withdraw money, etc.) until they decide to exit.
