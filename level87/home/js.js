
const items = {
  apple: 2,
  banana: 1,
  orange: 3
}


const priceList = Object.entries(items).map(
  ([item, price]) => `${item}: $${price}`
)

console.log(priceList)


const obj = {
  name: "John",
  age: 20,
  city: "Tbilisi"
}

const properties = ["name", "age", "country", "city"]


let validCount = 0

for (let prop of properties) {
  if (Object.hasOwn(obj, prop)) {
    validCount++
  }
}

console.log(validCount)
