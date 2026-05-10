const number = 10;

const element = (
  <div>
    <h1>{number + 5}</h1> {}

    <img 
      src="https://via.placeholder.com/150" 
      alt="example image"
    /> {}

    <p className={number > 5 ? "big-number" : "small-number"}>
      Number is {number}
    </p> {}
  </div>
);