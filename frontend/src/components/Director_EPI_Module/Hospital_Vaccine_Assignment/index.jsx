import React,{useState, useEffect} from 'react';
import { Box, Button, TextField, MenuItem } from "@mui/material";
import { useNavigate} from 'react-router-dom'; 
import useMediaQuery from "@mui/material/useMediaQuery";
import Header from "../../Charts/Header";
import Director_EPI_Sidebar from '../Director_EPI_Sidebar/Sidebar';
import axios from 'axios';
import Topbar from '../../../scenes/global/Topbar';
import { Formik } from 'formik';
import endpoint from '../../../apibackend';

const Hospital_Vaccination_Assignment = (props) => {
  const isNonMobile = useMediaQuery("(min-width:600px)");
  const [isSidebar, setIsSidebar] = useState(true);


  const [Vaccine_Quantity, setVaccine_Quantity]=useState();

  const [HospitalIDs, setHospitalIDs] = useState([]);
  const [selectedHospitalIDs, setselectedHospitalIDs] = useState("");

  const [VaccineIDs, setVaccineIDs] = useState([]);
  const [selectedVaccineIDs, setselectedVaccineIDs] = useState("");

  const [QuantityInStock, setQuantityInStock] = useState("");

  const [check, setCheck] = useState('');
  const [error, setError] = useState('');
  

  const DirectorEPI_Email = props.Email;
  const history = useNavigate();
  var respons;

  const baseURL = `${endpoint}getHospitalForDirectorEPI`;

  useEffect(() => {
    if (props.Email) {
      fetch(`${endpoint}CheckAssignmentViewForHospital/?assigned_vaccine_id=${selectedVaccineIDs}&Hospital_ID=${selectedHospitalIDs}`)
        .then((data) => data.json())
        .then((data) => setCheck(data))
    }
  }, [selectedVaccineIDs, selectedHospitalIDs])

  useEffect(() => {
    if (props.Email) {
      fetch(`${baseURL}/?directorEPIEmail=${props.Email}`)
      .then((data) => data.json())
      .then((data) => setHospitalIDs(data))
    }
  }, [props.Email])

  useEffect(() => {
    if(props.Email)
    {
    axios.get(`${endpoint}getVaccinesForDEPI/?DEPI_Email=${props.Email}`)
      .then(response => {
        setVaccineIDs(response.data);
      })
      .catch(error => {
        console.log(error);
      });
    }
  }, []);

  useEffect(() => {
    axios.get(`${endpoint}getVacForDEPI/?assigned_vaccine_id=${selectedVaccineIDs}&directorEPIEmail=${props.Email}`)
      .then(response => {
        setQuantityInStock(response.data[0].Vaccine_Quantity)
      })
      .catch(error => {
        console.log(error);
      });
  }, [selectedVaccineIDs]);
  
  const anotherFunction=()=>{
    setError("")
    };
  const saveData = async(event) =>
{
    event.preventDefault();
    if(!selectedHospitalIDs || !selectedVaccineIDs || !QuantityInStock)
    {
      setError("Please fill all the fields!")
      return;
    }
    let QuantityInHospitalStock;
    if(check.assignment_exists)
    {
      let formField = new FormData()
      formField.append('Hospital_ID', selectedHospitalIDs)
      formField.append('assigned_vaccine_id', selectedVaccineIDs)
      formField.append('QuantityInStock', QuantityInStock)
      await axios({
        method: 'put',
        url:`${endpoint}saveVaccineAssignedToHospital`,
        data: formField
      }).then(response =>{  
         console.log(response.data)
         QuantityInHospitalStock = response.data.Vaccine_Quantity
         console.log(QuantityInStock)
         return            
        })
        if(QuantityInStock-Vaccine_Quantity >= 0)
      {
        formField.append('newQuantity', parseInt(QuantityInHospitalStock) + parseInt(Vaccine_Quantity));
        formField.append('oldQuantity', parseInt(QuantityInStock) - parseInt(Vaccine_Quantity));
        await axios({
          method: 'put',
          url:`${endpoint}updatingVacQuantityForHospital`,
          data: formField
        }).then(response =>{  
           respons=response.status;
           console.log(response.data)            
          })
          if (respons==200)
          {
            history("/Director_EPI_Dashboard", { replace: true })
            return 
            }
      }
      else{
        setError("Assignment Quantity exceeds quantity in stock")
      }
    }
    let formField = new FormData()
    formField.append('Hospital_ID',selectedHospitalIDs)
    formField.append('assigned_vaccine_id',selectedVaccineIDs)
    formField.append('Vaccine_Quantity',Vaccine_Quantity)
    formField.append('DirectorEPI_Email',DirectorEPI_Email)
         await axios({
          method: 'POST',
          url:`${endpoint}saveVaccineAssignedToHospital`,
          data: formField
        }).then(response =>{  
           respons=response.status;
            console.log(respons);
          })
          // eslint-disable-next-line
if (respons==200){
        history("/director_epi_dashboard", { replace: true }) 
   }
   else{ 
    history("/signup")
}
}

  return (
    <>
    <div className="app">
    <Director_EPI_Sidebar isSidebar={isSidebar} />
    <main className="content">
    <Topbar setIsSidebar={setIsSidebar}/>
    <div className="form">
    <Box m="20px">
      <Header title="Assign Vaccine" subtitle="Assign Vaccine To a Hospital" />

      <Formik
        onSubmit={saveData}
      >
        {({
          handleBlur,
        }) => (
          <form onSubmit={saveData}>
            <Box
              display="grid"
              gap="30px"
              gridTemplateColumns="repeat(4, minmax(0, 1fr))"
              sx={{
                "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
              }}
            >

              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Hospital ID"
                onBlur={handleBlur}
                onChange={(e) => {
                  setselectedHospitalIDs(e.target.value);
                  anotherFunction();
                }}
                value={selectedHospitalIDs}
                name="HospitalID"
                select
                // SelectProps={{ native: true }}
                sx={{ gridColumn: "span 4" }}
              >
                {HospitalIDs.map((hospital) => (
                  <MenuItem key={hospital.id} value={hospital.id}>
                    {`${hospital.id} - ${hospital.hospitalName}`}
                  </MenuItem>
                ))}
              </TextField>


              <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Vaccine ID"
                onBlur={handleBlur}
                onChange={(e) => {
                  setselectedVaccineIDs(e.target.value);
                  anotherFunction();
                }}
                value={selectedVaccineIDs}
                name="Vaccine_ID"
                select
                sx={{ gridColumn: "span 2" }}
              >
                {VaccineIDs.map((vaccine) => (
                  <MenuItem key={vaccine.assigned_vaccine_id} value={vaccine.assigned_vaccine_id}>
                    {`${vaccine.assigned_vaccine_id} - ${vaccine.vaccineName}`}
                  </MenuItem>
                ))}
              </TextField>


               <TextField
                fullWidth
                variant="filled"
                type="text"
                label="Vaccine Quantity"
                onBlur={handleBlur}
                onChange={(e)=>{setVaccine_Quantity(e.target.value);
                  anotherFunction();}}
                value={Vaccine_Quantity}
                name="Vaccine_Quantity"
                sx={{ gridColumn: "span 2" }}
              />
                
            </Box>
            <div className='errorMsg'>{error}</div>
            <Box display="flex" justifyContent="end" mt="20px">
              <Button type="submit" color="secondary" variant="contained">
                Assign 
              </Button>
            </Box>
          </form>
        )}
      </Formik>
    </Box>
    </div>
    </main>
    </div>
    </>
  );
};


export default Hospital_Vaccination_Assignment;
