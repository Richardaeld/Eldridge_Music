//Update selected option as options are slected
var allSelects = document.querySelectorAll("select");
allSelects.forEach(selectsUpdate);
function selectsUpdate(item) {
    item.addEventListener("change", function() {
        // Finds all options
        let totalValues = item.options;
        // Removes selected attribute
        for(let i=0; i<totalValues.length; i++){
            if(item.options[i].hasAttribute("selected")){
                item.options[i].removeAttribute("selected");
            }
        }
        // Adds selected attribute to new selection
        for(let i=0; i<totalValues.length; i++){
            if(item.options[i].selected){
                item.options[i].setAttribute("selected", "");
            }
        }
    });
}