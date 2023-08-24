import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import React, { useEffect, useState } from 'react'; 
import axios from 'axios';

import { FaQrcode } from 'react-icons/fa';

export function AddTutor() {

    const [genders, setGeneros] = useState([]); 

    const [selectedGenero, setSelectedGenero] = useState('');

    const handleGeneroChange = (event) => {
        setSelectedGenero(event.target.value);
    };

    useEffect(() => {
        ListGenero();
    }, []);

    const ListGenero = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
          setGeneros(response.data.gender);
        } catch (error) {
          console.error('Error fetching generos:', error);
        }
      };

    return (
        <Form className='conteiner-form'>
            <h1 className='titulo'>Añadir Tutor/a</h1>

            <div className='contenedor-linea'>
                <hr className='linea'></hr>
            </div>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Nombre</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un nombre"/>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Apellido</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un apellido"/>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>DNI</Form.Label>
                <Form.Control type="number" placeholder="Ingrese un DNI"/>
            </Form.Group>

            <div className='mb-3'>
                <Form.Label className='mb-1'>Genero</Form.Label>
                <select id="gender" value={selectedGenero} onChange={handleGeneroChange} className='form-control'>
                    <option value="">Generos</option>
                    {genders.map((gender) => (
                        <option key={gender.id} value={gender.id}>
                            {gender.gender}
                        </option>
                    ))}
                </select>
            </div>

            <Form.Group className="mb-4">
                <Form.Label className='mb-1'>Fecha De Nacimiento</Form.Label>
                <Form.Control type="date" placeholder=""/>
            </Form.Group>
            
            <div className="contenedor-boton mb-1">
                <Button as="input" type="submit" value="Cargar" size="lg"/>
            </div>
        </Form>
    );
}