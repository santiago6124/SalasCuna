import React from 'react';
import './PaymentNote.css';

import Col from 'react-bootstrap/Col/';
import Row from 'react-bootstrap/Row/';
import Form from 'react-bootstrap/Form/';
import Button from 'react-bootstrap/Button/';
import Table from 'react-bootstrap/Table/';
import InputGroup from 'react-bootstrap/InputGroup/';

export function PaymentNote() {
    return (
        <div className='container-note mt-5'>
            <div className='container-titulo-note '>
                <h1>Nota de Pago</h1>
            </div>
            <div className='contenedor-linea-note'>
                <hr className='linea-note'></hr>
            </div>
            <Row className="mb-3">
                <Col>
                    <div className='input-select'>
                        <Form.Select placeholder="Seleccionar Sala Cuna" className="mb-1">
                            <option></option>
                            <option value="Capital">Capital</option>
                            <option value="Interior">Interior</option>
                        </Form.Select>
                    </div>
                </Col>
                <Col>
                    <div className='container-botones-payment'>
                        <div className='btn-1'>
                            <Button>PDF</Button>
                        </div>
                        <div className='btn-2'>
                            <Button>Excel</Button>
                        </div>
                    </div>
                </Col>
            </Row>

            <div>
                <Table striped bordered hover>
                    <thead>
                    <tr>
                        <th>Codigo</th>
                        <th>Nombre Sala</th>
                        <th>CUIT</th>
                        <th>Entidad</th>
                        <th>Cantidad de Niños</th>
                        <th>Seleccionar <InputGroup.Checkbox className="btn-selectall"
                                                             aria-label="Checkbox for following text input"/></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>01</td>
                        <td>teclitas</td>
                        <td>2243</td>
                        <td>RRHH</td>
                        <td>5</td>
                        <td><InputGroup.Checkbox/></td>
                    </tr>
                    </tbody>
                </Table>
            </div>

        </div>
    )
}

