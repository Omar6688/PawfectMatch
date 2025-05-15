// Confirm before delete
document.addEventListener("DOMContentLoaded", function () {
    // Confirm delete buttons
    const deleteButtons = document.querySelectorAll(".confirm-delete");
  
    deleteButtons.forEach((button) => {
      button.addEventListener("click", function (event) {
        const confirmed = confirm("Are you sure you want to delete this?");
        if (!confirmed) {
          event.preventDefault();
        }
      });
    });
  
    // Scroll-to-top button
    const scrollBtn = document.getElementById("scrollTopBtn");
  
    if (scrollBtn) {
      window.addEventListener("scroll", function () {
        if (window.scrollY > 300) {
          scrollBtn.style.display = "block";
        } else {
          scrollBtn.style.display = "none";
        }
      });
  
      scrollBtn.addEventListener("click", function () {
        window.scrollTo({
          top: 0,
          behavior: "smooth",
        });
      });
    }
  });
  