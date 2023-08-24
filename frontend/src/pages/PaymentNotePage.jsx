import React from 'react'

import {Menu} from '../components/Menu/Menu';
import {PaymentNote} from '../components/PaymentNote/PaymentNote';

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
                <PaymentNote/>
            </div>
            </body>
        </div>
    )
}
