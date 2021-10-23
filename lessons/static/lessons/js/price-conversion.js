// Finds and updates lesson price
function CalcCost() {
    var minutes = parseInt(document.getElementById("minutes").value);
    var hourCost = parseInt(document.getElementById("js_price").value);
    MinutePercent = (minutes / 60);
    totalCost = MinutePercent * hourCost;
    document.getElementById("price").value = totalCost;
}
// Intial lesson price update
CalcCost();
// Updates lesson price when lesson minutes are changed
document.getElementById("minutes").addEventListener("change", CalcCost);