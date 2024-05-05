import pfpic from './assets/react.svg'

function Card(){

return (

    <div className="card">
            <img calssName = "cardimg" src={pfpic} alt ="pfp pic"></img>
            <h2 className="card-title">Kritan</h2>
            <p className = "card-text">I sleep</p>

    </div>


);




}

export default Card