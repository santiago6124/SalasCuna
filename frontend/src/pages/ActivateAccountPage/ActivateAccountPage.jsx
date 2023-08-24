import React from "react";
import {Button} from "react-bootstrap";
import {useNavigate, useParams} from "react-router-dom";

import './ActivateAccountPage.css';

const ActivateAccountPage = () => {
    const {uid, token} = useParams()
    let history = useNavigate()

    let uidToken = uid
    let activationToken = token
    const [show, setShow] = React.useState(false);

    let activateAccount = async () => {
        let response = await fetch('/auth/users/activation/', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                "Accept": "application/json"
            },
            body: JSON.stringify({
                "uid": uidToken,
                "token": activationToken
            })
        })
        if (response.status === 204) {
            history('/')
        } else {
            alert('Something went wrong')
        }
    }


    return (
        <div className="divActivate">
            <div className="containerActivate">
                <h1>Verifica tu cuenta</h1>
                <Button className="mt-5" onClick={activateAccount}>Verificar</Button>
            </div>
        </div>

    );
}

export default ActivateAccountPage