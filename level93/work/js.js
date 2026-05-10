async function successFunction() {
  try {
    let value = "Task completed successfully!";
    console.log(value);
    return value;
  } catch (error) {
    console.log("Something went wrong");
  }
}

successFunction();

async function errorFunction() {
  try {
    throw new Error("This is the default error");
  } catch (error) {
    console.log("Custom Error: Something broke, but we handled it!");
  }
}

errorFunction();


async function checkNumber(number) {
  try {
    if (number < 10) {
      throw new Error("Number must be 10 or greater");
    }
    console.log("Valid number:", number);
  } catch (error) {
    console.log("Handled Error:", error.message);
  }
}

checkNumber(5);
checkNumber(15);
