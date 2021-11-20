// Extends card and image height to proper proportions to negate use of scroll bar
let contentHeight = document.getElementById("card-body").offsetHeight;
let cardHeight = document.getElementById("card").offsetHeight;
if (contentHeight > cardHeight) {
    document.getElementsByClassName("merch-card")[0].style.height = contentHeight + "px";
    document.getElementsByClassName("merch-image-background")[0].style.height = contentHeight + "px";
}

//-------------------- Form and form control for quantity
let bag = document.getElementById("in-bag").getElementsByTagName("input")[0];

// Removes one from bag total, to a min of 1
document.getElementById("remove-button").addEventListener("click", function() {
    let bagContent = parseInt(bag.value);
    if (bagContent > 1) {
        bagContent = bagContent - 1;
        bag.value = bagContent;
    }
});

// Adds one to bag total, to a max of 99
document.getElementById("add-button").addEventListener("click", function() {
    let bagContent = parseInt(bag.value);
    if (bagContent < 99) {
        bagContent = bagContent + 1;
        bag.value = bagContent;
    }
});

// Doesn't allow users to change numbers with direct keyboard input past 1-99
document.getElementById("in-bag").getElementsByTagName("input")[0].addEventListener("change", function() {
    if (bag.value > 99) {
        bag.value = 99;
    } else if (bag.value < 1) {
        bag.value = 1;
    }
});

//-------------------- Makes rating input visible and hidden
let rateReveal = document.getElementById("rate-me");
if (rateReveal != null) {
    rateReveal.addEventListener("click", function() {
        let input = document.getElementById("rate-me-input");
        let button = document.getElementById("rate-me-button");
        if (input.classList.contains("invis")) {
            input.classList.remove("invis");
            button.classList.remove("invis");
        } else {
            input.classList.add("invis");
            button.classList.add("invis");
        }
    });
}
