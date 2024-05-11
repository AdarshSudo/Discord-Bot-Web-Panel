// -------------------HOME HTML---------------------
// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {
  
        if (this.hash !== "") {
  
            event.preventDefault();
  
            var hash = this.hash;
  
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
  });
  
  // navbar toggle
  $('#nav-toggle').click(function(){
    $(this).toggleClass('is-active')
    $('ul.nav').toggleClass('show');
  });
  
  // Check for saved dark mode preference
  const currentTheme = localStorage.getItem('theme');
  if (currentTheme === 'dark') {
      document.body.classList.add('dark-mode');
      document.getElementById('darkModeToggle').checked = true;
  }
  
  // Toggle dark mode
  document.getElementById('darkModeToggle').addEventListener('change', function() {
      if (this.checked) {
          document.body.classList.add('dark-mode');
          localStorage.setItem('theme', 'dark');
      } else {
          document.body.classList.remove('dark-mode');
          localStorage.setItem('theme', 'light');
      }
  });
