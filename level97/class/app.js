
export default function App() {
    function handleClick() {
        console.log("User clicked on button")
    }
    return(
        <div onClick={handleClick}>
            <p>click me rn</p>
        </div>
    )
}