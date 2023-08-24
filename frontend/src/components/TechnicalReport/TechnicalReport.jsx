import React, {useRef} from 'react'
import './TechnicalReport.css';

import Col from 'react-bootstrap/Col/';
import Row from 'react-bootstrap/Row/';
import Form from 'react-bootstrap/Form/';
import Button from 'react-bootstrap/Button/';
import Table from 'react-bootstrap/Table/';
import InputGroup from 'react-bootstrap/InputGroup/';
import { DataGrid } from '@mui/x-data-grid';
import { GridColDef } from '@mui/x-data-grid';
import axios from 'axios'; // Import axios
import { useState, useEffect } from 'react';
import DownloadPDF from './DownloadPDF/DownloadPDF';

export default function TechnicalReport() {
    
        const [zoneOptions, setZoneOptions] = useState([]);
        const [selectedZone, setSelectedZone] = useState("");
        const [cribrooms, setCribrooms] = useState([]);
        const [startDate, setStartDate] = useState(""); // New state for start date
        const [endDate, setEndDate] = useState("");     // New state for end date    
        const [selectedCribrooms, setSelectedCribrooms] = useState([]); // New state for selected crib rooms
        const handleCheckboxChange = (event, row) => {
            const updatedSelectedCribrooms = event.target.checked
                ? [...selectedCribrooms, row] // Add to selected crib rooms
                : selectedCribrooms.filter(crib => crib.id !== row.id); // Remove from selected crib rooms
            setSelectedCribrooms(updatedSelectedCribrooms);
        };

        const iframeRef = useRef();
        const handlePdfClick = () => {
            // Implement your PDF generation logic here
            console.log('Generate PDF logic will be implemented here');
            console.log('Selected Start Date:', startDate);
            console.log('Selected End Date:', endDate);
            console.log('Selected Crib Rooms:', selectedCribrooms);

            // Iterate through each selected cribroom and send a GET request
            selectedCribrooms.forEach(cribroom => {
              const url = `http://127.0.0.1:8000/api/technical-report/${cribroom.id}/${startDate}/${endDate}/`;
              
              fetch(url)
                  .then(response => {
                      if (!response.ok) {
                          throw new Error('Network response was not ok');
                      }
                      return response.json();
                  })
                  .then(data => {
                      // Handle the data received from the API for each cribroom
                      console.log('API Response for Cribroom', cribroom.id, data, data.pays);
                      DownloadPDF(
                        iframeRef,
                        cribroom.entity,
                        cribroom.name,
                        cribroom.code,
                        cribroom.street,
                        cribroom.house_number,
                        cribroom.locality.locality,
                        cribroom.department.department,
                        data.pays.totalSumStr,
                        data.pays.totalSumInitMonth,
                        data.pays.totalSumInitYear,
                        data.pays.totalSumEndMonth,
                        data.pays.totalSumEndYear,
                        data.maxCapacityStr,
                        cribroom.max_capacity,
                        data.pays.firstSubTotalSumEndMonth,
                        data.pays.SecSubTotalSumInitMonth,
                        data.pays.totalSumFloat,
                        data.pays.firstSubTotalSumFloat,
                        data.pays.SecSubTotalSumFloat
                        );
                  })
                  .catch(error => {
                      console.error('Error fetching data:', error);
                  });
          });

        };
        useEffect(() => {
          loadZones();
        }, []);
    
        useEffect(() => {
          if (selectedZone) {
            loadCribrooms(selectedZone);
          }
        }, [selectedZone]);
    
        const loadCribrooms = async (zoneId) => {
          try {
            const response = await axios.get(`http://127.0.0.1:8000/api/cribroom/?zone=${zoneId}`);
            const jsonData = response.data;
            setCribrooms(jsonData);
          } catch (error) {
            console.error("Error fetching cribrooms:", error);
          }
        };
    
        const loadZones = async () => {
          try {
            const response = await axios.get("http://127.0.0.1:8000/api/zone/");
            const jsonData = response.data;
            setZoneOptions(jsonData);
          } catch (error) {
            console.error("Error fetching zone options:", error);
          }
        };
    
        const handleSelectChange = (event) => {
          setSelectedZone(event.target.value);
        };
    
        const columns = [
            { field: 'code', headerName: 'Codigo' },
            { field: 'name', headerName: 'Nombre Sala' },
            { field: 'cuit', headerName: 'CUIT' },
            { field: 'entidad', headerName: 'Entidad' },
            { field: 'cantidad_ninos', headerName: 'Cantidad de Niños' },
            {
                field: 'select',
                headerName: 'Seleccionar',
                sortable: false,
                filterable: false,
                width: 120,
                renderCell: (params) => (
                    <input
                    type="checkbox"
                    checked={selectedCribrooms.some(crib => crib.id === params.row.id)}
                    onChange={(e) => handleCheckboxChange(e, params.row)}
                />
                ),
            },
        ];
        
    
        return (
            <div className='container-report mt-5 mx-auto'>
                <div className='container-titulo-report '>
                    <h1>Informe Tecnico</h1>
                </div>
                <div className='contenedor-linea-report'>
                    <hr className='linea-report'></hr>
                </div>
                <Row className="mb-3">
                    <Col>
                        <div className='input-select'>
                            <Form.Select
                                name="zoneCR"
                                as="select"
                                value={selectedZone}
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
                        </div>
                    </Col>
                    <Col>
                    <iframe ref={iframeRef} style={{ display: 'none' }} title="PDFFrame" />
                    <Button variant="primary" onClick={handlePdfClick} className="mb-3">
                        PDF
                    </Button>
                    </Col>
                </Row>
                <Row className="mb-3">
                <Col>
                    {/* Start Date Selector */}
                    <InputGroup className="mb-3">
                        <InputGroup.Text>Start Date</InputGroup.Text>
                        <Form.Control
                            type="date"
                            value={startDate}
                            onChange={(e) => setStartDate(e.target.value)}
                        />
                    </InputGroup>
                </Col>
                <Col>
                    {/* End Date Selector */}
                    <InputGroup className="mb-3">
                        <InputGroup.Text>End Date</InputGroup.Text>
                        <Form.Control
                            type="date"
                            value={endDate}
                            onChange={(e) => setEndDate(e.target.value)}
                        />
                    </InputGroup>
                </Col>
            </Row>

    
                <div>
                    <div style={{ height: 400, width: '100%' }}>
                        <DataGrid rows={cribrooms} columns={columns} columnBuffer={2} columnThreshold={2} />
                    </div>
                </div>
            </div>
        );
    }