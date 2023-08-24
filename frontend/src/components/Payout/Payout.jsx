import React, { useEffect, useState } from "react";


import Col from "react-bootstrap/Col/";
import Row from "react-bootstrap/Row/";
import Form from "react-bootstrap/Form/";
import { Button } from "react-bootstrap";
import axios from "axios";
import { DataGrid } from '@mui/x-data-grid';


export default function Payout() {
  const [zoneOptions, setZoneOptions] = useState([]);
  const [selectedZona, setSelectedZone] = useState("");
  const [zone1Payouts, setZone1Payouts] = useState([]);
  const [zone2Payouts, setZone2Payouts] = useState([]);
  const [editedPayout, setEditedPayout] = useState(null);
  const handleEditClick = (payout) => {
    setEditedPayout(payout);
  };
  const handleEditSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const updatedPayout = {
      amount: formData.get("amount"),
      date: formData.get("date"),
    };

    try {
      const response = await axios.put(
        `http://127.0.0.1:8000/api/payout/${editedPayout.id}/`, // Use the correct endpoint with the primary key
        updatedPayout
      );
    
      if (response.status === 200) {
        console.log("Payout updated successfully");
        // Refresh the UI or update the payouts state as needed
        setEditedPayout(null); // Clear the editedPayout state
      } else {
        console.log("Failed to update payout");
      }
    } catch (error) {
      console.error("An error occurred while updating payout:", error);
    }
  };
  useEffect(() => {
    loadZones();
    loadZone1Payouts();
    loadZone2Payouts();
  }, []);
  const loadZone1Payouts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/payout/?zone_id_filter=1");
      const jsonData = await response.json();
      setZone1Payouts(jsonData);
    } catch (error) {
      console.error("Error fetching Zone 1 payouts:", error);
    }
  };
  
  const loadZone2Payouts = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/payout/?zone_id_filter=2");
      const jsonData = await response.json();
      setZone2Payouts(jsonData);
    } catch (error) {
      console.error("Error fetching Zone 2 payouts:", error);
    }
  };

  const loadZones = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/zone/");
      let jsonData = await response.json();
      setZoneOptions(jsonData);
    } catch (error) {
      console.error("Error fetching zona options:", error);
    }
  };

  const handleSelectChange = (event) => {
    setSelectedZone(event.target.value);
  };
  
  const handleSubmit = async (event) => {
    event.preventDefault();
  
    const formData = new FormData(event.target);
    const payload = {
      amount: formData.get("amount"),
      date: formData.get("date"),
      zone: selectedZona, // Use the selectedZona state here
    };
  
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/api/payout/",
        payload
      );
  
      console.log(payload);
  
      if (response.status === 201) {
        console.log("Payout added successfully");
        // Perform any further actions, such as refreshing the UI
      } else {
        console.log("Failed to add payout");
      }
    } catch (error) {
      console.error("An error occurred while adding payout:", error);
    }
  };
  

  return (
    <div className='container-report mt-5 mx-auto'>
              <div className='container-titulo-report '>
              <h1> Maestro Montos </h1>
          </div>
          <div className='contenedor-linea-report'>
              <hr className='linea-report'></hr>
          </div>
    <form onSubmit={handleSubmit}>
      <label>Amount:</label>
      <input type="number" name="amount" required />
      <br />
      <label>Date:</label>
      <input type="date" name="date" required />
      <br />
      <Form.Label className="mb-1">Zona</Form.Label>
      <Form.Select
name="zoneCR"
as="select"
value={selectedZona}
onChange={handleSelectChange}
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
      <br />
      <button type="submit">Add Payout</button>
    </form>
  
      {editedPayout && (
        <div>
          <h2>Edit Payout</h2>
          <form onSubmit={handleEditSubmit}>
            <label>Amount:</label>
            <input
              type="number"
              name="amount"
              defaultValue={editedPayout.amount}
              required
            />
            <br />
            <label>Date:</label>
            <input
              type="date"
              name="date"
              defaultValue={editedPayout.date}
              required
            />
            <br />
            <button type="submit">Update Payout</button>
          </form>
        </div>
      )}
  
      <div>
        <h2>Zone 1 Payouts</h2>
        <DataGrid
          rows={zone1Payouts}
          columns={[
            { field: 'id', headerName: 'ID', width: 70 },
            { field: 'amount', headerName: 'Amount', width: 130 },
            { field: 'date', headerName: 'Date', width: 130 },
            {
              field: 'actions',
              headerName: 'Actions',
              width: 120,
              renderCell: (params) => (
                <Button onClick={() => handleEditClick(params.row)}>Edit</Button>
              ),
            },
          ]}
          autoHeight
          pageSize={5}
        />
      </div>
      <div>
        <h2>Zone 2 Payouts</h2>
        <DataGrid
          rows={zone2Payouts}
          columns={[
            { field: 'id', headerName: 'ID', width: 70 },
            { field: 'amount', headerName: 'Amount', width: 130 },
            { field: 'date', headerName: 'Date', width: 130 },
            {
              field: 'actions',
              headerName: 'Actions',
              width: 120,
              renderCell: (params) => (
                <Button onClick={() => handleEditClick(params.row)}>Edit</Button>
              ),
            },
          ]}
          autoHeight
          pageSize={5}
        />
      </div>
    </div>
  );
}

