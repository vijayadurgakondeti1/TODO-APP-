document.getElementById("addForm").addEventListener("submit", function(event) {
    event.preventDefault();
    var taskInput = document.getElementById("todoInput").value;
    if (taskInput.trim() !== "") {
        addTask(taskInput);
        document.getElementById("todoInput").value = "";
    }
});

function addTask(task) {
    var listItem = document.createElement("li");
    listItem.className = "list-group-item";
    listItem.innerText = task;
    document.getElementById("todoList").appendChild(listItem);
}
