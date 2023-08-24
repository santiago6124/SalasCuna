import React from 'react'

import Menu from '../../components/Menu/Menu';
import {CreateRoom} from '../../components/CreateRoom/CreateRoom';

export default function CreateRoomPage() {
    return (
        <div className="App">
            <header>
                <div>
                    <Menu/>
                </div>
            </header>
            <body className='body'>
            <div>
                <CreateRoom/>
            </div>
            </body>
        </div>
    )
}
