import React from 'react'

import {Menu} from '../components/Menu/Menu';
import {DeleteChildren} from '../components/DeleteChildren/DeleteChildren';

export function AddChildrenPage() {
    return (
        <div className="App">
            <header>
                <div>
                    <Menu/>
                </div>
            </header>
            <body className='body'>
            <div>
                <DeleteChildren/>
            </div>
            </body>
        </div>
    )
}
