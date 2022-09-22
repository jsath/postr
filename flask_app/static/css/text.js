

function displayScroll(){
    let messagedisplay = document.querySelector('.messagedisplay');
    messagedisplay.scrollTop = messagedisplay.scrollHeight;
}

setInterval(displayScroll, 150);