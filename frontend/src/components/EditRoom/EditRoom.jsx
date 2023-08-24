import "../EditRoom/EditRoom.css";

import Modal from "react-bootstrap/Modal";

import Col from "react-bootstrap/Col/";
import Row from "react-bootstrap/Row/";
import Form from "react-bootstrap/Form/";
import { Container } from "react-bootstrap";
import { Button } from "react-bootstrap";

import React, { useState, useEffect } from "react";

import { getAllShifts, getAllZones, getAllCribroomsWithoutDepth } from "../../api/salasCuna.api";

export function UpdateRoom(props) {
  const [zoneOptions, setZoneOptions] = useState([]);
  const [shiftOptions, setShiftOptions] = useState([]);
  const [selectedCribroom, setSelectedCribroom] = useState("");
  const [selectedZone, setSelectedZone] = useState("");
  const [selectedShift, setSelectedShift] = useState("");
  const [cribroom, setCribroom] = useState([]);

  useEffect(() => {
    loadZones();
    loadShifts();
    setSelectedCribroom(props.id);
    loadSelectedCribroom(props.id); // Load selected cribroom data
  }, []);

  const loadZones = async () => {
    try {
      const response = await getAllZones();
      setZoneOptions(response.data);
    } catch (error) {
      console.error("Error fetching zona options:", error);
    }
  };

  const loadShifts = async () => {
    try {
      const response = await getAllShifts();
      setShiftOptions(response.data);
    } catch (error) {
      console.error("Error fetching shift options:", error);
    }
  };

  async function loadSelectedCribroom(cribroomId) {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/cribroom/?no_depth&id=" + cribroomId,
        { method: "GET" }
      );
      if (response.ok) {
        const data = await response.json(); // Extract JSON data
        const crib = data[0];
        setCribroom(crib);
      } else {
        console.error("Error fetching selected cribroom data:", response.statusText);
      }
    } catch (error) {
      console.error("Error fetching selected cribroom data:", error);
    }
  }

  const handleEdit = async (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const payload = {
      name: formData.get("nameCR"),
      code: formData.get("codeCR"),
      max_capacity: formData.get("max_capacityCR"),
      street: formData.get("streetCR") ? formData.get("streetCR"): "", // if null, empty string in order to not broke xd
      house_number: formData.get("house_numberCR"),
      shift: formData.get("shiftCR"),
      zone: formData.get("zoneCR"),
    };
    if (selectedCribroom) {
      try {
        let response = await fetch(
          "http://127.0.0.1:8000/api/cribroom/" + selectedCribroom + "/",
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
          }
        );
        if (response.ok) {
          console.log("Cribroom Updated");
          props.onHide();
        } else {
          console.log("Failed to Update");
        }
      } catch (err) {
        alert(err);
      }
    }
  };

  function handleShiftChange(event) {
    setSelectedShift(event.target.value);
  }

  function handleZoneChange(event) {
    setSelectedZone(event.target.value);
  }



  return (
    <Modal {...props} aria-labelledby="contained-modal-title-vcenter" centered>
      <div className="contenedor-form-wrapper">
        <Container fluid className="conteiner-form-room">
          <Form onSubmit={handleEdit} className="conteiner-form-edit">
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
                defaultValue={cribroom ? cribroom.name : ""}
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label className="mb-1">Codigo De Sala</Form.Label>
              <Form.Control
                type="text"
                placeholder="Editar El Nombre De La Sala"
                name="codeCR"
                defaultValue={cribroom ? cribroom.code : ""}
              />
            </Form.Group>
            <Form.Group className="mb-3">
              <Form.Label className="mb-1">Capacidad Maxima</Form.Label>
              <Form.Control
                type="number"
                placeholder="Editar La Capacidad Maxima De La Sala"
                name="max_capacityCR"
                defaultValue={cribroom ? cribroom.max_capacity : ""}
              />
            </Form.Group>
            <Row className="mb-1">
              <Col xs={9}>
                <Form.Label className="mb-1">Calle</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Editar Calle"
                  name="streetCR"
                  defaultValue={cribroom ? cribroom.street : ""}
                />
              </Col>
              <Col>
                <Form.Label className="mb-1">Nro</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="Nro"
                  name="house_numberCR"
                  defaultValue={cribroom ? cribroom.house_number : ""}
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
                      value={selectedShift ? selectedShift: cribroom.shift}
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
                  value={selectedZone ? selectedZone: cribroom.zone}
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
              <Button
                className="boton-edit mt-3"
                boton
                variant="primary"
                type="submit"
              >
                Editar Sala Cuna
              </Button>
            </div>
          </Form>
        </Container>
      </div>
    </Modal>
  );
}
