$(document).ready(function () {
    enableslide();
    
});



function enableslide() { 
    let isDown = false;
    let startX;
    let scrollLeft;
    const slider = document.querySelector('#slideshow');
    
    const end = () => {
        isDown = false;
      slider.classList.remove('active');
    }
    
    const start = (e) => {
      isDown = true;
      e.preventDefault();
      slider.classList.add('active');
      startX = e.pageX || e.touches[0].pageX - slider.offsetLeft;
      scrollLeft = slider.scrollLeft;	
    }
    
    const move = (e) => {
        if(!isDown) return;
    
      e.preventDefault();
      const x = e.pageX || e.touches[0].pageX - slider.offsetLeft;
      const dist = (x - startX);
      slider.scrollLeft = scrollLeft - dist;
    }
    
    (() => {
        let elHeight = $('#slideshow').width();
        let offset = (elHeight / 2) + (elHeight / 3.9);
        slider.scrollLeft = offset;
        
        slider.addEventListener('mousedown', start);
        slider.addEventListener('touchstart', start);
    
        slider.addEventListener('mousemove', move);
        slider.addEventListener('touchmove', move);
    
        slider.addEventListener('mouseleave', end);
        slider.addEventListener('mouseup', end);
        slider.addEventListener('touchend', end);
    })();
}