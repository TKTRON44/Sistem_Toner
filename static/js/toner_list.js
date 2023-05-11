// toner_list.js
document.addEventListener("DOMContentLoaded", function() {
  var dropdownBtn = document.querySelector(".dropdown-btn");
  var dropdownContent = document.querySelector(".dropdown-content");
  var tonerOptions = document.querySelectorAll(".toner-option");

  dropdownBtn.addEventListener("click", function() {
    dropdownContent.classList.toggle("show");
  });

  tonerOptions.forEach(function(option) {
    option.addEventListener("click", function(event) {
      event.preventDefault();
      var selectedToner = option.getAttribute("data-model");
      // Faça algo com o toner selecionado
      console.log("Toner selecionado:", selectedToner);

      // Atualize a caixa de seleção com o toner selecionado
      dropdownBtn.textContent = selectedToner;

      // Oculte o dropdown após selecionar um toner
      dropdownContent.classList.remove("show");
    });
  });

  window.addEventListener("click", function(event) {
    if (!event.target.matches(".dropdown-btn")) {
      dropdownContent.classList.remove("show");
    }
  });
});
