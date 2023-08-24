import Menu from "../Menu/Menu";
import SearchBar from "../SearchBar/SearchBar";
import UpdateRoomModaled from "../EditRoom/EditRoom";
import {UpdateRoom} from "../EditRoom/EditRoom";
import DeleteRoom from "../DeleteRoom/DeleteRoom";
import "./CribroomDashboard.css";

import React, { useEffect, useState } from "react";

import {
  getAllCribroomsWithoutDepth,
  getAllLocalities,
} from "../../api/salasCuna.api";

//DataGrid Import
import { DataGrid, GridActionsCellItem } from "@mui/x-data-grid";

//UI Icons Imports
import DeleteIcon from "@mui/icons-material/Delete";
import SaveAltIcon from "@mui/icons-material/SaveAlt";
import EditIcon from "@mui/icons-material/Edit";

export default function CribroomDashboard() {
  const [cribrooms, setCribrooms] = useState([]);
  const [filteredCribroom, setFilteredCribroom] = useState([]);
  const [keyword, setKeyword] = useState("");
  const [zoneOptions, setZoneOptions] = useState([]);
  const [shiftOptions, setShiftOptions] = useState([]);
  const [locality, setLocalities] = useState([]);
  const [selectedCribroom, setSelectedCribroom] = useState("");
  const [cribroomName, setCribroomName] = useState("");

  const [modalShow, setModalShow] = useState(false);
  const [confirmed, setConfirmed] = useState(false);
  const [modalEditShow, setModalEditShow] = useState(false);
  const [modalDeleteShow, setModalDeleteShow] = useState(false);
  const [confirmedEdit, setEditConfirmed] = useState(false);
  const [confirmedDelete, setDeleteConfirmed] = useState(false);

  useEffect(() => {
    listCribroom();
  }, []);

  const listCribroom = async () => {
    try {
      const responseLocality = await getAllLocalities();
      setLocalities(responseLocality.data);
      const response = await getAllCribroomsWithoutDepth();
      const localityData = responseLocality.data;
      const cribroomData = response.data;
      const updatedCribrooms = await cribroomData.map(cribroom => {
        const matchingLocality = localityData.find(locality => locality.id === cribroom.locality);
        if (matchingLocality) {
          return {
            ...cribroom,
            locality: matchingLocality.locality,
            is_active: cribroom.is_active ? "Activo" : "Inactivo"
            };
        }
        else {
          return {
            ...cribroom,
            is_active: cribroom.is_active ? "Activo" : "Inactivo"
            };
        }
      });
      setCribrooms(updatedCribrooms);
      setFilteredCribroom(updatedCribrooms);  
    } catch (error) {
      console.log("Error fetching SalasCunas:", error);
    }
  };

  const handleEditClick = (rowId) => {
    setSelectedCribroom(rowId);
    setModalEditShow(true)
    console.log("Edit clicked for row with id:", rowId);
  };

  const handleDeleteClick = (rowId, CRName) => {
    setSelectedCribroom(rowId);
    setCribroomName(CRName);
    setModalDeleteShow(true);
    console.log("Edit clicked for row with id:", rowId);
  };

  // SEARCH FUNCTION

  const updateKeyword = (keyword) => {
    const filtered = cribrooms.filter((cribroom) => {
      return `${cribroom.name.toLowerCase()}`.includes(keyword.toLowerCase());
    });
    setKeyword(keyword)
    setFilteredCribroom(filtered);
    console.log(filteredCribroom);
  };
  const handleCribroomChange = async (event) => {
    setSelectedCribroom(event.target.value);
  };

  const handleConfirmClick = async (event) => {
    setEditConfirmed(true);
  };

  const hanldeEditConfirmClick = async (event) => {
    setDeleteConfirmed(true);
  };
  return (
    <>
      <body>
        <div className="cribroom-dashboard">
          <header className="header">
            <Menu />
          </header>
          {selectedCribroom && (
            <>
              <UpdateRoom
                id={selectedCribroom}
                show={modalEditShow}
                onHide={() => {
                  setModalEditShow(false);
                  setSelectedCribroom(""); // Reset selectedCribroom after closing modal
                  window.location.reload();
                }}
              />
          </>
        )}
        {selectedCribroom && (
              <DeleteRoom
                id={selectedCribroom}
                name={cribroomName}
                show={modalDeleteShow}
                onHide={() => {
                  setModalDeleteShow(false);
                  setSelectedCribroom(""); // Reset selectedCribroom after closing modal
                  window.location.reload();
                }}
              />
            )}
          {!selectedCribroom && (
            <>
              <>
                <h1 className="titulo-cb">Gestion De Salas Cuna</h1>
                <div className="contenedor-linea-cb">
                  <hr className="linea-cb"></hr>
                </div>
                <div>
                  <SearchBar
                    keyword={keyword}
                    onChange={updateKeyword}
                    placeholder={"Buscar Sala Cuna"}
                  />
                </div>
                <div className="DataGrid-Wrapper">
                  <DataGrid
                    style={{ borderRadius: "15px", margin: "20px" }}
                    rows={filteredCribroom}
                    columns={[
                      {
                        field: "id",
                        headerName: "Codigo Sala Cuna",
                        width: 150,
                      },
                      { field: "name", headerName: "Nombre", width: 200 },
                      { field: "street", headerName: "Direccion", width: 150 },
                      {
                        field: "house_number",
                        headerName: "Numero",
                        width: 150,
                      },
                      {
                        field: "max_capacity",
                        headerName: "Cap. Maxima",
                        width: 150,
                      },
                      {
                        field: "locality",
                        headerName: "Localidad",
                        width: 150,
                      },
                      { field: "is_active", headerName: "Estado", width: 150 },
                      { field: "entity", headerName: "Entidad", width: 150 },
                      {
                        field: "actions",
                        type: "actions",
                        headerName: "Acciones",
                        width: 80,
                        getActions: (params) => [
                          <GridActionsCellItem
                            icon={<DeleteIcon />}
                            label="Delete"
                            onClick={() => handleDeleteClick(params.row.id, params.row.name)}
                          />,
                          <>
                            <GridActionsCellItem
                              variant="primary"
                              icon={<EditIcon />}
                              onClick={() => handleEditClick(params.row.id)}
                            />
                          </>,
                        ],
                      },
                    ]}
                    autoHeight
                    autoWidth
                    pageSize={5}
                  />
                </div>
              </>
            </>
          )}
        </div>
      </body>
    </>
  );
}

