import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

import React, {useEffect, useState} from 'react';
import axios from 'axios';

export function AddResidence() {

    const [localities, setLocalities] = useState([]); 
    const [neighborhoods, setNeighborhoods] = useState([]); 

    const [selectedLocality, setSelectedLocality] = useState('');
    const [selectedNeighborhood, setSelectedNeighborhood] = useState('');

    const handleLocalityChange = (event) => {
        setSelectedLocality(event.target.value);
    };
    const handleNeighborhoodChange = (event) => {
        setSelectedNeighborhood(event.target.value);
    };


    useEffect(() => {
        ListLocality();
        ListNeighborhood();
    }, []);

    const ListLocality = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
            setLocalities(response.data.locality);
            } catch(error) {
                console.error('Error fetching localidad:', error);
            };
    };

    const ListNeighborhood = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
            setNeighborhoods(response.data.neighborhood);
            } catch(error) {
                console.error('Error fetching barrio:', error);
            };
    };

    return (
        <Form className='conteiner-form'>
            <h1 className='titulo'>Añadir Domicilio</h1>

            <div className='contenedor-linea'>
                <hr className='linea'></hr>
            </div>
            <Row className="mb-3">
                <Col>
                    <Form.Label className='mb-1'>Calle</Form.Label>
                    <Form.Control type="text" placeholder="Ingrese una calle"/>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Numero</Form.Label>
                    <Form.Control type="number" placeholder="Ingrese un numero"/>
                </Col>
            </Row>

            <div className='mb-3'>
                <Form.Label className='mb-1'>Barrio</Form.Label>
                <select id="neighborhood" value={selectedNeighborhood} onChange={handleNeighborhoodChange} className='form-control'>
                    <option value="">Localidad</option>
                    {neighborhoods.map((neighborhood) => (
                        <option key={neighborhood.id} value={neighborhood.id}>
                            {neighborhood.neighborhood}
                        </option>
                    ))}
                </select>
            </div>

            <div className='mb-3'>
                <Form.Label className='mb-1'>Localidad</Form.Label>
                <select id="locality" value={selectedLocality} onChange={handleLocalityChange} className='form-control'>
                    <option value="">Localidad</option>
                    {localities.map((locality) => (
                        <option key={locality.id} value={locality.id}>
                            {locality.locality}
                        </option>
                    ))}
                </select>
            </div>


            <Row className="mb-4">
                <Col>
                    <Form.Label className='mb-1'>Departamento</Form.Label>
                    <Form.Control type="text" placeholder="Ingrese una calle"/>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Telefono</Form.Label>
                    <Form.Control type="number" placeholder="Ingrese un telefono"/>
                </Col>
            </Row>

            <div className="contenedor-boton mb-1">
                <Button as="input" type="submit" value="Cargar" size="lg"/>
            </div>

        </Form>
    );
}
  