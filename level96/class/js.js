function generateBoolean(){
    const bool = Math.random() > 0.5;
    return bool
};
const myP = <p>{generateBoolean ? "hello": "goodbye"}</p>
const myDiv = (
    <div>
        {generateBoolean() && <p>hello and goodbye</p>}
    </div>
);