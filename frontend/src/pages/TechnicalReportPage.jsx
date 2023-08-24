import React from 'react'

import {Menu} from '../components/Menu/Menu';
import {TechnicalReport} from '../components/TechnicalReport/TechnicalReport';

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
                <TechnicalReport/>
            </div>
            </body>
        </div>
    )
}
