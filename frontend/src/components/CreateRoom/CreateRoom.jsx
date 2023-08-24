import "./CreateRoom.css";

import Col from "react-bootstrap/Col/";
import Row from "react-bootstrap/Row/";
import Form from "react-bootstrap/Form/";
import { Container } from "react-bootstrap";
import { Button } from "react-bootstrap";

import React, { useState, useEffect } from "react";


export function CreateRoom() {
  const [zoneOptions, setZoneOptions] = useState([]);
  const [shiftOptions, setShiftOptions] = useState([]);
  const [selectedZona, setSelectedZone] = useState("");
  const [selectedShift, setSelectedShift] = useState("");
  useEffect(() => {
    loadZones();
    loadShifts();
  }, []);

  const loadZones = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/zone/");
      let jsonData = await response.json();
      setZoneOptions(jsonData);
    } catch (error) {
      console.error("Error fetching zona options:", error);
    }
  };

  const loadShifts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/ShiftListView/");
      let jsonData = await response.json();
      setShiftOptions(jsonData);
    } catch (error) {
      console.error("Error fetching shift options:", error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault()

    const formData = new FormData(event.target);
    const payload = {
        name: formData.get("nameCR"),
        code: formData.get("codeCR"),
        max_capacity: formData.get("max_capacityCR"),
        street: formData.get("streetCR"),
        house_number: formData.get("house_numberCR"),
        shift: formData.get("shiftCR"),
        zone: formData.get("zoneCR"),
    };
  
    try {
     let response = await fetch('http://127.0.0.1:8000/api/cribroom/', {
       method: 'POST',
       headers: {
           'Content-Type': 'application/json'
       },
       body: JSON.stringify(payload),
    });

    if (response.ok) {
      console.log('Child added successfully');
      window.location.reload();
  } else {
      console.log('Failed to add child');
  }

     } catch (err) {
      alert(":c")
      console.log(err)
     }

  }


  const handleShiftChange = (event) => {
    setSelectedShift(event.target.value);
    
};

const handleZoneChange = (event) => {
  setSelectedZone(event.target.value);
  
};

  return (
    <div className="body">
      <div className="contenedor-form-wrapper">
        <Container fluid className="conteiner-form-room">
          <Form onSubmit={handleSubmit} className="conteiner-form-edit">
            <h1 className="titulo">Agregar Sala Cuna</h1>
            <div className="contenedor-linea">
              <hr className="linea"></hr>
            </div>

            <Form.Group className="mb-3">
              <Form.Label className="mb-1">Nombre De Sala</Form.Label>
              <Form.Control
                type="text"
                placeholder="Editar El Nombre De La Sala"
                name="nameCR"
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label className="mb-1">Codigo De Sala</Form.Label>
              <Form.Control
                type="text"
                placeholder="Editar El Nombre De La Sala"
                name="codeCR"
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label className="mb-1">Capacidad Maxima</Form.Label>
              <Form.Control
                type="number"
                placeholder="Editar La Capacidad Maxima De La Sala"
                name="max_capacityCR"
              />
            </Form.Group>
            <Row className="mb-1">
              <Col xs={9}>
                <Form.Label className="mb-1">Calle</Form.Label>
                <Form.Control type="text" placeholder="Editar Calle" name="streetCR"/>
              </Col>
              <Col >
                <Form.Label className="mb-1">Nro</Form.Label>
                <Form.Control type="number" 
                placeholder="Nro"
                name="house_numberCR"
                 />
              </Col>
            </Row>

            <Row className="mb-3">
              <Col>
                <Form.Group>
                  <Form.Label className="mb-1">Turno</Form.Label>
                  <Form.Group className="mb-3">
                    <Form.Select
                      name="shiftCR"
                      as="select"
                      value={selectedShift}
                      className="mb-1"
                      onChange={handleShiftChange}
                    >
                      <option value="" disabled>
                        Seleccionar Turno
                      </option>
                      {shiftOptions.map((shift) => (
                        <option key={shift.id} value={shift.id}>
                          {shift.name}
                        </option>
                      ))}
                    </Form.Select>
                  </Form.Group>
                </Form.Group>
              </Col>
              <Col>
                <Form.Label className="mb-1">Zona</Form.Label>
                <Form.Select
                  name="zoneCR"
                  as="select"
                  value={selectedZona}
                  onChange={handleZoneChange}
                >
                  <option value="" disabled>
                    Seleccionar Zona
                  </option>
                  {zoneOptions.map((zone) => (
                    <option key={zone.id} value={zone.id}>
                      {zone.name}
                    </option>
                  ))}
                </Form.Select>
              </Col>
            </Row>
            <div className="contenedor-boton-qr ">
              <Button className="boton-edit mt-3" boton variant="primary" type="submit">
                Crear Sala Cuna
              </Button>
            </div>
          </Form>
        </Container>
      </div>
    </div>
  );
}
