import "./DeleteRoom.css";

import Button from "react-bootstrap/esm/Button";
import Modal from "react-bootstrap/Modal";
import Alert from "@mui/material/Alert";

import React, { useState, useEffect } from "react";

export default function DeleteRoom(props) {
  const [selectedCribroom, setSelectedCribroom] = useState("");

  useEffect(() => {
    setSelectedCribroom(props.id);
  }, []);

  const handleDelete = async (event) => {
    event.preventDefault();
    console.log(selectedCribroom);
    try {
      const payload = {
        is_active: "False",
      };

      console.log("making fetch");
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
      props.onHide();
    } catch (err) {
      alert("Error al eliminar la sala cuna");
    }
  };


  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <div>
        <Modal.Title className="titulo-eliminar">
          Eliminar Sala Cuna
        </Modal.Title>
      </div>
      <div className="contenedor-linea-eliminar">
        <hr className="linea-eliminar"></hr>
      </div>
      <div className="par">
        <p>Esta seguro que desea Eliminar la Sala Cuna {selectedCribroom}?</p>
        <p>Esto hara que su estado pase a ser Inactivo,</p>
      </div>
      <div className="par">
        <Alert severity="warning">
          <p>Los chicos que esten en esta sala cuna tambien</p>
          <p>
            pasaran a estar en <strong>estado Inactivo</strong>
          </p>
        </Alert>
      </div>
      <Modal.Footer>
        <div className="button-wrapper">
          <div>
            <Button
              className="mt-3"
              boton
              variant="danger"
              onClick={(handleDelete)}
            >
              Deshabilitar
            </Button>
          </div>
          <Button
            className="mt-3"
            boton
            variant="primary"
            onClick={props.onHide}
          >
            Cancelar
          </Button>
        </div>
      </Modal.Footer>
    </Modal>
  );
}
