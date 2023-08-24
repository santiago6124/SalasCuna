import React from 'react'
import './DeleteUser.css';

import {Button, Form} from 'react-bootstrap';


export function DeleteUser() {
    return (
        <Form className='conteiner-form-delete'>
            <h1 className='titulo-delete'>Dar Baja Usuario</h1>

            <div className='contenedor-linea-delete'>
                <hr className='linea-delete'></hr>
            </div>
            <Form.Group className="mb-3 mt-5">
                <Form.Label className='mb-1'><b>Nombre</b></Form.Label>
                <Form.Control type="text" placeholder="Ingrese un nombre"/>
            </Form.Group>

            <div className='contenedor-boton-eliminar'>
                <Button className='boton-eliminar mt-5' boton variant="primary">
                    Eliminar
                </Button>
            </div>

        </Form>
    );
}
