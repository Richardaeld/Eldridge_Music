// Finds and updates lesson price
function CalcCost() {
    // Variables
    let totalMonths = parseInt(document.getElementById("month_duration").value);
    let totalType = document.getElementById("payment_type").value;
    let minutes = document.getElementById("minutes").value;
    let hourCost = parseInt(document.getElementById("js_price").value);
    let weeklyLessons = parseInt(document.getElementById("per_week").value);
    // Find lesson time (minutes), hourly cost, and lessons per week
    // Find lesson cost based on hourly cost and lesson time and then multiply
    // lessons per week for a total weekly cost
    minutes = parseInt(minutes.split(" ")[0]);
    MinutePercent = (minutes / 60) * weeklyLessons;
    totalCost = MinutePercent * hourCost;
    console.log(totalCost)
    console.log(totalMonths)
    // Calculate payment total per selected type
    if (totalType == "weekly") {
        // do nothing
    } else if (totalType == "monthly") {
        totalCost *= 4
    } else if (totalType == "one time") {
        totalCost *= 4 * totalMonths
    }
    // Display final total cost
    document.getElementById("price").value = "$" +  totalCost;
}

// Intial lesson price update
CalcCost();
// Updates lesson price when lesson minutes, per week,
// month duration, or payment type are changed
document.getElementById("minutes").addEventListener("change", CalcCost);
document.getElementById("per_week").addEventListener("change", CalcCost);
document.getElementById("month_duration").addEventListener("change", CalcCost);
document.getElementById("payment_type").addEventListener("change", CalcCost);
