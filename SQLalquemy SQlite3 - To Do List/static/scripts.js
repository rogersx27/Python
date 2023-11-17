function validateForm() {
    // Obtener el valor del campo de tarea
    var taskContent = document.forms["taskForm"]["content-task"].value;

    // Verificar si el campo está vacío
    if (taskContent.trim() === "") {
        // evita la carga de página
        event.preventDefault();
        // Mostrar la alerta
        document.getElementById("alert").style.display = "block";
        // Evitar que el formulario se envíe
        return false;
    } else {
        // Ocultar la alerta si el campo no está vacío
        document.getElementById("alert").style.display = "none";
        // Permitir que el formulario se envíe
        return true;
    }
}