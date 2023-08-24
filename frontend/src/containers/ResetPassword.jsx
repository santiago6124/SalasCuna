import React from 'react';

const ResetPassword = () => {

    return (
        <div className='container mt-5'>
            <h1>Request Password Reset:</h1>
            <form>
                <div className='form-group'>
                    <input
                        className='form-control'
                        type='email'
                        placeholder='Email'
                        name='email'
                        required
                    />
                </div>
                <button className='btn btn-primary' type='submit'>Reset Password</button>
            </form>
        </div>
    );
};

export default ResetPassword;