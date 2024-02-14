// this code will be executed after page load
(function() {
  console.log('after.js executed');

  (function(){
    let images = document.querySelectorAll('img');
    images.forEach((img) => {
        img.src = chrome.runtime.getURL('imgs/villainess.jpeg');
      })
  })();

})();
