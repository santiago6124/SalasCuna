import "./App.css";


import {Menu} from "./components/menu";
import {DeleteRoom} from "./components/eliminarSala";

function App() {
    return (
        <div className="App">
            <header>
                <div>
                    <Menu/>
                </div>
            </header>
            <body className="body">
            <div></div>
            <div>
                <DeleteRoom/>
            </div>
            </body>
        </div>
    );
}

export default App;
