// Extends card and image height to proper proportions to negate use of scroll bar
let contentHeight = document.getElementById("merch-form").offsetHeight;
let cardHeight = document.getElementById("card").offsetHeight;
if (contentHeight > cardHeight) {
    document.getElementsByClassName("merch-card")[0].style.height = contentHeight + "px"
    document.getElementsByClassName("merch-image-background")[0].style.height = contentHeight + "px"
}

// Removes one from bag total, to a min of 0
document.getElementById("remove-button").addEventListener("click", function() {
    let bag = document.getElementById("in-bag").getElementsByTagName("span")[0];
    let bagContent = parseInt(bag.textContent);
    if (bagContent > 0) {
        bagContent = bagContent - 1;
        bag.textContent = bagContent;
    }
})

// Adds one to bag total, to a max of 99
document.getElementById("add-button").addEventListener("click", function() {
    let bag = document.getElementById("in-bag").getElementsByTagName("span")[0];
    let bagContent = parseInt(bag.textContent);
    if (bagContent < 99) {
        bagContent = bagContent + 1;
        bag.textContent = bagContent;
    }
})