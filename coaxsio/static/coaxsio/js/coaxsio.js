//Set depression effect on .key-white with adjacent .key-black
var findKeyWhite = document.querySelectorAll(".key-white");
findKeyWhite.forEach(keyWhiteEvent);
function keyWhiteEvent(keyWhite, keyWhiteIndex) {

    keyWhite.addEventListener('mouseover', function() {
        if(keyWhite.nextSibling.nextSibling != null && keyWhite.nextSibling.nextSibling.classList.contains("key-black")){
            keyWhite.nextSibling.nextSibling.classList.add("key-white-depressed-bottom");
        }
        if(keyWhite.previousSibling.previousSibling != null && keyWhite.previousSibling.previousSibling.classList.contains("key-black")){
            keyWhite.previousSibling.previousSibling.classList.add("key-white-depressed-top");
        }
    });

    keyWhite.addEventListener('mouseout', function() {
        if(keyWhite.nextSibling.nextSibling != null && keyWhite.nextSibling.nextSibling.classList.contains("key-black")){
            keyWhite.nextSibling.nextSibling.classList.remove("key-white-depressed-bottom");
        }
        if(keyWhite.previousSibling.previousSibling != null && keyWhite.previousSibling.previousSibling.classList.contains("key-black")){
            keyWhite.previousSibling.previousSibling.classList.remove("key-white-depressed-top");
        }
    });

}
