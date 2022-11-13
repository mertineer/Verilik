// SMOOTH SCROLLING
$(document).ready(function(){
  
  $("a").on('click', function(event) {

    
    if (this.hash !== "") {
      
      event.preventDefault();

      var hash = this.hash;

      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        
        window.location.hash = hash;
      });
    } 
  });
});

// REVEAL SCROLLING
window.addEventListener('scroll', reveal);

function reveal(){
  var reveals = document.querySelectorAll('.reveal');

  for(var i = 0; i < reveals.length; i++){
    var windowheight = window.innerHeight;
    var revealtop = reveals[i].getBoundingClientRect().top;
    var revealpoint = 150;

    if(revealtop < windowheight - revealpoint){
      reveals[i].classList.add('active');
  }
    else{
      reveals[i].classList.remove('active');
    }
  }
}


// DARK MODE
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
}
