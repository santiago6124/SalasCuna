import './AddChildren.css';

import Col from 'react-bootstrap/Col/';
import Row from 'react-bootstrap/Row/';
import Form from 'react-bootstrap/Form/';
import {Button} from 'react-bootstrap';
import React, {useEffect, useState} from 'react';
import axios from 'axios';

export function AddChildren() {
    useEffect(() => {
        getChildren();
    }, []);

    const getChildren = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/all-objects/');
        let data = await response.json();
        console.log(data);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData(event.target);
        const payload = {
            id: "4545455",
            first_name: formData.get("nombre"),
            last_name: formData.get("apellido"),
            dni: formData.get("dni"),
            birthdate: formData.get("fechaNacimiento"),
            registration_date: formData.get("fechaAlta"),
            gender: formData.get("genero"),
            cribroom: formData.get("salacuna"),
            shift: formData.get("turno"),
            user: formData.get("usuario"),
            guardian: formData.get("tutor"),
            child_state: formData.get("estado"),
        };

        try {
            const response = await fetch('http://127.0.0.1:8000/api/child/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(payload),
            });

            if (response.ok) {
                console.log('Child added successfully');
                // Perform any additional actions if needed
            } else {
                console.log('Failed to add child');
                // Handle the error if needed
            }
        } catch (error) {
            console.error('An error occurred while adding child:', error);
        }
    };

    const [tutores, setTutores] = useState([]); 
    const [genders, setGeneros] = useState([]); 
    const [salas, setSalas] = useState([]); 
    const [shifts, setTurno] = useState([]); 

    const [selectedGenero, setSelectedGenero] = useState('');
    const [selectedTutor, setSelectedTutor] = useState('');
    const [selectedSalaCuna, setSelectedSalacuna] = useState('');
    const [selectedTurno, setSelectedTurno] = useState('');

    const handleGeneroChange = (event) => {
        setSelectedGenero(event.target.value);
    };
    const handleTutorChange = (event) => {
        setSelectedTutor(event.target.value);
    };
    const handleSalaCunaChange = (event) => {
        setSelectedSalacuna(event.target.value);
    };
    const handleTurnoChange = (event) => {
        setSelectedTurno (event.target.value);
    };

    useEffect(() => {
        getChildren();
        ListTutors();
        ListGenero();
        ListSalasCuna();
        ListShift();
    }, []);

    const ListTutors = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
            setTutores(response.data.guardian);
            } catch(error) {
                console.error('Error fetching tutores:', error);
            };
    };

    const ListGenero = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
          setGeneros(response.data.gender);
        } catch (error) {
          console.error('Error fetching generos:', error);
        }
      };

    const ListSalasCuna = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
            setSalas(response.data.cribroom);
            }   catch (error)  {
                console.log('Error fetching Salas Cunas:', error);
            };
    };

    const ListShift = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildRelatedObjectsView/');
            setTurno(response.data.shift);
            } catch (error) {
                console.log('Error fetching Turnos:', error);
            };
    };

    return (
        <Form className="conteiner-form" onSubmit={handleSubmit}>
            
            <h1 className="titulo">Añadir Niños/as</h1>

            <div className="contenedor-linea">
                <hr className="linea"/>
            </div>

            <Form.Group className="mb-3">
                <Form.Label className="mb-1">Nombre</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un nombre" name="nombre"/>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Apellido</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un apellido"name="apellido"/>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>DNI</Form.Label>
                <Form.Control type="number" placeholder="Ingrese un DNI"name="dni"/>
            </Form.Group>
            
            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Fecha De Nacimiento</Form.Label>
                <Form.Control type="date" placeholder="" name="fechaNacimiento"/>
            </Form.Group>

            <Row className="mb-3">
                <Col>
                    <div>
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
                </Col>
                <Col>
                    <Form.Group className="mb-3">
                        <Form.Label className='mb-1'>Domicilio</Form.Label>
                        <Form.Control type="text" placeholder="Ingrese un domicilio" name= "domicilio"/>
                    </Form.Group>    
                </Col>
            </Row>
            
            <Row className="mb-3">
                <Col>
                    <div>
                        <Form.Label className='mb-1'>Sala Cuna</Form.Label>
                        <select id="cribroom" value={selectedSalaCuna} onChange={handleSalaCunaChange} className='form-control'>
                            <option value="">Sala Cuna</option>
                            {salas.map((cribroom) => (
                                <option key={cribroom.id} value={cribroom.id}>
                                    {cribroom.cribroom}
                                </option>
                            ))}
                        </select>
                    </div>
                </Col>
                <Col>
                    <div>
                        <Form.Label className='mb-1'>Tutor</Form.Label>
                        <select id="guardian" value={selectedTutor} onChange={handleTutorChange} className='form-control'>
                            <option value="">Tutores</option>
                            {tutores.map((guardian) => (
                                <option key={guardian.id} value={guardian.id}>
                                    {guardian.guardian}
                                </option>
                            ))}
                        </select>
                    </div>
                </Col>
            </Row>       
            
            <div className='mb-3'>
                <Form.Label className='mb-1'>Turno</Form.Label>
                <select id="shift" value={selectedTurno} onChange={handleTurnoChange} className='form-control'>
                    <option value="">Turnos</option>
                    {shifts.map((shift) => (
                        <option key={shift.id} value={shift.id}>
                            {shift.shift}
                        </option>
                    ))}
                </select>
            </div>

                    
            <Row className="mb-4">
                <Col>
                    <Form.Label className='mb-1'>Fecha de baja</Form.Label>
                    <Form.Control type="date" placeholder="" name="fechaBaja"/>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Fecha de alta</Form.Label>
                    <Form.Control type="date" placeholder="" name="fechaAlta"/>
                </Col>
            </Row>
 
            <div className="contenedor-boton mb-1 ">
                <Button as="input" type="submit" value="Cargar" size="lg"/>
            </div>
        </Form>
    );
}