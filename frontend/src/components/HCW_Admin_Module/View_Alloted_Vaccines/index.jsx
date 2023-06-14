import { Box } from "@mui/material";
import { DataGrid, GridToolbar, GridCellParams, GridColDef, GridCellValue } from "@mui/x-data-grid";
import { tokens } from "../../../theme";
import Header from "../../Charts/Header";
import { useTheme } from "@mui/material";
import HCW_Admin_Sidebar from "../HCW_Admin_Sidebar/Sidebar";
import React from "react";
import { useState, useEffect } from "react";
import Topbar from "../../../scenes/global/Topbar";
import endpoint from "../../../apibackend";
const baseURL = `${endpoint}getVaccineAssignedToHCWA`;


const HCWA_Alloted_Vaccines = (props) => {
  const theme = useTheme();
  const [isSidebar, setIsSidebar] = useState(true);

  const colors = tokens(theme.palette.mode);
  const [tableData, setTableData] = useState([]);
  useEffect(() => {
    fetch(`${baseURL}/?HCWA_Email=${props.Email}`)
      .then((data) => data.json())
      .then((data) => setTableData(data.vaccine_records))
  }, [])

  const columns: GridColDef[] = [
    { field: "id", headerName: "Serial#", flex: 0.5, editable: true, valueParser: (value: GridCellValue, params: GridCellParams) => {
      console.log(value);
    } },
    { field: "vaccineName", headerName: "Vaccine Name", flex: 1,editable: true, valueParser: (value: GridCellValue, params: GridCellParams) => {
      console.log(value);
    } },
    {
      field: "Vaccine_Quantity",
      headerName: "Vaccine Quantity",
      flex: 1,
      cellClassName: "name-column--cell",
      editable: true,
        valueParser: (value: GridCellValue, params: GridCellParams) => {
        console.log(value);
      }
    },
    {
      field: "HCWA_fullName",
      headerName: "Assigned to",
      flex: 1,
      cellClassName: "name-column--cell",
      editable: true,
        valueParser: (value: GridCellValue, params: GridCellParams) => {
        console.log(value);
      }
    },

    {
        field: "directorEPI_Email",
        headerName: "Assigned By",
        flex: 1,
        cellClassName: "name-column--cell",
        editable: true,
          valueParser: (value: GridCellValue, params: GridCellParams) => {
          console.log(value);
        }
      },
    
  ];

  return (
    <>
     <div className="app">
    <HCW_Admin_Sidebar isSidebar={isSidebar} />
    <main className="content">
    <Topbar setIsSidebar={setIsSidebar} />
    <div className='Contacts'>
    <Box m="20px">
      <Header
        title="Assigned Vaccies"
        subtitle="List of Assigned Vaccines"
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
        />
      </Box>
    </Box>
    </div>
    </main>
    </div>
    </>
  );
};

export default HCWA_Alloted_Vaccines;
