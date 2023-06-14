import { Box, IconButton, Typography, useTheme } from "@mui/material";
import { tokens } from "../../../theme";
import DownloadOutlinedIcon from "@mui/icons-material/DownloadOutlined";
import VaccinesSharpIcon from '@mui/icons-material/VaccinesSharp';
import PersonAddIcon from "@mui/icons-material/PersonAdd";
import Header from "../../Charts/Header";
import LineChart from "../../Charts/LineChart2";
import StatBox from "../../StatBox";
import { useState, useEffect } from "react";
import "react-pro-sidebar/dist/css/styles.css";
import Vaccine_Manager_Sidebar from "../Vaccine_Manager_Sidebar/Sidebar";
import { useNavigate } from "react-router-dom";
import Topbar from '../../../scenes/global/Topbar'
import endpoint from "../../../apibackend";

const baseURL = `${endpoint}getDEPIforVM`
const baseURL2 = `${endpoint}countVaccineAssignedToDirectorEPI`;
const baseURL3 = `${endpoint}countvac`;
const baseURL4 = `${endpoint}savevac`;

const Vaccine_Manager_Dashboard = (props) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [isSidebar, setIsSidebar] = useState(true);

  const [VaccinesCount, setVaccinesCount] = useState(0);
  const [AssignedVaccinesCount, setAssignedVaccinesCount] = useState(0);
  const [EPIsCount, setEPIsCount] = useState(0);
  const [vac, setvac] = useState([]);
  const navigate = useNavigate();


  useEffect(() => {
    if (props.Email) {
      fetch(`${baseURL}/?VM_Email=${props.Email}`)
        .then((data) => data.json())
        .then((data) => setEPIsCount(data.count))
    }
  }, [props.Email])


  useEffect(() => {
    fetch(baseURL2)
      .then((data) => data.json())
      .then((data) => setAssignedVaccinesCount(data))
  }, [])

  useEffect(() => {
    fetch(baseURL3)
      .then((data) => data.json())
      .then((data) => setVaccinesCount(data))
  }, [])

  useEffect(() => {
    fetch(baseURL4)
      .then((data) => data.json())
      .then((data) => setvac(data))
  }, [])

   
  return (
    <>
    <div className="app">
    <Vaccine_Manager_Sidebar isSidebar={isSidebar} />
    <main className="content">
    <Topbar setIsSidebar={setIsSidebar} />
    <div className="Dashboard">
    <Box m="20px">
      {/* HEADER */}
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Header title="Vaccine Manager Dashboard" subtitle="Welcome to your dashboard" />       
      </Box>

      {/* GRID & CHARTS */}
      <Box
        display="grid"
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="140px"
        gap="20px"
      >
        {/* ROW 1 */}
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[900]}
          display="flex"
          alignItems="center"
          justifyContent="center"
          sx={{ borderRadius: '13px' }}
          onClick={()=> navigate("/VaccineData")}
        >
          <StatBox
            title={VaccinesCount.toLocaleString("en-US")}
            subtitle="Total Vaccines"
            progress="0.50"
            increase="+21%"
            icon={
              <VaccinesSharpIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[600]}
          display="flex"
          alignItems="center"
          justifyContent="center"
          sx={{ borderRadius: '13px' }}
          onClick={()=> navigate("/EPI_Data_View")}
        >
          <StatBox
            title={EPIsCount.toLocaleString("en-US")}
            subtitle="Director EPIs"
            progress="0.80"
            increase="+43%"
            icon={
              <PersonAddIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
          
        </Box>

        <Box
          gridColumn="span 3"
          backgroundColor={colors.primary[700]}
          display="flex"
          alignItems="center"
          justifyContent="center"
          sx={{ borderRadius: '13px' }}
          onClick={()=> navigate("/DEPI_Assigned_Vaccines")}
        >
          <StatBox
            title={AssignedVaccinesCount.toLocaleString("en-US")}
            subtitle="Assigned Vaccines"
            progress="0.80"
            increase="+43%"
            icon={
              <VaccinesSharpIcon
                sx={{ color: colors.greenAccent[600], fontSize: "26px" }}
              />
            }
          />
        </Box>
        
        

        {/* ROW 2 */}
        <Box
          gridColumn="span 8"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          sx={{ borderRadius: '13px' }}
        >
          <Box
            mt="25px"
            p="0 30px"
            display="flex "
            justifyContent="space-between"
            alignItems="center"
            sx={{ borderRadius: '13px' }}
          >
            <Box>
              <Typography
                variant="h5"
                fontWeight="600"
                color={colors.grey[100]}
              >
                Director EPI Data
              </Typography>
              <Typography
                variant="h3"
                fontWeight="bold"
                color={colors.greenAccent[500]}
              >
             
              </Typography>
            </Box>
            <Box>
              <IconButton>
                <DownloadOutlinedIcon
                  sx={{ fontSize: "26px", color: colors.greenAccent[500] }}
                />
              </IconButton>
            </Box>
          </Box>
          <Box height="250px" m="-20px 0 0 0">
            <LineChart isDashboard={true} />
          </Box>
        </Box>
        <Box
          gridColumn="span 4"
          gridRow="span 2"
          backgroundColor={colors.primary[400]}
          overflow="auto"
          sx={{ borderRadius: '13px' }}
        >
          <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            borderBottom={`4px solid ${colors.primary[500]}`}
            colors={colors.grey[100]}
            p="15px"
          >
            <Typography color={colors.grey[100]} variant="h5" fontWeight="600">
              Recent Vaccines
            </Typography>
          </Box>
          {vac.map((transaction, i) => (
            <Box
              key={`${transaction.id}-${i}`}
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              borderBottom={`4px solid ${colors.primary[500]}`}
              p="15px"
            >
              <Box>
                <Typography
                  color={colors.greenAccent[500]}
                  variant="h5"
                  fontWeight="600"
                >
                  {transaction.id}
                </Typography>
                <Typography color={colors.grey[100]}>
                  {transaction.vaccineName}
                </Typography>
              </Box>
              <Box color={colors.grey[100]}>{transaction.vaccinetype}</Box>
              <Box
                backgroundColor={colors.greenAccent[500]}
                p="5px 10px"
                borderRadius="4px"
              >
                {transaction.vaccinequantity}
              </Box>
            </Box>
          ))}
        </Box>        
        
      </Box>
    </Box>
    </div>
    </main>
    </div>
    </>
    );
};

export default Vaccine_Manager_Dashboard;
