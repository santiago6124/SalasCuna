import React, { useEffect, useState } from 'react';
import axios from 'axios';

import Col from 'react-bootstrap/Col/';
import Row from 'react-bootstrap/Row/';
import Form from 'react-bootstrap/Form/';
import {Button} from 'react-bootstrap';

import { useNavigate, useLocation } from 'react-router-dom';

export function FormEditChildren() {

    useEffect(() => {
        getChildren();
    }, []);

    const getChildren = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/all-objects/');
        let data = await response.json();
        console.log(data);
    };


    const [chieldGenders, setChildGender] = useState([]); 
    const [guardianGenders, setGuardianGender] = useState([]);
    const [salas, setCribroom] = useState([]); 
    const [shifts, setShift] = useState([]); 
    const [localities, setLocality] = useState([]); 
    const [neighborhoods, setNeighborhood] = useState([]); 
    const [childStates, setChildState] = useState([]);
    const [guardianTypes, setGuardianType] = useState([]); 
    const [phoneFeatures, setPhoneFeature] = useState([]); 

    const [selectedGeneroChield, setSelectedGeneroChield] = useState('');
    const [selectedGeneroGuardian, setSelectedGeneroGuardian] = useState('');
    const [selectedSalaCuna, setSelectedSalacuna] = useState('');
    const [selectedTurno, setSelectedTurno] = useState('');
    const [selectedLocality, setSelectedLocality] = useState('');
    const [selectedNeighborhood, setSelectedNeighborhood] = useState('');
    const [selectedChildState, setSelectedChildState] = useState('');
    const [selectedPhoneFeature, setSelectedPhoneFeature] = useState('');
    const [selectedGuardianType, setSelectedGuardianType] = useState('');
    

    const handleGeneroChieldChange = (event) => {
        setSelectedGeneroChield(event.target.value);
        
    };
    
    const handleGeneroGuardianChange = (event) => {
        setSelectedGeneroGuardian(event.target.value);
        
    };

    const handleSalaCunaChange = (event) => {
        setSelectedSalacuna(event.target.value);
        
    };
    const handleTurnoChange = (event) => {
        setSelectedTurno (event.target.value);
        
    };
    const handleLocalityChange = (event) => {
        setSelectedLocality(event.target.value);
        
    };
    const handleNeighborhoodChange = (event) => {
        setSelectedNeighborhood(event.target.value);
        
    };
    const handleChildStateChange = (event) => {
        setSelectedChildState(event.target.value);
        
    };
    const handlePhoneFeatureChange = (event) => {
        setSelectedPhoneFeature(event.target.value);
        
    };
    const handleGuardianTypeChange = (event) => {
        setSelectedGuardianType(event.target.value);
        
    };
    

    useEffect(() => {
        getChildren();
        GenderList();
        CribroomList();
        ShiftList();
        LocalityList();
        NeighborhoodList();
        ChildStateList();
        GuardianTypeList();
        PhoneFeatureList();
        
        }, []);


    const GenderList = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/GenderListView/');
          setChildGender(response.data);
          setGuardianGender(response.data);
        } catch (error) {
          console.error('Error fetching generos:', error);
        }
      };


    const CribroomList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/CribroomListView/');
            setCribroom(response.data);
            }   catch (error)  {
                console.log('Error fetching Salas Cunas:', error);
            };
    };

    const ShiftList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ShiftListView/');
            setShift(response.data);
            } catch (error) {
                console.log('Error fetching Turnos:', error);
            };
    };

    const LocalityList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/LocalityListView/');
            setLocality(response.data);
            } catch(error) {
                console.error('Error fetching localidad:', error);
            };
    };

    const NeighborhoodList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/NeighborhoodListView/');
            setNeighborhood(response.data);
            } catch(error) {
                console.error('Error fetching barrio:', error);
            };
    };

    const ChildStateList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/ChildStateListView/');
            setChildState(response.data);
            } catch(error) {
                console.error('Error fetching estados:', error);
            };
    };

    const navigate = useNavigate();
    
    const GuardianTypeList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/GuardianTypeListView/');
            setGuardianType(response.data);
            } catch(error) {
                console.error('Error fetching estados:', error);
            };
    };

    const PhoneFeatureList = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/PhoneFeatureListView/');
            setPhoneFeature(response.data);
            } catch(error) {
                console.error('Error fetching estados:', error);
            };
    };

  const handleNewClick = () => {
   navigate('/children-management');
  };

  const location = useLocation();
    const childId = location?.state?.childId;

  const handleSubmit = async (event) => {
    event.preventDefault()

    const formData = new FormData(event.target);
    const payload = {
        first_name: formData.get("nombreChield"),
        last_name: formData.get("apellidoChield"),
        dni: formData.get("dniChield"),
        birthdate: formData.get("fechaNacimientoChield"),
        house_number: formData.get("numero_casa"),
        registration_date: formData.get("fechaAlta"),
        disenroll_date: formData.get("fechaBaja"),
        locality: formData.get("locality"),
        gender: formData.get("generoChild"),
        cribroom: formData.get("salacuna"),
        shift: formData.get("turno"),
        child_state: formData.get("estado"),
        neightborhood: formData.get("neightborhood"),
        guardian_first_name:formData.get("nombreGuardian"),
        guardian_last_name: formData.get("apellidoGuardian"),
        guardian_dni: formData.get("dniGuardian"),
        guardian_phone_number: formData.get("telefono"),
        guardian_phone_Feature: formData.get("phoneFeature"),
        guardian_guardian_Type_id: formData.get("guardianType"),
        giardian_gender_id: formData.get("generoGuardian"),
        
    };
  
    try {
     console.log(childId + " id");
     let response = await fetch(`http://127.0.0.1:8000/api/child/${childId}/`, {
       method: 'PUT',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify(payload),
    });
    console.log(response + "response");
    if (response.ok) {
      console.log('Child edited successfully');
      window.location.reload();
  } else {
      console.log('Failed to edit child');
  }

     } catch (err) {
      alert(":c")
      console.log(err)
     }

  }




  return (
    <Form className="conteiner-form" onSubmit={handleSubmit}>
        
            <Button
              as="input"
              type="submit" 
              value="Back"
              size="m"
              onClick={handleNewClick}
            />

            <h1 className="titulo">Editar Niños/as</h1>

            <div className="contenedor-linea">
                <hr className="linea"/>
            </div>

            <Form.Group className="mb-3">
                <Form.Label className="mb-1">Nombre</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un nombre" name="nombreChield" />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Apellido</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un apellido"name="apellidoChield" />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>DNI</Form.Label>
                <Form.Control type="number" placeholder="Ingrese un DNI"name="dniChield" />
            </Form.Group>
            
            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Fecha De Nacimiento</Form.Label>
                <Form.Control type="date" placeholder="" name="fechaNacimientoChield" />
            </Form.Group>

            <Row className="mb-3">
                <Col>
                    <div>
                        <Form.Label className='mb-1'>Genero</Form.Label>
                        <select id="gender" name="generoChield" value={selectedGeneroChield} onChange={handleGeneroChieldChange} className='form-control'>
                            <option value="">Generos</option>
                            {chieldGenders.map((gender) => (
                                <option key={gender.id} value={gender.id}>
                                    {gender.gender}
                                </option>
                            ))}
                        </select>
                    </div>
                </Col>
                <Col>
                    <div>
                        <Form.Label className='mb-1'>Estado</Form.Label>
                        <select id="child_state" name="estado" value={selectedChildState} onChange={handleChildStateChange} className='form-control'>
                            <option value="">Estado</option>
                            {childStates.map((child_state) => (
                                <option key={child_state.id} value={child_state.id}>
                                    {child_state.name}
                                </option>
                            ))}
                        </select>
                    </div>
                </Col>
            </Row>
            
            <Row className="mb-3">
                <Col>
                    <div>
                        <Form.Label className='mb-1'>Sala Cuna</Form.Label>
                        <select id="cribroom" name="salacuna" value={selectedSalaCuna} onChange={handleSalaCunaChange} className='form-control'>
                            <option value="">Sala Cuna</option>
                            {salas.map((cribroom) => (
                                <option key={cribroom.id} value={cribroom.id}>
                                    {cribroom.name}
                                </option>
                            ))}
                        </select>
                    </div>
                </Col>
            </Row>       
            
            <div className='mb-3'>
                <Form.Label className='mb-1'>Turno</Form.Label>
                <select id="shift" name="turno" value={selectedTurno} onChange={handleTurnoChange} className='form-control'>
                    <option value="">Turnos</option>
                    {shifts.map((shift) => (
                        <option key={shift.id} value={shift.id}>
                            {shift.name}
                        </option>
                    ))}
                </select>
            </div>

                    
            <Row className="mb-5">
                <Col>
                    <Form.Label className='mb-1'>Fecha de baja</Form.Label>
                    <Form.Control type="date" placeholder="" name="fechaBaja"/>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Fecha de alta</Form.Label>
                    <Form.Control type="date" placeholder="" name="fechaAlta"/>
                </Col>
            </Row>


            <h1 className='titulo'>Añadir Tutor/a</h1>

            <div className='contenedor-linea'>
                <hr className='linea'></hr>
            </div>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Nombre</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un nombre" name="nombreGuardian" />
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>Apellido</Form.Label>
                <Form.Control type="text" placeholder="Ingrese un apellido" name="apellidoGuardian"/>
            </Form.Group>

            <Form.Group className="mb-3">
                <Form.Label className='mb-1'>DNI</Form.Label>
                <Form.Control type="number" placeholder="Ingrese un DNI" name='dniGuardian' />
            </Form.Group>

            <div className='mb-3'>
                <Form.Label className='mb-1'>Genero</Form.Label>
                <select id="gender" name='generoGuardian' value={selectedGeneroGuardian} onChange={handleGeneroGuardianChange} className='form-control'>
                    <option value="">Generos</option>
                    {guardianGenders.map((gender) => (
                        <option key={gender.id} value={gender.id}>
                            {gender.gender}
                        </option>
                    ))}
                </select>
            </div>

            <Row className="mb-4">
                <Col>
                    <Form.Label className='mb-1'>Caracterisitca Telefonica</Form.Label>

                    <select id="phoneFeature" name='phoneFeature' value={selectedPhoneFeature} onChange={handlePhoneFeatureChange} className='form-control'>
                    <option value="">Phone Features</option>
                    {phoneFeatures.map((phoneFeature) => (
                        <option key={phoneFeature.id} value={phoneFeature.id}>
                            {phoneFeature.feature}
                        </option>
                    ))}
                </select>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Telefono</Form.Label>
                    <Form.Control type="number" placeholder="Ingrese un telefono" name='telefono' />
                </Col>
            </Row>

            <Row className="mb-4">
                <Col>
                    <Form.Label className='mb-1'>Madre/padre o Tutor?</Form.Label>

                    <select id="guardianType" name='guardianType' value={selectedGuardianType} onChange={handleGuardianTypeChange} className='form-control'>
                    <option value="">Madre/padre o Tutor?</option>
                    {guardianTypes.map((guardianType) => (
                        <option key={guardianType.id} value={guardianType.id}>
                            {guardianType.type}
                        </option>
                    ))}
                </select>
                </Col>
            </Row>

            <h1 className='titulo'>Añadir Domicilio</h1>

            <div className='contenedor-linea'>
                <hr className='linea'></hr>
            </div>
            <Row className="mb-3">
                <Col>
                    <Form.Label className='mb-1'>Calle</Form.Label>
                    <Form.Control type="text" placeholder="Ingrese una calle" name="calle"/>
                </Col>
                <Col>
                    <Form.Label className='mb-1'>Numero</Form.Label>
                    <Form.Control type="number" placeholder="Ingrese un numero" name="numero_casa"/>
                </Col>
            </Row>

            <div className='mb-3'>
                <Form.Label className='mb-1'>Barrio</Form.Label>
                <select id="neighborhood" name="neighborhood" value={selectedNeighborhood} onChange={handleNeighborhoodChange} className='form-control'>
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
                <select id="locality" name="locality" value={selectedLocality} onChange={handleLocalityChange} className='form-control'>
                    <option value="">Localidad</option>
                    {localities.map((locality) => (
                        <option key={locality.id} value={locality.id}>
                            {locality.locality}
                        </option>
                    ))}
                </select>
            </div>


 
            <div className="contenedor-boton mb-1 ">
                <Button as="input" type="submit" value="Cargar" size="lg"/>
            </div>
        </Form>

        
  );
}