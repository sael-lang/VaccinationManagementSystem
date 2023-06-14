import { Box } from "@mui/material";
import { DataGrid, GridToolbar, GridCellParams, GridColDef, GridCellValue, GridCellEditStopReasons } from "@mui/x-data-grid";
import { tokens } from "../../../theme";
import Header from "../../Charts/Header";
import { useTheme } from "@mui/material";
import Vaccine_Manager_Sidebar from "../Vaccine_Manager_Sidebar/Sidebar";
// import axios from "axios";
import React from "react";
import { useState, useEffect } from "react";
import Topbar from "../../../scenes/global/Topbar";
import endpoint from "../../../apibackend";
const baseURL = `${endpoint}saveVaccineAssignedToDirectorEPI`;


const DEPI_Assigned_Vaccines = () => {
  const [isSidebar, setIsSidebar] = useState(true);
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [tableData, setTableData] = useState([]);


  let headerName;
  let updateValue;
  var respons;

  const [new_Quantity, setNew_Quantity] = useState(0);
  const [updateValueID, setUpdateValueID] = useState();

  const updateData = async() =>
  {
      // let formField = new FormData()
      // console.log(updateValueID)
      // console.log(new_Quantity)
      // formField.append('id', updateValueID)
      // formField.append(headerName, new_Quantity)
      //      await axios({
      //       method: 'put',
      //       url:'http://127.0.0.1:8000/saveVaccineAssignedToDirectorEPI',
      //       data: formField
      //     }).then(response =>{  
      //        respons=response.status;
             
      //       })
      console.log('yet to be implemented')
  }


  useEffect(() => {
    fetch(baseURL)
      .then((data) => data.json())
      .then((data) => setTableData(data))
  }, [])

  const onRowsSelectionHandler = (ids) => {
    const selectedRowsData = ids.map((id) => tableData.find((row) => row.id === id));
    setUpdateValueID(selectedRowsData[0].id);
    console.log(updateValueID);
  };

  const columns: GridColDef[] = [
    { field: "id", headerName: "Serial No#", flex: 0.5},
    { field: "directorEPIfullName", headerName: "Director EPI Name", flex: 0.5},
    { field: "vaccineName", headerName: "Vaccine Name", flex: 1, editable: true, valueParser: (value: GridCellValue, params: GridCellParams) => {
      headerName = ('updatevaccineName');
      updateValue = value;
    } },
    {
      field: "Vaccine_Quantity",
      headerName: "Vaccine Quantity",
      flex: 1,
      cellClassName: "name-column--cell",
      editable: true,
        valueParser: (value: GridCellValue, params: GridCellParams) => {
          headerName = ('Vaccine_Quantity');
          setNew_Quantity(value);
      }
    },
  ];

  return (
    <>
    <div className="app">
    <Vaccine_Manager_Sidebar isSidebar={isSidebar} />
    <main className="content">
    <Topbar setIsSidebar={setIsSidebar} />
    <div className='Contacts'>
    <Box m="20px">
      <Header
        title="Vaccines"
        subtitle="List of Vaccines saved in the Database"
      />
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
          "& .MuiDataGrid-toolbarContainer .MuiButton-text": {
            color: `${colors.grey[100]} !important`,
          },
        }}
      >
        <DataGrid
          rows={tableData}
          columns={columns}
          components={{ Toolbar: GridToolbar }}
          experimentalFeatures={{ newEditingApi: true }}
          onSelectionModelChange={(ids) => onRowsSelectionHandler(ids)}
          onCellEditStop={(params: GridCellEditStopParams, event: MuiEvent) => {
            if (params.reason === GridCellEditStopReasons.enterKeyDown) {
              updateData();
            }
          }}
          initialState={{
            sorting: {
              sortModel: [{ field: 'id', sort: 'asc' }],
            },
          }}
        />
      </Box>
    </Box>
    </div>
    </main>
    </div>
    </>
  );
};

export default DEPI_Assigned_Vaccines;
