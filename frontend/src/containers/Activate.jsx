import React from 'react';

const Activate = () => {

    return (
        <div className='container'>
            <div
                className='d-flex flex-column justify-content-center align-items-center'
                style={{marginTop: '200px'}}
            >
                <h1>Verify your Account:</h1>
                <button
                    style={{marginTop: '50px'}}
                    type='button'
                    className='btn btn-primary'
                >
                    Verify
                </button>
            </div>
        </div>
    );
};

export default Activate;