// Finds and updates lesson price
function CalcCost() {
    let totalMonths = parseInt(document.getElementById("month_duration").value);
    let total = 4 * totalMonths;
    let lessonTotal = parseInt(document.getElementById("price").value);
    let totalType = document.getElementById("payment_type").value;
    // let totalType = document.querySelector(".price-button-active").id.split("-")[1]
    // let totalType = this.id.split("-")[1];

    // Variables
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


    if (totalType == "week") {
        // do nothing
    } else if (totalType == "month") {
        totalCost *= 4
    } else if (totalType == "full") {
        totalCost *= 4 * totalMonths
    }

    document.getElementById("price").value = "$" +  totalCost;
}


// function paymentTotalType() {
//     let totalType = document.querySelector(".price-button-active").id.split("-")[1]
//     document.querySelector(".price-button-active").classList.add("price-button-inactive")
//     document.querySelector(".price-button-active").classList.remove("price-button-active")
//     this.classList.add("price-button-active")
//     this.classList.remove("price-button-inactive")
//     CalcCost()
// }



// Intial lesson price update
CalcCost();
// Updates lesson price when lesson minutes are changed
document.getElementById("minutes").addEventListener("change", CalcCost);
document.getElementById("per_week").addEventListener("change", CalcCost);
document.getElementById("month_duration").addEventListener("change", CalcCost);
document.getElementById("payment_type").addEventListener("change", CalcCost);

// document.getElementById("price-week").addEventListener("click", paymentTotalType);
// document.getElementById("price-month").addEventListener("click", paymentTotalType);
// document.getElementById("price-total").addEventListener("click", paymentTotalType);


