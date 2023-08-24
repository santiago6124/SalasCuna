import "./SelectRoom.css";
import Col from "react-bootstrap/Col/";
import Row from "react-bootstrap/Row/";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/esm/Button";

import React, { useEffect, useState } from "react";

import {UpdateRoom} from "../EditRoom/EditRoom";

export function SelectRoom() {
  const [cribroomOptions, setCribroom] = useState([]);
  const [selectedCribroom, setSelectedCribroom] = useState("");
  const [confirmed, setConfirmed] = useState(false);

  useEffect(() => {
    LoadCribrooms();
  }, []);
  const LoadCribrooms = async () => {
    try {
      let response = await fetch("http://127.0.0.1:8000/api/cribroom/");
      let jsonData = await response.json();
      console.log(jsonData);
      setCribroom(jsonData);
    } catch (error) {
      console.error("Error fetching Cribroom Options", error);
    }
  };

  const handleConfirmClick = () => {
    setConfirmed(true);
  };

  return (
    <body className="body">
      {confirmed ? (
        <UpdateRoom />
      ) : (
        <Form className="conteiner-form-room">
          <h1 className="titulo">Editar Sala Cuna</h1>
          <div className="contenedor-linea">
            <hr className="linea"></hr>
          </div>
          <Row>
            <Col xs={9} className="conteiner-select"></Col>
            <Form.Group className="mb-3">
              <Form.Label className="mb-1 mt-3">
                Seleccionar Sala Cuna Que Desea Editar
              </Form.Label>
              <Form.Select
                as="select"
                value={selectedCribroom}
                className="mb-1"
                onChange={(event) => setSelectedCribroom(event.target.value)}
              >
                <option value="" disabled>
                  Seleccionar Sala Cuna
                </option>
                {cribroomOptions.map((cribroom) => (
                  <option key={cribroom.id} value={cribroom.id}>
                    {cribroom.name}
                  </option>
                ))}
              </Form.Select>
              <div className="contenedor-boton-room">
                <Button
                  className="button-select mt-4"
                  boton
                  variant="primary"
                  onClick={handleConfirmClick}
                >
                  Confirmar
                </Button>
              </div>
            </Form.Group>
          </Row>
        </Form>
      )}
    </body>
  );
}
