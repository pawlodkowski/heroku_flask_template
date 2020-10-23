// sanity check
// console.log('script is linked');

var button = document.getElementsByClassName('js-btn')[0];

button.addEventListener('mouseover', function() {
    // console.log('whoa mouseover is running!')
    button.style.background = '#00C9B6';
});

button.addEventListener('mouseout', function() {
    // console.log('and now im mousingOUT!');
    button.style.background = 'white';
});
