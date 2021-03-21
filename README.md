# Thomas Plant - Bar Project

### Project Overview
For my project I have decided to base it on a bar computer sysetem, incorporating multiple database with multiple tables with at least one relationship between two of them, a front end web application with CRUD functionality using python and flask, as well as providing sufficient testing and overall documentation of the project, including a Trello kanban-style board to track everything that needs to be done and what has already been completed. 

### What I will be using to complete this project
To complete this project to a high standard I will be using various programs, languages and systems and utilise all of the various tools that they offer. Some of which will be:
* Python
* Git
* Visual Studio Code
* Github
* Trello
* Flask
* HTML
* Google Cloud Platform  

Many of these programs and systems work symbiotically so it will not only make the project work more efficiently but it will also utilise many of the tools and capabilities available by using them.

### Creating a Virtual Machine
By using a virtaul machine (VM), it allows you to store the code and the system externally, so not only does it save you having to use all your own storage space and RAM, but it also allows you to access it from anywhere so it means that the application will be much more flexible and universal.

### Creating the Databases
For the database I will include a 5 tables:
* Customer
* Bartender
* Drinks
* Payment
* Orders

The Orders table will include the relationships and foreign keys, displaying the specific ID numbers that link to each of the other tables (Customer_ID, Employee_ID, etc.) These tables will also need to have complete CRUD functionality so they will need to be updatable from the web application, meaning there will be many different pages, forms and templates used so that the web page is easily navigated and simple to use.  

![datatables](https://user-images.githubusercontent.com/79214361/110125741-965d8600-7dbb-11eb-9f87-58687a695df6.png) 

### Planning/Documentation
Over the duration of this project I planned each of the steps I needed to complete before the end by using a Trello kanban board, so that it is clear and simply laid out, what I have finished and what I am still yet to complete. By doing this I will ensure that my time is managed well and ensure that everything I need to complete is finished on time. As well as this I shall be uploading all of the saved code onto Github so that it is all readily available to view, and I can see the various changes made along the way by using branching and viewing the various different commits to cleary show my working process.  

![trelloboard](https://user-images.githubusercontent.com/79214361/111922306-fb3dff00-8a90-11eb-9e2f-3de295bef3f8.png)

Link to the final Kanban board: https://trello.com/b/qQsce79b/kanban-template

### Testing
The database will need to be tested thoroughly throughout the process to make sure that the code is reliable and doesn't contain any bugs or faults. I will ensure this by making dedicated test suites to fully test the code to make sure it works and is consistent.  
First of all I tested the initial database to make sure at the very least that had full test coverage.

![test1](https://user-images.githubusercontent.com/79214361/111921229-5cfb6a80-8a8b-11eb-905f-326fc78e59dc.png)
  
Then after the databases were sufficiently tested, I decided to continue through writing the rest of the code, for all of the functions and pages for my project. I then tesetd all of the rest of the code gradually as it was being written, however I found it took a lot longer to write individual tests for the sections of code and instead opted for doing a few sections at a time, as I found thagt some of the tests were very similar to each other.

![test2](https://user-images.githubusercontent.com/79214361/111921052-6932f800-8a8a-11eb-82eb-7ace5148da22.png)  

After I had finished all of the sections of code I found that it became a lot easier to test any areas I'd missed all at once, and so began going through each of the individual missed lines, trying to test as many as possible.

![test3](https://user-images.githubusercontent.com/79214361/111921111-b1eab100-8a8a-11eb-8933-9e63b0622d04.png)

After some more rigorous testing, I had managed to get each of the sectiions in the "application" folder to past 80% coverage, I then made sure the whole project was covered just as thoroughly, and eventually managed to achieve 87% test coverage for the enitre project.

![test4](https://user-images.githubusercontent.com/79214361/111921473-af895680-8a8c-11eb-9411-e72effb0b10f.png)  

### Web Application Deployment

For the web application I wanted there to be a central homepage and then links to all of the other sections of the website, each with their own CRUD functionality, so that each part of the website could be added to, changed and updated by the user without having to alter the back-end code.

![homepage](https://user-images.githubusercontent.com/79214361/111923776-b4ec9e00-8a98-11eb-8423-159145f855a5.png)  

Then on each page there would be the table with all of the previous data, and multiple fields to add in the new data.

![image](https://user-images.githubusercontent.com/79214361/111924273-8f14c880-8a9b-11eb-8958-4028c179a2c0.png)


Each of the data entries on each of the individual pages, would all have an update and delete function, so that they would all conform to CRUD functionality. Although I didnt use any program to make the web application look particularly neat or presentable, I did encorpatate a table and table spacings to make te pages all easier to read.

### Conclusion
In conclusion, I have managed to submit my project with all key components, capable of CRUD functionality and by using all of the required programs, features and tools set out for this project. I found much of this project challenging and had to solve many problems and issues along the way, however I feel that in doing so I have developed a much more comprehensive understanding about how certain programs work, the specific aspects of working on a project of this scope and also developed a better understanding of what the role of a DevOps consultant is and a lot of the responsibilities that I could be faced with in the future.
