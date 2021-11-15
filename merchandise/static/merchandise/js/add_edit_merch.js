// Find new file name and display
document.getElementById("id_image").addEventListener("change", function () {
    let file = document.getElementById("id_image")
    let fileName = file.value.split("\\")
    fileName = fileName[fileName.length-1]
    document.getElementById("filename").textContent = "Image will be updated to: " + fileName
})