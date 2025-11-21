function calculateAge() {
//parseint makes str to num
// if you didnt wrote anyyhing in the box the function will return (print) 0 
  const yearsToAdd = parseInt(document.getElementById("year").value) || 0
  const monthsToAdd = parseInt(document.getElementById("month").value) || 0
  const daysToAdd = parseInt(document.getElementById("day").value) || 0
//needed help but this code make a resultdate variable and gets todays date
  const today = new Date()
  const resultDate = new Date(today)
//needed help also but this code calculates the the ammount of days or months or year you wrote down  and add to the currrent date
  resultDate.setFullYear(resultDate.getFullYear() + yearsToAdd)
  resultDate.setMonth(resultDate.getMonth() + monthsToAdd)
  resultDate.setDate(resultDate.getDate() + daysToAdd)

//calculating the ammount
//getMonth() gives month index 0 = January,  11 = December so we need to add +1
  const y = resultDate.getFullYear()
  const m = resultDate.getMonth() + 1
  const d = resultDate.getDate()
//geting elements from html and giving them text contet so it  can  show the calculation
  document.getElementById("years").textContent = y
  document.getElementById("months").textContent = m
  document.getElementById("days").textContent = d
}
