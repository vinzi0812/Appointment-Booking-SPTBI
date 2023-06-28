document.getElementById("form2").addEventListener("click", function (event) {
  var confirmDelete = confirm("Are you sure you want to delete?");
  if (confirmDelete) {
    document.getElementById("someForm").submit(); // Submit the form if confirmed
  }
});