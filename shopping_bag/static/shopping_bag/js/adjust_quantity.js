//-------------------- Form and form control for quantity
// Adds one to bag total, to a max of 99
let findAddButtons = document.querySelectorAll(".add-button");
findAddButtons.forEach(AddButtonFunction);
function AddButtonFunction(addButton, addButtonIndex) {
    let bag = document.getElementsByClassName("in-bag")[addButtonIndex].getElementsByTagName("input")[0];
    let invisBag = document.getElementsByClassName("invisBag")[addButtonIndex];
    addButton.addEventListener('click', function () {
        let bagContent = parseInt(bag.value);
        if (bagContent < 99 ) {
            bagContent = bagContent + 1;
            bag.value = bagContent;
            invisBag.value = bagContent;
        }
    })
}

// Removes one from bag total, to a min of 1
let findSubButtons = document.querySelectorAll(".sub-button");
findSubButtons.forEach(subButtonFunction);
function subButtonFunction(subButton, subButtonIndex) {
    let bag = document.getElementsByClassName("in-bag")[subButtonIndex].getElementsByTagName("input")[0];
    let invisBag = document.getElementsByClassName("invisBag")[subButtonIndex];
    subButton.addEventListener('click', function () {
        let bagContent = parseInt(bag.value);
        if (bagContent > 0 ) {
            bagContent = bagContent - 1;
            bag.value = bagContent;
            invisBag.value = bagContent;
        }
    })
}

// Doesn't allow users to change numbers with direct keyboard input past 1-99
let findInputs = document.querySelectorAll(".in-bag > input")
findInputs.forEach(addFloorCeiling);
function addFloorCeiling(input) {
    input.addEventListener("change", function() {
        if (input.value > 99) {
            input.value = 99;
        } else if (input.value < 0) {
            input.value = 0;
        }
    });
}
