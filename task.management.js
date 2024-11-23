document.getElementById('task-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const taskName = document.getElementById('task-name').value;
    const taskDescription = document.getElementById('task-description').value;
    const dueDate = document.getElementById('due-date').value;
    const priority = document.getElementById('priority').value;

    // Create a new task item
    const taskItem = document.createElement('li');
    taskItem.innerHTML = `
        <span>${taskName}</span>
        <span>${taskDescription}</span>
        <span>${dueDate}</span>
        <span>${priority}</span>
        <button>Mark as Complete</button>
        <button>Delete</button>
        
    `;

    // Add the task item to the task list
    document.getElementById('task-list').appendChild(taskItem);
   // ... (rest of your code)
    
        // Add the 'show' class to the new task item
        taskItem.classList.add('show');
    
        // Add the task item to the task list
        document.getElementById('task-list').appendChild(taskItem);
    
        // ... (rest of your code)
    // Clear the form fields
    document.getElementById('task-form').reset();
    document.getElementById('task-form').addEventListener('submit', function(event) {
        event.preventDefault();
    
     
    });
});