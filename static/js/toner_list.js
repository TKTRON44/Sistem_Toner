// toner_list.js
document.addEventListener("DOMContentLoaded", function() {
  var dropdownBtn = document.querySelector(".dropdown-btn");
  var dropdownContent = document.querySelector(".dropdown-content");
  var tonerOptions = document.querySelectorAll(".toner-option");
  var confirmationMessage = document.getElementById("confirmation-message");

  dropdownBtn.addEventListener("click", function() {
    dropdownContent.classList.toggle("show");
  });

  tonerOptions.forEach(function(option) {
    option.addEventListener("click", function(event) {
      event.preventDefault();
      var selectedTonerId = option.getAttribute("data-id");
      var selectedTonerModel = option.getAttribute("data-model");

      $.ajax({
        type: "POST",
        url: "/subtract_toner/",
        data: {
          toner_id: selectedTonerId,
          action: "subtract"
        },
        success: function(response) {
          confirmationMessage.textContent = "Ação concluída com sucesso: Toner " + selectedTonerModel + " subtraído.";
        },
        error: function(xhr, status, error) {
          console.error(error);
        }
      });

      // Atualize a caixa de seleção com o toner selecionado
      dropdownBtn.textContent = selectedTonerModel;

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
